import json
import sys

review = json.load(open("review.json"))

if not review["approved"]:
    print("Fix rejected")
    sys.exit(1)

diagnosis = json.load(open("diagnosis.json"))

target_file = diagnosis["target_file"]

replacement_content = diagnosis["replacement_content"]

if not target_file:
    raise SystemExit("No file provided")

with open(target_file, "w") as f:
    f.write(replacement_content)

print(f"Updated {target_file}")
