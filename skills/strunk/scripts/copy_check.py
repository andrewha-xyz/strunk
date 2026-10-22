#!/usr/bin/env python3
# /// script
# requires-python = ">=3.11"
# dependencies = []
# ///
"""Lint interface text against The Elements of Style.

    uv run --locked "<skill dir>/scripts/copy_check.py" en.json
    uv run --locked "<skill dir>/scripts/copy_check.py" --text "In order to continue, please note that you must sign in."
    echo "Oops! Something went wrong" | uv run --locked "<skill dir>/scripts/copy_check.py" --json

Input: a strings file (.json flat or nested, Apple .strings, Android strings.xml, gettext .po),
a plain-text file (one string per paragraph), --text, or stdin.

Rules (1918 numbering; V.n = White's reminder n, 4th.12 = the consistency rule):
  10  passive voice hides the actor            11  negative where an instruction belongs
  12  vague where the object or number belongs 13  needless words
  15  OK/Cancel instead of the two answers     V.7 overstatement   V.8 qualifiers
  V.9 breezy manner, emoji                     V.10 mixed case / ellipsis across a file
  V.14 fancy words                             4th.12 two words for one thing across a file

Severity: warn (fix or justify) or note (look). Exit 0 when nothing warns, 1 when something does,
2 on a usage error or a file that cannot be parsed (with --json the report is {"error": ...}).
The linter finds candidates; the writer decides. It cannot see the screen.
"""
import argparse
import json
import re
import sys
import xml.etree.ElementTree as ET
from collections import Counter
from pathlib import Path

W = "warn"
N = "note"

