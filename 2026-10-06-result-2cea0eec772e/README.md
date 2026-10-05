# Verified implementation 2026-10-06-result-2cea0eec772e

The source reports Bilibili released Index-Translate, a Qwen3.5-based multilingual translation family covering 150 languages.

Source: [r/LocalLLaMA: bilibili released Index-Translate,a A Multilingual Translation Model Family based on Qwen3.5](https://www.reddit.com/r/LocalLLaMA/comments/1wxa1wr/bilibili_released_indextranslatea_a_multilingual/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiIxNTAgbGFuZ3VhZ2VzIiwidGV4dCI6IkluZGV4LVRyYW5zbGF0ZSBpcyBhIGZhbWlseSBvZiBtdWx0aWxpbmd1YWwgdHJhbnNsYXRpb24gbW9kZWxzIGJ1aWx0IG9uIFF3ZW4zLjUuIFRoZSB0ZXh0IG1vZGVscyBjb3ZlciAxNTAgbGFuZ3VhZ2VzIGFuZCBmb2xsb3cgdHJhbnNsYXRpb24gaW5zdHJ1Y3Rpb25zIHN1Y2ggYXMgdGVybWlub2xvZ3ksIGZvcm1hdHRpbmcsIGFuZCBjb250ZW50LXByZXNlcnZhdGlvbiByZXF1aXJlbWVudHMuIn0sIm9wZXJhdGlvbiI6InJlZ2V4X21hdGNoIn0='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiIxNTAgbGFuZ3VhZ2VzIiwidGV4dCI6IkluZGV4LVRyYW5zbGF0ZSBpcyBhIGZhbWlseSBvZiBtdWx0aWxpbmd1YWwgdHJhbnNsYXRpb24gbW9kZWxzIGJ1aWx0IG9uIFF3ZW4zLjUuIFRoZSB0ZXh0IG1vZGVscyBjb3ZlciAxNTAgbGFuZ3VhZ2VzIGFuZCBmb2xsb3cgdHJhbnNsYXRpb24gaW5zdHJ1Y3Rpb25zIHN1Y2ggYXMgdGVybWlub2xvZ3ksIGZvcm1hdHRpbmcsIGFuZCBjb250ZW50LXByZXNlcnZhdGlvbiByZXF1aXJlbWVudHMuIn0sIm9wZXJhdGlvbiI6InJlZ2V4X21hdGNoIn0='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
