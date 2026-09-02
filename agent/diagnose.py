import json
from mistral_client import client

with open("artifacts/failure.log") as f:
    logs = f.read()

logs = logs[-15000:]

prompt = f"""
You are a GitHub Actions debugging expert.

Analyze these logs.

Return ONLY valid JSON.

Schema:

{{
  "root_cause": "",
  "proposed_fix": "",
  "target_file": "",
  "replacement_content": ""
}}

Logs:

{logs}
"""

response = client.chat.complete(
    model="mistral-medium-latest",
    messages=[
        {"role": "user", "content": prompt}
    ]
)

result = response.choices[0].message.content

with open("diagnosis.json", "w") as f:
    f.write(result)
