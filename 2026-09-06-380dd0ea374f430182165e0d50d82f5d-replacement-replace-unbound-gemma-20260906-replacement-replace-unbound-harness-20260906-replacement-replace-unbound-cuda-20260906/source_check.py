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
else:
    raise RuntimeError("unsupported source check")
if observed != case["expected"]:
    raise RuntimeError("observed result differs from expected result")
print(json.dumps({"observed": observed}, sort_keys=True, separators=(",", ":")))
