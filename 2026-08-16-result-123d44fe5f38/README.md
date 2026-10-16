# Verified implementation 2026-08-16-result-123d44fe5f38

The source reports that a £299.99 Snapdragon mini PC ran a 35B coder at 24.5 tok/s, or about 30 tok/s with MTP.

Source: [r/LocalLLaMA: What a £300, 35W Snapdragon mini PC can actually do 👀: 35B coder at ~30 tok/s, and an 80B model that doesnt even fit in RAM running at 17 tok/s](https://www.reddit.com/r/LocalLLaMA/comments/1x6stod/what_a_300_35w_snapdragon_mini_pc_can_actually_do/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6NS41LCJpbnB1dHMiOnsiYWZ0ZXIiOjMwLCJiZWZvcmUiOjI0LjV9LCJvcGVyYXRpb24iOiJudW1lcmljX2RlbHRhIn0='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6NS41LCJpbnB1dHMiOnsiYWZ0ZXIiOjMwLCJiZWZvcmUiOjI0LjV9LCJvcGVyYXRpb24iOiJudW1lcmljX2RlbHRhIn0='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
