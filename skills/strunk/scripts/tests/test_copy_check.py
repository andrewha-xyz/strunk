import json
import subprocess
import sys
from pathlib import Path

SCRIPT = Path(__file__).resolve().parents[1] / "copy_check.py"


def run(*args, stdin=None):
    p = subprocess.run(
        [sys.executable, "-I", str(SCRIPT), *args],
        input=stdin, capture_output=True, text=True,
    )
    return p.returncode, p.stdout, p.stderr


def findings(*args, stdin=None):
    code, out, err = run("--json", *args, stdin=stdin)
    assert err == "", err
    return code, json.loads(out)


def test_clean_text_exits_zero():
    code, rep = findings("--text", "Delete 3 photos?")
    assert code == 0
    assert rep["findings"] == []


def test_needless_phrase_rule_13():
    code, rep = findings("--text", "In order to continue, please note that you must sign in.")
    rules = {f["rule"] for f in rep["findings"]}
    assert "13" in rules
    phrases = {f["match"].lower() for f in rep["findings"] if f["rule"] == "13"}
    assert "in order to" in phrases
    assert "please note that" in phrases
    assert code == 1


def test_passive_rule_10():
    code, rep = findings("--text", "Your payment could not be processed.")
    assert any(f["rule"] == "10" for f in rep["findings"])


def test_short_result_passive_is_allowed():
    code, rep = findings("--text", "File deleted")
    assert not any(f["rule"] == "10" for f in rep["findings"])


def test_negative_instruction_rule_11():
    code, rep = findings("--text", "Password is not long enough.")
    assert any(f["rule"] == "11" for f in rep["findings"])


def test_vague_rule_12():
    code, rep = findings("--text", "Something went wrong. Are you sure?")
    hits = [f for f in rep["findings"] if f["rule"] == "12"]
    assert len(hits) == 2


def test_breezy_and_overstated_style():
    code, rep = findings("--text", "Oops! Something went wrong 🙈 Awesome!!")
    rules = {f["rule"] for f in rep["findings"]}
    assert "V.9" in rules
    assert "V.7" in rules


def test_qualifier_v8():
    code, rep = findings("--text", "This may take a little while.")
    assert any(f["rule"] == "V.8" for f in rep["findings"])


def test_lexicon_hit_cites_entry():
    code, rep = findings("--text", "Utilize the settings page prior to syncing.")
    m = {f["match"].lower(): f for f in rep["findings"]}
    assert "utilize" in m and m["utilize"]["instead"] == "use"
    assert "prior to" in m and m["prior to"]["instead"] == "before"


def test_json_strings_file_terminology_collisions(tmp_path):
    f = tmp_path / "en.json"
    f.write_text(json.dumps({
        "auth.cta": "Log in",
        "auth.title": "Sign in to continue",
        "nav.login": "Login",
        "files.remove": "Remove file",
        "files.delete": "Delete file",
    }))
    code, rep = findings(str(f))
    coll = [f for f in rep["findings"] if f["rule"] == "4th.12"]
    groups = {c["group"] for c in coll}
    assert "sign in" in groups and "delete" in groups
    assert code == 1


