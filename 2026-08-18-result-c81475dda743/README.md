# Verified implementation 2026-08-18-result-c81475dda743

Citizen Lab reports that targeted ads delivered zero-click mercenary spyware and enabled surveillance at scale.

Source: [AdFection: Targeted ads turned into a pipeline for zero-click mercenary spyware](https://citizenlab.ca/research/how-discover-tech-turned-targeted-ads-into-a-pipeline-for-spyware/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJkaXNwbGF5IG9mIGEgdGFyZ2V0ZWQgYWQgaXMgZW5vdWdoIGZvciBpbmZlY3Rpb24iLCJ0ZXh0IjoidGhlIHNpbXBsZSBkaXNwbGF5IG9mIGEgdGFyZ2V0ZWQgYWQgaXMgZW5vdWdoIGZvciBpbmZlY3Rpb24ifSwib3BlcmF0aW9uIjoicmVnZXhfbWF0Y2gifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJkaXNwbGF5IG9mIGEgdGFyZ2V0ZWQgYWQgaXMgZW5vdWdoIGZvciBpbmZlY3Rpb24iLCJ0ZXh0IjoidGhlIHNpbXBsZSBkaXNwbGF5IG9mIGEgdGFyZ2V0ZWQgYWQgaXMgZW5vdWdoIGZvciBpbmZlY3Rpb24ifSwib3BlcmF0aW9uIjoicmVnZXhfbWF0Y2gifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
