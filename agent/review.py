import json
from mistral_client import client

proposal = open("diagnosis.json").read()

prompt = f"""
You are a staff engineer.

Review the fix proposal.

Reject:
- hallucinations
- unsupported fixes
- risky changes

Return ONLY JSON:

{{
  "approved": true,
  "reason": ""
}}

Proposal:

{proposal}
"""

response = client.chat.complete(
    model="mistral-medium-latest",
    messages=[
        {
            "role": "user",
            "content": prompt
        }
    ]
)

with open("review.json", "w") as f:
    f.write(response.choices[0].message.content)
