# Verified implementation 2026-08-19-result-6fc00e5eba09

The source reports that Libreboot 26.10 imports all 233 MrChromebox-supported Chromebook boards and defaults to EDK2 on most 64-bit hardware.

Source: [Libreboot 26.10 "Ominous Olive" released with UEFI, Chromebook support](https://libreboot.org/news/libreboot2610.html)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6MTAwLjAsImlucHV0cyI6eyJwYXJ0IjoyMzMsInByZWNpc2lvbiI6MSwid2hvbGUiOjIzM30sIm9wZXJhdGlvbiI6InBlcmNlbnRhZ2UifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6MTAwLjAsImlucHV0cyI6eyJwYXJ0IjoyMzMsInByZWNpc2lvbiI6MSwid2hvbGUiOjIzM30sIm9wZXJhdGlvbiI6InBlcmNlbnRhZ2UifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