# (pattern, rule, severity, instead, note). Patterns are matched case-insensitively on word boundaries.
PHRASES = [
    # rule 13: needless words
    (r"in order to", "13", W, "to", ""),
    (r"in order for", "13", W, "for", ""),
    (r"due to the fact that", "13", W, "because", ""),
    (r"owing to the fact that", "13", W, "because", ""),
    (r"in spite of the fact that", "13", W, "although", ""),
    (r"the fact that", "13", W, "", "recast the sentence"),
    (r"as to whether", "13", W, "whether", ""),
    (r"there is no doubt but that", "13", W, "no doubt", ""),
    (r"for the purpose of", "13", W, "to", ""),
    (r"in the event that", "13", W, "if", ""),
    (r"at this (?:point in )?time", "13", W, "now", "or delete"),
    (r"at the present time", "13", W, "now", "or delete"),
    (r"at the moment", "13", W, "", "delete; the present tense says it"),
    (r"currently", "13", W, "", "delete; the present tense says it"),
    (r"subsequent to", "13", W, "after", ""),
    (r"in a timely manner", "13", W, "", "give the time"),
    (r"a number of", "13", W, "", "give the number"),
    (r"(?:is|are|be|was|were) able to", "13", W, "can", ""),
    (r"has the ability to", "13", W, "can", ""),
    (r"please note that", "13", W, "", "delete the frame; say the thing"),
    (r"please be aware that", "13", W, "", "delete the frame; say the thing"),
    (r"note that", "13", W, "", "delete the frame; say the thing"),
    (r"keep in mind that", "13", W, "", "delete the frame; say the thing"),
    (r"it is recommended that", "13", W, "", "use the imperative, or name who recommends and why"),
    (r"successfully", "13", W, "", "delete; a past-tense verb already succeeded"),
    (r"simply", "13", W, "", "delete; the user judges what is simple"),
    (r"easily", "13", W, "", "delete; the user judges what is easy"),
    (r"just", "13", N, "", "delete unless it means 'only' or 'a moment ago'"),
    (r"make use of", "13", W, "use", ""),
    (r"in the process of", "13", W, "", "delete"),
    (r"(?:which|who|that) (?:is|was|are|were)", "13", N, "", "relative pronoun plus 'be' is often superfluous: 'the file which is selected' is 'the selected file'"),
    (r"you can", "13", N, "", "often the imperative or the fact is enough"),
    (r"please", "13", N, "", "delete from instructions; keep when asking a favour the user may refuse"),
    # chapter V and extension (lexicon.md)
    (r"prior to", "V.14", W, "before", ""),
    (r"utili[sz]e", "V.14", W, "use", ""),
    (r"leverage", "V.14", W, "use", ""),
    (r"commence", "V.14", W, "start", ""),
    (r"facilitate", "V.14", W, "help", ""),
    (r"endeavou?r", "V.14", W, "try", ""),
    (r"initiate", "V.14", W, "start", ""),
    (r"terminate", "V.14", W, "end", ""),
    (r"finali[sz]e", "V.14", W, "finish", ""),
    (r"prioriti[sz]e", "V.14", W, "rank", "or recast"),
    (r"in terms of", "V.14", W, "", "recast"),
    (r"hopefully", "ch.V", W, "", "delete"),
    (r"literally", "ch.V", W, "", "delete"),
    (r"etc\.?", "ch.V", W, "", "list the items or give the count"),
    (r"respective(?:ly)?", "ch.V", W, "", "usually delete"),
    (r"(?:in|for) (?:many|most|some|this|that|which) cases?", "ch.V", W, "", "recast without 'case'"),
    # rule 12: vague
    (r"something went wrong", "12", W, "", "say what went wrong, or what to do"),
    (r"an? (?:unexpected |unknown )?error (?:has )?occurred", "12", W, "", "say what went wrong, or what to do"),
    (r"unexpected error", "12", W, "", "say what went wrong, or what to do"),
    (r"are you sure\??", "12", W, "", "ask the question with its object: 'Delete 3 photos?'"),
    (r"invalid (?:input|value|entry|data)", "12", W, "", "say what to enter"),
    (r"click here", "12", W, "", "make the destination the link text"),
    (r"learn more", "12", N, "", "name what the link opens"),
    (r"contact (?:us|support)", "12", N, "", "name the channel: email, call, chat"),
    (r"items?\b", "12", N, "", "the real noun if the product knows it"),
    # rule 10: actor hidden
    (r"there (?:is|are|was|were)", "10", W, "", "make the thing the subject"),
    (r"(?:was|were|is|are) unable to", "10", W, "", "name the actor: 'Couldn't save', 'Your bank declined the card'"),
    (r"(?:could|can) ?not be|(?:couldn|can)'t be", "10", W, "", "name the actor"),
    (r"failed to be", "10", W, "", "name the actor"),
    (r"(?:perform|execute|initiate|complete) (?:a|an|the) \w+", "10", W, "", "use the verb buried in the noun"),
    # rule 11: negative where an instruction belongs
    (r"(?:is|are|was|were) not", "11", W, "", "say what to do instead"),
    (r"(?:isn|aren|wasn|weren|doesn|don|didn)'t", "11", W, "", "say what to do instead"),
    (r"cannot|can't", "11", W, "", "say what to do instead; keep when stating a consequence ('cannot be undone')"),
    (r"invalid|incorrect|wrong", "11", W, "", "say what to enter"),
    (r"\bno\b", "11", N, "", "a negative fact is fine; follow it with the remedy"),
    # rule 15: button pair
    (r"^\s*(?:ok|okay|cancel)\s*$", "15", N, "", "buttons answer the question in its own words: Delete / Keep"),
    # White 7: overstatement
    (r"awesome|amazing|fantastic|incredible|perfect!?|great job|well done|you're all set|woohoo|hooray|yay", "V.7", W, "", "state the fact: Done, Sent, Saved"),
    (r"seamless(?:ly)?|effortless(?:ly)?|powerful|robust|intuitive|lightning[- ]fast|blazing", "V.7", W, "", "the specific fact, or nothing"),
    (r"!{2,}", "V.7", W, "", "one exclamation mark is already one too many"),
    (r"!", "V.7", N, "", "an exclamation mark is a claim of excitement"),
    # White 8: qualifiers
    (r"very|rather|quite|somewhat|a bit|a little|pretty(?= [a-z])|really", "V.8", W, "", "delete, or a stronger word, or the number"),
    # White 9: breezy
    (r"oops|whoops|uh[- ]oh|yikes|oopsie|whoopsie|welp|houston", "V.9", W, "", "the fact and the remedy, in a plain voice"),
    # White 1 / 17: product in the foreground
    (r"we(?:'re| are) (?:excited|thrilled|happy|proud|delighted)", "V.1", W, "", "the product's feelings are not the topic"),
    (r"\bsorry\b", "V.1", N, "", "apologize only for harm the product caused, then say what it will do"),
    (r"we (?:think|believe) you(?:'ll| will) (?:love|enjoy)", "V.17", W, "", "recommend with a reason or not at all"),
]

