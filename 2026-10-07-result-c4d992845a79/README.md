# Verified implementation 2026-10-07-result-c4d992845a79

The source reports two Civitai LoRAs, one Pastebin workflow, and three prompts for a GPT semi-realistic 3D anime look.

Source: [r/StableDiffusion: How to get the GPT semi-realistic 3D anime look locally (LoRAs + workflow + prompts)](https://www.reddit.com/r/StableDiffusion/comments/1wy2c6t/how_to_get_the_gpt_semirealistic_3d_anime_look/)

Implementation focus: a verified public result.

Verification command: `python -c 'from pathlib import Path
CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJlbnZpcm9ubWVudCBpcyBmdWxseSBwaG90b2dyYXBoaWM7IG9ubHkgdGhlIGNoYXJhY3RlciBoYXMgYW5pbWUgZmVhdHVyZXMiLCJ0ZXh0IjoiQSBwaG90b3JlYWxpc3RpYyB0cm9waWNhbCB0ZW5uaXMgcGhvdG9ncmFwaCB3aXRoIGEgc2VtaS1yZWFsaXN0aWMgYW5pbWUgd29tYW4gbmF0dXJhbGx5IGludGVncmF0ZWQgaW50byB0aGUgc2NlbmUuIFRoZSBlbnZpcm9ubWVudCBpcyBmdWxseSBwaG90b2dyYXBoaWM7IG9ubHkgdGhlIGNoYXJhY3RlciBoYXMgYW5pbWUgZmVhdHVyZXMuIn0sIm9wZXJhdGlvbiI6InJlZ2V4X21hdGNoIn0='"'"'
program = "CASE_B64 = '"'"'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJlbnZpcm9ubWVudCBpcyBmdWxseSBwaG90b2dyYXBoaWM7IG9ubHkgdGhlIGNoYXJhY3RlciBoYXMgYW5pbWUgZmVhdHVyZXMiLCJ0ZXh0IjoiQSBwaG90b3JlYWxpc3RpYyB0cm9waWNhbCB0ZW5uaXMgcGhvdG9ncmFwaCB3aXRoIGEgc2VtaS1yZWFsaXN0aWMgYW5pbWUgd29tYW4gbmF0dXJhbGx5IGludGVncmF0ZWQgaW50byB0aGUgc2NlbmUuIFRoZSBlbnZpcm9ubWVudCBpcyBmdWxseSBwaG90b2dyYXBoaWM7IG9ubHkgdGhlIGNoYXJhY3RlciBoYXMgYW5pbWUgZmVhdHVyZXMuIn0sIm9wZXJhdGlvbiI6InJlZ2V4X21hdGNoIn0='"'"'\nimport base64\nimport json\nimport re\n\ncase = json.loads(base64.b64decode(CASE_B64).decode(\"utf-8\"))\noperation = case[\"operation\"]\ninputs = case[\"inputs\"]\nif operation == \"json_value\":\n    observed = inputs[\"document\"]\n    for step in inputs[\"path\"]:\n        observed = observed[step]\nelif operation == \"regex_match\":\n    observed = re.search(inputs[\"pattern\"], inputs[\"text\"]) is not None\nelif operation == \"stable_sort\":\n    observed = sorted(inputs[\"values\"])\nelif operation == \"boundary_compare\":\n    observed = inputs[\"minimum\"] <= inputs[\"value\"] <= inputs[\"maximum\"]\nelif operation == \"numeric_delta\":\n    observed = inputs[\"after\"] - inputs[\"before\"]\nelif operation == \"percentage\":\n    observed = round(inputs[\"part\"] / inputs[\"whole\"] * 100, inputs[\"precision\"])\nelse:\n    raise RuntimeError(\"unsupported source check\")\nif observed != case[\"expected\"]:\n    raise RuntimeError(\"observed result differs from expected result\")\nprint(json.dumps({\"observed\": observed}, sort_keys=True, separators=(\",\", \":\")))\n"
Path('"'"'/record/source_check.py'"'"').write_text(program, encoding='"'"'utf-8'"'"')
scope = {'"'"'CASE_B64'"'"': CASE_B64}
exec(compile(program, '"'"'source_check.py'"'"', '"'"'exec'"'"'), scope)
'`
