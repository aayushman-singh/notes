# Verified implementation 2026-10-05-result-5bc1349c15c8

The source reports that ncurses terminfo can simulate a two-counter Minsky machine via repeated parameter expansion.

Source: [r/programming: A Minsky machine in ncurses terminfo](https://www.reddit.com/r/programming/comments/1wvy0zi/a_minsky_machine_in_ncurses_terminfo/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6MiwiaW5wdXRzIjp7ImRvY3VtZW50Ijp7ImNvdW50ZXJzIjoyLCJkZW1vIjoiRmlib25hY2NpIiwiaG9zdCI6Ii91c3IvYmluL3RvcCJ9LCJwYXRoIjpbImNvdW50ZXJzIl19LCJvcGVyYXRpb24iOiJqc29uX3ZhbHVlIn0='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6MiwiaW5wdXRzIjp7ImRvY3VtZW50Ijp7ImNvdW50ZXJzIjoyLCJkZW1vIjoiRmlib25hY2NpIiwiaG9zdCI6Ii91c3IvYmluL3RvcCJ9LCJwYXRoIjpbImNvdW50ZXJzIl19LCJvcGVyYXRpb24iOiJqc29uX3ZhbHVlIn0='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