EMOJI = re.compile("[\U0001F300-\U0001FAFF\U00002600-\U000027BF\U0001F1E6-\U0001F1FF]")
PASSIVE = re.compile(r"\b(?:is|are|was|were|be|been|being)\s+(?:not\s+)?(?:\w+ly\s+)?(\w+)\b", re.I)
IRREGULAR = {"built", "sent", "done", "made", "lost", "found", "set", "put", "read", "kept", "paid", "held", "shown", "sold",
             "hit", "cut", "won", "left", "met", "spent", "told", "thought", "brought", "bought", "caught", "given", "taken",
             "written", "hidden", "chosen", "broken", "forgotten", "known", "seen", "driven", "frozen", "stolen", "spoken",
             "eaten", "beaten", "fallen", "forbidden", "proven", "sung", "struck", "stuck", "swept", "torn", "worn", "thrown",
             "drawn", "withdrawn", "overridden", "rebuilt", "reset", "undone", "redone", "begun", "run", "sent", "lent", "fed", "led", "bred"}
NOT_PARTICIPLE = {"wicked", "naked", "sacred", "hundred", "hatred", "kindred", "crooked", "rugged", "ragged", "jagged", "wretched",
                  "beloved", "indeed", "speed", "need", "exceed", "proceed", "succeed", "agreed", "freed", "shed", "unused"}


def participle(w: str) -> bool:
    w = w.lower()
    return w in IRREGULAR or (w.endswith("ed") and len(w) >= 5 and w not in NOT_PARTICIPLE)
STATE_RESULT = {"saved", "deleted", "sent", "selected", "connected", "synced", "uploaded", "downloaded", "updated",
                "verified", "confirmed", "paid", "blocked", "enabled", "disabled", "required", "removed", "added",
                "archived", "shared", "locked", "hidden", "installed", "signed", "done", "cancelled", "canceled",
                "charged", "billed", "refunded", "notified", "approved", "rejected", "cleared", "logged"}
CONSEQUENCE = re.compile(r"(?:can(?:'t|not)|could(?:n't| not)) be (?:undone|reversed|recovered|restored|changed later)", re.I)

# group -> [(label, pattern)]: two labels of one group in one file is a terminology collision (4th-edition rule 12)
TERMS = {
    "sign in": [("sign in", r"sign in"), ("log in", r"log in"), ("login", r"login"), ("signin", r"signin"), ("log on", r"log on"), ("logon", r"logon")],
    "sign out": [("sign out", r"sign out"), ("log out", r"log out"), ("logout", r"logout"), ("signout", r"signout")],
    "sign up": [("sign up", r"sign up"), ("register", r"register"), ("create account", r"create (?:an )?account"), ("join", r"join")],
    "delete": [("delete", r"delete"), ("remove", r"remove"), ("trash", r"trash"), ("erase", r"erase")],
    "download": [("export", r"export"), ("download", r"download"), ("save to device", r"save to (?:your )?device")],
    "settings": [("settings", r"settings"), ("preferences", r"preferences"), ("options", r"options")],
    "ok": [("ok", r"ok"), ("okay", r"okay"), ("got it", r"got it")],
    "email": [("e-mail", r"e-mail"), ("email", r"email")],
    "close": [("close", r"close"), ("dismiss", r"dismiss")],
    "edit": [("edit", r"edit"), ("modify", r"modify"), ("change", r"change")],
    "search": [("search", r"search"), ("find", r"find"), ("look up", r"look up")],
}

SMALL = {"a", "an", "the", "to", "of", "and", "or", "in", "on", "for", "at", "by", "with", "from", "as", "is", "vs"}


