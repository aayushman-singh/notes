# Verified implementation 2026-10-28-result-867db54c5ecf

The source reports that macOS developer tools still trusted compromised eMudhra certificates on October 28 after Apple was notified October 17.

Source: [Ten days later, Git on macOS still trusts the compromised eMudhra certificates](https://emudhra.we-have-a-problem.com/apple.html)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6MTEsImlucHV0cyI6eyJhZnRlciI6MjgsImJlZm9yZSI6MTd9LCJvcGVyYXRpb24iOiJudW1lcmljX2RlbHRhIn0='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6MTEsImlucHV0cyI6eyJhZnRlciI6MjgsImJlZm9yZSI6MTd9LCJvcGVyYXRpb24iOiJudW1lcmljX2RlbHRhIn0='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
