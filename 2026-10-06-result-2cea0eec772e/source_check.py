CASE_B64 = 'eyJleHBlY3RlZCI6dHJ1ZSwiaW5wdXRzIjp7InBhdHRlcm4iOiIxNTAgbGFuZ3VhZ2VzIiwidGV4dCI6IkluZGV4LVRyYW5zbGF0ZSBpcyBhIGZhbWlseSBvZiBtdWx0aWxpbmd1YWwgdHJhbnNsYXRpb24gbW9kZWxzIGJ1aWx0IG9uIFF3ZW4zLjUuIFRoZSB0ZXh0IG1vZGVscyBjb3ZlciAxNTAgbGFuZ3VhZ2VzIGFuZCBmb2xsb3cgdHJhbnNsYXRpb24gaW5zdHJ1Y3Rpb25zIHN1Y2ggYXMgdGVybWlub2xvZ3ksIGZvcm1hdHRpbmcsIGFuZCBjb250ZW50LXByZXNlcnZhdGlvbiByZXF1aXJlbWVudHMuIn0sIm9wZXJhdGlvbiI6InJlZ2V4X21hdGNoIn0='
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
