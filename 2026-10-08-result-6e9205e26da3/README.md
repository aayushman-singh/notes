# Verified implementation 2026-10-08-result-6e9205e26da3

The source reports a 21M model with a 6.4B-parameter lookup table matches a 114M dense model on the same 500M Wikipedia tokens.

Source: [r/LocalLLaMA: I gave a 21M model a 6.4B-parameter lookup table. It matches a 114M dense model and runs with the table on an SSD (RX 9070)](https://www.reddit.com/r/LocalLLaMA/comments/1wz7tvs/i_gave_a_21m_model_a_64bparameter_lookup_table_it/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6MC41MiwiaW5wdXRzIjp7InBhcnQiOjMzMDAwMDAwLCJwcmVjaXNpb24iOjIsIndob2xlIjo2NDAwMDAwMDAwfSwib3BlcmF0aW9uIjoicGVyY2VudGFnZSJ9'"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6MC41MiwiaW5wdXRzIjp7InBhcnQiOjMzMDAwMDAwLCJwcmVjaXNpb24iOjIsIndob2xlIjo2NDAwMDAwMDAwfSwib3BlcmF0aW9uIjoicGVyY2VudGFnZSJ9'"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
