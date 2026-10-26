# Verified implementation 2026-10-26-result-14ee692acbf1

The source reports that Samsung runs an INT8 TensorFlow Lite AlexNet model on 960×540 images every few seconds to identify games.

Source: [Samsung running a TensorFlow lite model on 960x540 image to track you](https://twitter.com/mike64_t/status/2114150399406202896)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJeYWxleFxcLnRmbGl0ZSQiLCJ0ZXh0IjoiYWxleC50ZmxpdGUifSwib3BlcmF0aW9uIjoicmVnZXhfbWF0Y2gifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJeYWxleFxcLnRmbGl0ZSQiLCJ0ZXh0IjoiYWxleC50ZmxpdGUifSwib3BlcmF0aW9uIjoicmVnZXhfbWF0Y2gifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
