import tweepy
from dotenv import load_dotenv
from openai import OpenAI
import os

def get_client():
    load_dotenv()
    
    client = tweepy.Client(
        consumer_key=os.getenv("CONSUMER_KEY"),
        consumer_secret=os.getenv("CONSUMER_SECRET"),
        access_token=os.getenv("ACCESS_TOKEN"),
        access_token_secret=os.getenv("ACCESS_TOKEN_SECRET"),
    )
    
    return client

def create_tweet(client, tweet_text):
    client.create_tweet(text=tweet_text)
    

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
  model="meta-llama/llama-3.3-8b-instruct:free",
  messages=[
    {
      "role": "user",
      "content": "Write a tweet thread for Twitter aimed at startup founders within 200 words. The goal is to go viral. Start with a curiosity-driven hook like Most startups die for the same 3 reasons — but no one talks about them 🧵 but also make sure to change it to something even better from time to time. Make the rest of the tweets concise and valuable, with insights from real founder experiences. Use emojis occasionally and clear formatting.End with a CTA like ‘Follow me for more founder tips’.DONOT INCLUDE ABOUT yourhandle or any that kind of hastags. Output the tweet only, without the starting lines like here is a tweet or anything like that. Make sure the numbers are. The formatting should be in simply understandable english without any typos like markdown.Keep the numbering for reasons 1. 2. 3. type only and display only 3 points. Donot make unnecessary paragraphs"
    }
  ]
)
print(completion.choices[0].message.content)
client = get_client()
create_tweet(client, completion.choices[0].message.content)