def flatten(obj, prefix=""):
    if isinstance(obj, dict):
        for k, v in obj.items():
            yield from flatten(v, f"{prefix}{k}." if not isinstance(v, str) else f"{prefix}{k}")
    elif isinstance(obj, list):
        for i, v in enumerate(obj):
            yield from flatten(v, f"{prefix}{i}." if not isinstance(v, str) else f"{prefix}{i}")
    elif isinstance(obj, str):
        yield prefix.rstrip("."), obj


ESC = {"n": "\n", "t": "\t", "r": "\r", '"': '"', "'": "'", "\\": "\\", "@": "@", "?": "?"}


def join_surrogates(s: str) -> str:
    return s.encode("utf-16", "surrogatepass").decode("utf-16", "replace")


def unescape_apple(s: str) -> str:
    """Apple .strings escapes: \\n \\t \\" \\\\, \\U with 1-4 hex digits (surrogate pairs joined), octal \\ooo (read as Latin-1; NeXTSTEP Latin is not modelled)."""
    def one(m):
        e = m.group(1)
        if e[0] == "U":
            return chr(int(e[1:], 16))
        if e[0] in "01234567":
            return chr(int(e, 8) & 0xFF)
        return ESC.get(e, e)
    return join_surrogates(re.sub(r"\\(U[0-9A-Fa-f]{1,4}|[0-7]{1,3}|.)", one, s))


def unescape_android(s: str) -> str:
    """Android string-resource escapes: \\n \\t \\" \\' \\\\ \\@ \\? and \\uXXXX (surrogate pairs joined)."""
    def one(m):
        e = m.group(1)
        if e[0] == "u":
            return chr(int(e[1:], 16))
        return ESC.get(e, e)
    return join_surrogates(re.sub(r"\\(u[0-9A-Fa-f]{4}|.)", one, s))


C_ESC = {"n": "\n", "t": "\t", "r": "\r", "v": "\v", "a": "\a", "b": "\b", "f": "\f", '"': '"', "'": "'", "\\": "\\", "?": "?"}


def c_bytes(s: str) -> bytes:
    """gettext (C-style) escapes: \\n \\t \\v \\a \\b \\f \\" \\\\, octal \\ooo and hex \\xh+ as BYTES of the UTF-8 catalog."""
    out = bytearray()
    for m in re.finditer(r"\\([0-7]{1,3}|x[0-9A-Fa-f]+|.)|(.)", s, re.S):
        e, lit = m.group(1), m.group(2)
        if lit is not None:
            out += lit.encode("utf-8", "surrogatepass")
        elif e[0] in "01234567":
            out.append(int(e, 8) & 0xFF)
        elif e[0] == "x":
            out.append(int(e[1:], 16) & 0xFF)
        else:
            out += C_ESC.get(e, e).encode("utf-8")
    return bytes(out)


def unescape_c(fragments: list[str]) -> str:
    return join_surrogates(b"".join(c_bytes(f) for f in fragments).decode("utf-8", "replace"))


def read_text(path: Path) -> str:
    raw = path.read_bytes()
    if raw.startswith((b"\xff\xfe", b"\xfe\xff")):
        return raw.decode("utf-16")
    if raw.startswith(b"\xef\xbb\xbf"):
        return raw.decode("utf-8-sig")
    try:
        return raw.decode("utf-8")
    except UnicodeDecodeError:
        return raw.decode("utf-16")


