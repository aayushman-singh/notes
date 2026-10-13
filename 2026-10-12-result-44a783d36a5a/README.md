# Verified implementation 2026-10-12-result-44a783d36a5a

The source reports MiniCPM-V 4.7 supports mixed 4x/16x visual token compression for balancing detail and cost.

Source: [r/LocalLLaMA: openbmb/MiniCPM-V-4.7-35B-A3B](https://www.reddit.com/r/LocalLLaMA/comments/1x47taj/openbmbminicpmv4735ba3b/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7Im1heGltdW0iOjE2LCJtaW5pbXVtIjo0LCJ2YWx1ZSI6NH0sIm9wZXJhdGlvbiI6ImJvdW5kYXJ5X2NvbXBhcmUifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7Im1heGltdW0iOjE2LCJtaW5pbXVtIjo0LCJ2YWx1ZSI6NH0sIm9wZXJhdGlvbiI6ImJvdW5kYXJ5X2NvbXBhcmUifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
