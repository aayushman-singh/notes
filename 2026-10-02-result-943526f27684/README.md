# Verified implementation 2026-10-02-result-943526f27684

The source reports Maple raised official Canadian source citation from 6.0% to 62.9% on 600 held-out questions with search.

Source: [r/LocalLLaMA: Two open-weights releases: Victoria (Qwen3.8-Flash-Next with 44% of experts cut, 70% Terminal-Bench 2.1, GGUF included) and Maple (a Canada-first fine-tune)](https://www.reddit.com/r/LocalLLaMA/comments/1wujph3/two_openweights_releases_victoria_qwen38flashnext/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6NTYuOSwiaW5wdXRzIjp7ImFmdGVyIjo2Mi45LCJiZWZvcmUiOjYuMH0sIm9wZXJhdGlvbiI6Im51bWVyaWNfZGVsdGEifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6NTYuOSwiaW5wdXRzIjp7ImFmdGVyIjo2Mi45LCJiZWZvcmUiOjYuMH0sIm9wZXJhdGlvbiI6Im51bWVyaWNfZGVsdGEifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