def parse_strings(raw: str) -> list[tuple[str, str]]:
    """Apple .strings: "key" = "value"; with /* */ and // comments outside strings. Raises ValueError on malformed input."""
    out, i, n, line = [], 0, len(raw), 1

    def skip():
        nonlocal i, line
        while i < n:
            if raw[i] == "\n":
                line += 1; i += 1
            elif raw[i].isspace():
                i += 1
            elif raw.startswith("/*", i):
                j = raw.find("*/", i + 2)
                if j < 0:
                    raise ValueError(f"line {line}: unterminated comment")
                line += raw.count("\n", i, j); i = j + 2
            elif raw.startswith("//", i):
                j = raw.find("\n", i); i = n if j < 0 else j
            else:
                return

    def string():
        nonlocal i, line
        if i >= n or raw[i] != '"':
            raise ValueError(f"line {line}: expected a quoted string")
        j, buf = i + 1, []
        while j < n and raw[j] != '"':
            if raw[j] == "\\":
                buf.append(raw[j:j + 2]); j += 2
            else:
                line += raw[j] == "\n"; buf.append(raw[j]); j += 1
        if j >= n:
            raise ValueError(f"line {line}: unterminated string")
        i = j + 1
        return unescape_apple("".join(buf))

    while True:
        skip()
        if i >= n:
            return out
        k = string(); skip()
        if i >= n or raw[i] != "=":
            raise ValueError(f"line {line}: expected '=' after {k!r}")
        i += 1; skip()
        v = string(); skip()
        if i >= n or raw[i] != ";":
            raise ValueError(f"line {line}: missing ';' after {k!r}")
        i += 1
        out.append((k, v))


def parse_po(raw: str) -> list[tuple[str, str]]:
    """gettext .po: entries need no blank line between them; msgctxt joins the key; msgstr[n] each become a string."""
    entries, cur, field = [], None, None
    for no, line in enumerate(raw.splitlines(), 1):
        st = line.strip()
        if not st or st.startswith("#"):
            continue
        m = re.match(r'^(msgctxt|msgid_plural|msgid|msgstr(?:\[\d+\])?)\s+"((?:[^"\\]|\\.)*)"$', st)
        cont = re.match(r'^"((?:[^"\\]|\\.)*)"$', st)
        if m:
            name = m.group(1)
            if name in ("msgctxt", "msgid") and cur and "msgid" in cur:
                entries.append(cur); cur = None
            cur = cur if cur is not None else {}
            if name in cur:
                raise ValueError(f"line {no}: duplicate {name}")
            cur[name] = [m.group(2)]; field = name
        elif cont and field and cur is not None:
            cur[field].append(cont.group(1))
        else:
            raise ValueError(f"line {no}: cannot parse {st[:60]!r}")
    if cur:
        entries.append(cur)
    for no, e in enumerate(entries, 1):
        if "msgid" not in e:
            raise ValueError(f"entry {no}: msgctxt without msgid")
        if not any(k.startswith("msgstr") for k in e):
            raise ValueError(f"entry {no} ({e['msgid'][:40]!r}): msgid without msgstr")
        if "msgstr" in e and any(k.startswith("msgstr[") for k in e):
            raise ValueError(f"entry {no} ({e['msgid'][:40]!r}): both msgstr and msgstr[n]")
        if ("msgid_plural" in e) != any(k.startswith("msgstr[") for k in e):
            raise ValueError(f"entry {no} ({e['msgid'][:40]!r}): msgid_plural and msgstr[n] must go together")
        for k in list(e):
            e[k] = unescape_c(e[k])
    seen = set()
    for e in entries:
        ident = (e.get("msgctxt"), e["msgid"])
        if ident in seen:
            raise ValueError(f"duplicate message definition {e['msgid'][:40]!r}" + (f" (context {ident[0]!r})" if ident[0] else ""))
        seen.add(ident)
    out = []
    for e in entries:
        msgid = e.get("msgid")
        if not msgid:
            continue
        key = f"{msgid} ({e['msgctxt']})" if e.get("msgctxt") else msgid
        plural = sorted((k for k in e if k.startswith("msgstr[")), key=lambda k: int(k[7:-1]))
        if plural:
            for k in plural:
                i = int(k[7:-1])
                out.append((f"{key}[{i}]", e[k] or (msgid if i == 0 else e.get("msgid_plural", msgid))))
        else:
            out.append((key, e.get("msgstr") or msgid))
    return out


