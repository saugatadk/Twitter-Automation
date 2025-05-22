from openai import OpenAI
import os

client = OpenAI(
  base_url="https://openrouter.ai/api/v1",
  api_key=os.getenv("OPENAI_API_KEY"),
)

completion = client.chat.completions.create(
#   extra_headers={
#     "HTTP-Referer": "<YOUR_SITE_URL>", # Optional. Site URL for rankings on openrouter.ai.
#     "X-Title": "<YOUR_SITE_NAME>", # Optional. Site title for rankings on openrouter.ai.
#   },
  extra_body={},
  model="google/gemma-3n-e4b-it:free",
  messages=[
    {
      "role": "user",
      "content": "Write a single-sentence viral tweet for startup founders with a curiosity-driven hook, clear insight, and no hashtags or mentions and end with ‘#business #startup #Tips’ But remember to change the answer everytime this prompt is prompted"
    }
  ]
)