def test_apple_strings_and_android_xml(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('"a" = "In order to continue";\n"b" = "Saved";\n')
    x = tmp_path / "strings.xml"
    x.write_text('<resources><string name="a">Please note that it failed</string></resources>')
    _, rep1 = findings(str(s))
    _, rep2 = findings(str(x))
    assert rep1["stats"]["strings"] == 2 and rep1["findings"][0]["key"] == "a"
    assert rep2["stats"]["strings"] == 1 and rep2["findings"][0]["key"] == "a"


def test_case_inconsistency_across_file(tmp_path):
    f = tmp_path / "en.json"
    f.write_text(json.dumps({
        "a.title": "Save Changes",
        "b.title": "Save Your Work Now",
        "c.title": "Save Draft",
        "d.title": "Discard draft",
    }))
    _, rep = findings(str(f))
    assert any(f["rule"] == "V.10" for f in rep["findings"])


def test_stats_words_per_string():
    _, rep = findings("--text", "Delete 3 photos? This cannot be undone.")
    assert rep["stats"]["words"] == 7
    assert rep["stats"]["strings"] == 1


def test_stdin():
    code, out, err = run("--json", stdin="Simply tap to easily begin.")
    rep = json.loads(out)
    assert {f["match"].lower() for f in rep["findings"]} >= {"simply", "easily"}


def test_exit_code_zero_with_only_notes():
    code, rep = findings("--text", "No internet connection")
    assert all(f["severity"] == "note" for f in rep["findings"])
    assert code == 0


def test_po_plural_forms_are_checked(tmp_path):
    f = tmp_path / "en.po"
    f.write_text('msgid "photo"\nmsgid_plural "photos"\nmsgstr[0] "Oops"\nmsgstr[1] "Simply continue"\n\nmsgid "Saved"\nmsgstr ""\n')
    code, rep = findings(str(f))
    assert rep["stats"]["strings"] == 3
    assert {f["match"].lower() for f in rep["findings"]} >= {"oops", "simply"}
    assert code == 1


def test_android_string_array_and_escapes(tmp_path):
    x = tmp_path / "strings.xml"
    x.write_text('<resources><string name="a">We\\\'re thrilled</string>'
                 '<string-array name="arr"><item>Oops</item><item>Saved</item></string-array></resources>')
    code, rep = findings(str(x))
    assert rep["stats"]["strings"] == 3
    keys = {f["key"] for f in rep["findings"]}
    assert "arr[0]" in keys and "a" in keys


def test_apple_strings_comments_and_unicode_escapes(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('/* "retired" = "Oops"; */\n// "also" = "Oops";\n"active" = "\\U004Fops";\n"ok" = "Saved";\n')
    code, rep = findings(str(s))
    assert rep["stats"]["strings"] == 2
    assert [f["key"] for f in rep["findings"]] == ["active"]
    assert rep["findings"][0]["match"].lower() == "oops"


def test_apple_strings_utf16(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_bytes('"a" = "Oops";\n'.encode("utf-16"))
    code, rep = findings(str(s))
    assert rep["stats"]["strings"] == 1 and code == 1


def test_exclamation_marks_without_word_boundary():
    _, rep = findings("--text", "Done!!")
    assert any(f["rule"] == "V.7" and f["severity"] == "warn" for f in rep["findings"])
    _, rep = findings("--text", "Done!")
    assert any(f["rule"] == "V.7" and f["severity"] == "note" for f in rep["findings"])


def test_pretty_as_qualifier():
    _, rep = findings("--text", "This is pretty fast.")
    assert any(f["rule"] == "V.8" and f["match"].lower().startswith("pretty") for f in rep["findings"])


def test_export_download_collision(tmp_path):
    f = tmp_path / "en.json"
    f.write_text(json.dumps({"a": "Export", "b": "Download your data"}))
    _, rep = findings(str(f))
    assert any(f["rule"] == "4th.12" and f["group"] == "download" for f in rep["findings"])


def test_relative_plus_be_is_noted():
    _, rep = findings("--text", "The file which is selected will be sent.")
    assert any(f["rule"] == "13" and f["match"].lower() == "which is" for f in rep["findings"])


def test_malformed_input_exits_two(tmp_path):
    f = tmp_path / "en.json"
    f.write_text("{not json")
    code, out, err = run("--json", str(f))
    assert code == 2
    assert "error" in json.loads(out)
    code, out, err = run(str(f))
    assert code == 2 and err.strip() != ""


def test_runs_on_python_311():
    p = subprocess.run(["uv", "run", "--python", "3.11", "--no-project", str(SCRIPT), "--text", "Saved"],
                       capture_output=True, text=True)
    assert p.returncode == 0, p.stderr


def test_po_adjacent_entries_and_context_and_octal(tmp_path):
    f = tmp_path / "en.po"
    f.write_text('msgid ""\nmsgstr "Content-Type: text/plain\\n"\nmsgid "a"\nmsgstr "Oops"\nmsgid "b"\nmsgstr "Saved"\n'
                 'msgctxt "menu"\nmsgid "Open"\nmsgstr "\\117pen simply"\nmsgctxt "dialog"\nmsgid "Open"\nmsgstr "Open"\n')
    code, rep = findings(str(f))
    keys = [k for k in {f["key"] for f in rep["findings"]}]
    assert rep["stats"]["strings"] == 4
    assert any(f["key"] == "a" and f["match"].lower() == "oops" for f in rep["findings"])
    assert any(f["key"] == "Open (menu)" and f["match"].lower() == "simply" for f in rep["findings"])


def test_po_unterminated_quote_exits_two(tmp_path):
    f = tmp_path / "en.po"
    f.write_text('msgid "Saved"\nmsgstr "Oops\n')
    code, out, err = run(str(f))
    assert code == 2


def test_strings_comment_inside_value_and_trailing_comment(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('"a" = "Show /* Oops */";\n"b" = "Saved"; // "retired" = "Oops";\n"c" = "Done";\n')
    _, rep = findings(str(s))
    assert rep["stats"]["strings"] == 3
    assert [f["key"] for f in rep["findings"] if f["match"].lower() == "oops"] == ["a"]


def test_strings_missing_semicolon_exits_two(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('"a" = "Saved"\n"b" = "Done";\n')
    code, out, err = run(str(s))
    assert code == 2 and "a" in err


def test_strings_surrogate_pair_emoji(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('"a" = "Oops \\UD83D\\UDE22";\n')
    _, rep = findings(str(s))
    assert any(f["rule"] == "V.9" and f["match"] == "😢" for f in rep["findings"])


def test_android_whitespace_collapse_and_quoted(tmp_path):
    x = tmp_path / "strings.xml"
    x.write_text('<resources>\n<string name="a">In order\n        to continue</string>\n<string name="b">"  Cancel  "</string>\n</resources>')
    _, rep = findings(str(x))
    assert any(f["key"] == "a" and f["match"].lower() == "in order to" for f in rep["findings"])
    assert any(f["key"] == "b" and f["rule"] == "15" for f in rep["findings"])


def test_passive_heuristic_ignores_adjectives():
    for t in ["The indicator is red", "The light is green", "Your child is seven", "The door is open"]:
        _, rep = findings("--text", t)
        assert not any(f["rule"] == "10" for f in rep["findings"]), t
    _, rep = findings("--text", "The request was rejected by the server.")
    assert any(f["rule"] == "10" for f in rep["findings"])


def test_po_escaped_quote_missing_msgstr_duplicate_and_utf8_octal(tmp_path):
    f = tmp_path / "en.po"
    f.write_text('msgid "a"\nmsgstr "Saved\\"\n')
    assert run(str(f))[0] == 2
    f.write_text('msgid "a"\nmsgid "b"\nmsgstr "Saved"\n')
    assert run(str(f))[0] == 2
    f.write_text('msgid "a"\nmsgstr "x"\nmsgstr "y"\n')
    assert run(str(f))[0] == 2
    f.write_text('msgid "a"\nmsgstr "Oops \\360\\237\\230\\242"\n')
    _, rep = findings(str(f))
    assert any(f["rule"] == "V.9" and f["match"] == "😢" for f in rep["findings"])


def test_apple_octal_and_short_unicode_escapes(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('"a" = "\\117ops";\n"b" = "\\U4Fops";\n')
    _, rep = findings(str(s))
    assert sorted(f["key"] for f in rep["findings"] if f["match"].lower() == "oops") == ["a", "b"]


def test_android_inline_quotes_preserve_whitespace(tmp_path):
    x = tmp_path / "strings.xml"
    x.write_text('<resources><string name="a">In "order" to\n   continue</string><string name="b">Tap "  Save  " now</string></resources>')
    _, rep = findings(str(x))
    texts = {f["key"]: f["text"] for f in rep["findings"]}
    assert texts["a"] == "In order to continue"
    assert any(f["key"] == "a" and f["match"].lower() == "in order to" for f in rep["findings"])
    assert "b" not in texts or texts["b"] == "Tap   Save   now"


def test_missing_file_json_error():
    code, out, err = run("--json", "/nonexistent/en.json")
    assert code == 2 and "error" in json.loads(out)


def test_po_continuation_lines_decode_together_and_c_escapes(tmp_path):
    f = tmp_path / "en.po"
    f.write_text('msgid "a"\nmsgstr "Oops \\360\\237"\n"\\230\\242"\nmsgid "b"\nmsgstr "\\x04fops\\vnow"\n')
    _, rep = findings(str(f))
    assert any(f["key"] == "a" and f["match"] == "😢" for f in rep["findings"])
    assert any(f["key"] == "b" and f["match"].lower() == "oops" for f in rep["findings"])
    f.write_text('msgid "a"\nmsgstr "Oops"\nmsgstr[0] "Saved"\n')
    assert run(str(f))[0] == 2


def test_apple_and_android_decoders_differ(tmp_path):
    s = tmp_path / "Localizable.strings"
    s.write_text('"a" = "\\u004Fops";\n')
    _, rep = findings(str(s))
    assert not any(f["match"].lower() == "oops" for f in rep["findings"])
    x = tmp_path / "strings.xml"
    x.write_text('<resources><string name="a">\\U004Fops</string><string name="b">\\u004Fops</string></resources>')
    _, rep = findings(str(x))
    assert [f["key"] for f in rep["findings"] if f["match"].lower() == "oops"] == ["b"]


def test_android_quote_after_escaped_backslash(tmp_path):
    x = tmp_path / "strings.xml"
    x.write_text('<resources><string name="a">"C:\\\\" In order\n   to continue</string></resources>')
    _, rep = findings(str(x))
    assert any(f["key"] == "a" and f["match"].lower() == "in order to" for f in rep["findings"])


def test_lone_surrogate_in_json_and_single_string_file_checks(tmp_path):
    f = tmp_path / "en.json"
    f.write_text('{"a": "Oops\\ud800"}')
    code, out, err = run("--json", str(f))
    assert code == 1 and json.loads(out)["findings"]
    f.write_text('{"settings": "Settings & Preferences"}')
    _, rep = findings(str(f))
    assert any(f["rule"] == "4th.12" for f in rep["findings"])


def test_po_fragments_do_not_bleed_and_duplicate_msgid(tmp_path):
    f = tmp_path / "en.po"
    f.write_text('msgid "a"\nmsgstr "Help:\\x0a"\n"Click here"\n')
    _, rep = findings(str(f))
    assert any(f["key"] == "a" and f["match"].lower() == "click here" for f in rep["findings"])
    f.write_text('msgid "Save"\nmsgstr "Save"\nmsgid "Save"\nmsgstr "Store"\n')
    assert run(str(f))[0] == 2
    f.write_text('msgctxt "a"\nmsgid "Save"\nmsgstr "Save"\nmsgctxt "b"\nmsgid "Save"\nmsgstr "Store"\n')
    assert run(str(f))[0] == 0


def test_curly_apostrophes_match_contractions():
    _, rep = findings("--text", "Don\u2019t continue. We\u2019re thrilled.")
    rules = {f["rule"] for f in rep["findings"]}
    assert "11" in rules and "V.1" in rules
    assert all("\u2019" in f["text"] for f in rep["findings"])