def android_text(t: str) -> str:
    """Android rendering rules: text inside unescaped double quotes is kept verbatim (quotes dropped); outside, whitespace runs collapse to one space and the ends are trimmed."""
    parts, buf, i, quoted = [], [], 0, False
    while i < len(t):
        c = t[i]
        if c == "\\" and i + 1 < len(t):
            buf.append(t[i:i + 2]); i += 2
        elif c == '"':
            parts.append((quoted, "".join(buf))); buf = []; quoted = not quoted; i += 1
        else:
            buf.append(c); i += 1
    parts.append((quoted, "".join(buf)))
    out = [seg if q else re.sub(r"\s+", " ", seg) for q, seg in parts]
    if not parts[0][0]:
        out[0] = out[0].lstrip()
    if not parts[-1][0]:
        out[-1] = out[-1].rstrip()
    return unescape_android("".join(out))


def load(path: Path) -> list[tuple[str, str]]:
    raw = read_text(path)
    suf = path.suffix.lower()
    if suf == ".json":
        return list(flatten(json.loads(raw)))
    if suf == ".strings":
        return parse_strings(raw)
    if suf == ".xml":
        out = []
        for el in ET.fromstring(raw).iter():
            name = el.get("name")
            if el.tag == "string" and name:
                out.append((name, android_text("".join(el.itertext()))))
            elif el.tag in ("plurals", "string-array") and name:
                for i, item in enumerate(el.findall("item")):
                    key = f"{name}[{item.get('quantity')}]" if el.tag == "plurals" else f"{name}[{i}]"
                    out.append((key, android_text("".join(item.itertext()))))
        return out
    if suf == ".po":
        return parse_po(raw)
    paras = [p.strip() for p in re.split(r"\n\s*\n", raw) if p.strip()]
    return [(f"p{i + 1}", p) for i, p in enumerate(paras)]


def words(s: str) -> list[str]:
    return [t for t in re.findall(r"[^\s]+", s) if re.search(r"\w", t)]


def is_title_case(s: str) -> bool:
    ws = [w for w in re.findall(r"[A-Za-z][A-Za-z'’-]*", s) if not (len(w) > 1 and w.isupper())]
    if len(ws) < 3:
        return False
    caps = [w[0].isupper() for w in ws]
    body = [c for w, c in zip(ws[1:], caps[1:]) if w.lower() not in SMALL]
    return caps[0] and len(body) >= 2 and all(body)


def is_sentence_case(s: str) -> bool:
    ws = re.findall(r"[A-Za-z][A-Za-z'’-]*", s)
    if len(ws) < 2:
        return False
    return ws[0][0].isupper() and any(w[0].islower() for w in ws[1:] if w.lower() not in SMALL)


def check_string(key: str, text: str) -> list[dict]:
    out = []
    shown = text
    text = text.replace("\u2019", "'").replace("\u2018", "'")
    consequence = [(m.start(), m.end()) for m in CONSEQUENCE.finditer(text)]
    def in_consequence(m):
        return any(a <= m.start() and m.end() <= b for a, b in consequence)
    for pat, rule, sev, instead, note in PHRASES:
        regex = pat if pat[0] in "^!" else rf"(?<![\w'])(?:{pat})(?![\w'])"
        for m in re.finditer(regex, text, re.I):
            if rule in ("10", "11") and in_consequence(m):
                continue
            out.append(dict(key=key, text=shown, rule=rule, severity=sev, match=shown[m.start():m.end()], instead=instead, note=note))
    for m in PASSIVE.finditer(text):
        part = m.group(1).lower()
        if not participle(part):
            continue
        if any(o["rule"] == "10" and o["match"].lower() in m.group(0).lower() for o in out) or in_consequence(m):
            continue
        if part in STATE_RESULT:
            out.append(dict(key=key, text=shown, rule="10", severity=N, match=m.group(0), instead="",
                            note="passive stating a result; fine when the object is the topic ('Your edits are saved')"))
        else:
            out.append(dict(key=key, text=shown, rule="10", severity=W, match=m.group(0), instead="",
                            note="passive hides the actor; say who did it, or make the object the subject"))
    for m in EMOJI.finditer(text):
        out.append(dict(key=key, text=shown, rule="V.9", severity=W, match=m.group(0), instead="",
                        note="emoji in product copy is breeziness; the fact, in a plain voice"))
    return out


