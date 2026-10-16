# Verified implementation 2026-08-16-result-bf1ef07abbc3

The source reports that disabling two SFE/PPE sysfs features stopped TCP payload corruption on a TP-Link EAP770 v1.

Source: [Wanted to download an ISO, ended up writing a kernel exploit](https://blog.dfb.sh/blog/eap770-root-for-two-zeros/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6OTYxMzAwOTI0LCJpbnB1dHMiOnsiYWZ0ZXIiOjM2ODM3Nzg1NjAsImJlZm9yZSI6MjcyMjQ3NzYzNn0sIm9wZXJhdGlvbiI6Im51bWVyaWNfZGVsdGEifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6OTYxMzAwOTI0LCJpbnB1dHMiOnsiYWZ0ZXIiOjM2ODM3Nzg1NjAsImJlZm9yZSI6MjcyMjQ3NzYzNn0sIm9wZXJhdGlvbiI6Im51bWVyaWNfZGVsdGEifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
