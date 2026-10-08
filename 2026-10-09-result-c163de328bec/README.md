# Verified implementation 2026-10-09-result-c163de328bec

The source reports Loop 4 Clean PSNR is 42.480 and Loop 1 Clean PSNR is 41.885 at the 24k checkpoint.

Source: [r/StableDiffusion: I adapted the Looped-DiT concept into a tiny anime upscaler (Baikal LoopSR x2) [ComfyUI / Weights]](https://www.reddit.com/r/StableDiffusion/comments/1x0h9ye/i_adapted_the_loopeddit_concept_into_a_tiny_anime/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6MC41OTQ5OTk5OTk5OTk5OTg5LCJpbnB1dHMiOnsiYWZ0ZXIiOjQyLjQ4LCJiZWZvcmUiOjQxLjg4NX0sIm9wZXJhdGlvbiI6Im51bWVyaWNfZGVsdGEifQ=='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6MC41OTQ5OTk5OTk5OTk5OTg5LCJpbnB1dHMiOnsiYWZ0ZXIiOjQyLjQ4LCJiZWZvcmUiOjQxLjg4NX0sIm9wZXJhdGlvbiI6Im51bWVyaWNfZGVsdGEifQ=='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