def check_file(strings: list[tuple[str, str]]) -> list[dict]:
    out = []
    seen: dict[str, dict[str, list[str]]] = {}
    for key, text in strings:
        text = text.replace("\u2019", "'")
        for group, variants in TERMS.items():
            for label, v in variants:
                if re.search(rf"(?<![\w'])(?:{v})(?![\w'])", text, re.I):
                    seen.setdefault(group, {}).setdefault(label, []).append(key)
    for group, hits in seen.items():
        if len(hits) > 1:
            parts = [label + " in " + ", ".join(ks[:4]) for label, ks in hits.items()]
            out.append(dict(key="*", text="", rule="4th.12", severity=W, match=group, group=group, instead="",
                            note="one word for one thing: " + "; ".join(parts)))
    multi = [(k, t) for k, t in strings if len(words(t)) >= 2 and "\n" not in t]
    title = [k for k, t in multi if is_title_case(t)]
    sent = [k for k, t in multi if is_sentence_case(t)]
    if title and sent:
        out.append(dict(key="*", text="", rule="V.10", severity=N, match="case", instead="",
                        note=f"Title Case in {', '.join(title[:4])}; sentence case in {', '.join(sent[:4])}. Choose one."))
    dots = [k for k, t in strings if "..." in t]
    ell = [k for k, t in strings if "…" in t]
    if dots and ell:
        out.append(dict(key="*", text="", rule="V.10", severity=N, match="ellipsis", instead="",
                        note=f"'...' in {', '.join(dots[:4])}; '…' in {', '.join(ell[:4])}. Choose one."))
    return out


def report(strings, findings, as_json):
    wc = [len(words(t)) for _, t in strings]
    longest = max(zip(wc, (k for k, _ in strings)), default=(0, ""))
    stats = dict(strings=len(strings), words=sum(wc),
                 mean_words=round(sum(wc) / len(wc), 1) if wc else 0,
                 longest=dict(key=longest[1], words=longest[0]),
                 by_rule=dict(Counter(f["rule"] for f in findings)),
                 warns=sum(f["severity"] == W for f in findings),
                 notes=sum(f["severity"] == N for f in findings))
    if as_json:
        print(json.dumps(dict(stats=stats, findings=findings), ensure_ascii=False, indent=1))
        return
    last = None
    for f in findings:
        if f["key"] != last:
            last = f["key"]
            print(f"\n{f['key']}: {f['text']!r}" if f["text"] else f"\n{f['key']}")
        fix = f" -> {f['instead']}" if f["instead"] else ""
        note = f"  ({f['note']})" if f["note"] else ""
        print(f"  [{f['severity']}] rule {f['rule']}: {f['match']!r}{fix}{note}")
    print(f"\n{stats['strings']} strings, {stats['words']} words, mean {stats['mean_words']}, "
          f"longest {stats['longest']['key']} ({stats['longest']['words']} words); "
          f"{stats['warns']} warn, {stats['notes']} note")


def main():
    ap = argparse.ArgumentParser(description=__doc__, formatter_class=argparse.RawDescriptionHelpFormatter)
    ap.add_argument("path", nargs="?", help="strings file or text file")
    ap.add_argument("--text", help="one string to check")
    ap.add_argument("--json", action="store_true")
    a = ap.parse_args()
    if a.text is not None:
        strings = [("text", a.text)]
    elif a.path:
        p = Path(a.path)
        try:
            if not p.is_file():
                raise FileNotFoundError(f"not a file: {p}")
            strings = load(p)
        except Exception as e:
            if a.json:
                print(json.dumps(dict(error=f"{type(e).__name__}: {e}", path=str(p))))
            else:
                print(f"could not parse {p}: {type(e).__name__}: {e}", file=sys.stderr)
            sys.exit(2)
    elif not sys.stdin.isatty():
        strings = [("stdin", sys.stdin.read().strip())]
    else:
        ap.print_help(); sys.exit(2)
    strings = [(k, join_surrogates(t)) for k, t in strings]
    findings = []
    for k, t in strings:
        findings.extend(check_string(k, t))
    findings.extend(check_file(strings))
    report(strings, findings, a.json)
    sys.exit(1 if any(f["severity"] == W for f in findings) else 0)


if __name__ == "__main__":
    main()
