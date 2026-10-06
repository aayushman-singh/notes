CASE_B64 = 'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiJlbnZpcm9ubWVudCBpcyBmdWxseSBwaG90b2dyYXBoaWM7IG9ubHkgdGhlIGNoYXJhY3RlciBoYXMgYW5pbWUgZmVhdHVyZXMiLCJ0ZXh0IjoiQSBwaG90b3JlYWxpc3RpYyB0cm9waWNhbCB0ZW5uaXMgcGhvdG9ncmFwaCB3aXRoIGEgc2VtaS1yZWFsaXN0aWMgYW5pbWUgd29tYW4gbmF0dXJhbGx5IGludGVncmF0ZWQgaW50byB0aGUgc2NlbmUuIFRoZSBlbnZpcm9ubWVudCBpcyBmdWxseSBwaG90b2dyYXBoaWM7IG9ubHkgdGhlIGNoYXJhY3RlciBoYXMgYW5pbWUgZmVhdHVyZXMuIn0sIm9wZXJhdGlvbiI6InJlZ2V4X21hdGNoIn0='
import base64
import json
import re

case = json.loads(base64.b64decode(CASE_B64).decode("utf-8"))
operation = case["operation"]
inputs = case["inputs"]
if operation == "json_value":
    observed = inputs["document"]
    for step in inputs["path"]:
        observed = observed[step]
elif operation == "regex_match":
    observed = re.search(inputs["pattern"], inputs["text"]) is not None
elif operation == "stable_sort":
    observed = sorted(inputs["values"])
elif operation == "boundary_compare":
    observed = inputs["minimum"] <= inputs["value"] <= inputs["maximum"]
elif operation == "numeric_delta":
    observed = inputs["after"] - inputs["before"]
elif operation == "percentage":
    observed = round(inputs["part"] / inputs["whole"] * 100, inputs["precision"])
else:
    raise RuntimeError("unsupported source check")
if observed != case["expected"]:
    raise RuntimeError("observed result differs from expected result")
print(json.dumps({"observed": observed}, sort_keys=True, separators=(",", ":")))
