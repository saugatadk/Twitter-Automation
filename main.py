import tweepy
from dotenv import load_dotenv
from openai import OpenAI
import os
import re

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
  model="google/gemma-3n-e4b-it:free",
  messages=[
    {
      "role": "user",
      "content": "Write a single-sentence viral tweet for startup founders with a curiosity-driven hook, clear insight, and no hashtags or mentions and end with ‘Follow me for more founder tips.’"
    }
  ]
)

tweet_text = completion.choices[0].message.content.strip()

# Sanitize the tweet:
def sanitize_tweet(text):
    text = text.replace('\n\n', '\n')  # remove double line breaks
    text = re.sub(r'http\S+', '', text)  # remove links
    text = re.sub(r'@\w+', '', text)  # remove mentions
    text = re.sub(r'#\w+', '', text)  # remove hashtags
    text = text.encode('ascii', errors='ignore').decode()  # remove non-ASCII characters like unusual emojis
    return text.strip()

tweet_text = sanitize_tweet(tweet_text)

# Log tweet before sending
print("Sanitized Tweet:\n", tweet_text)


# Post to Twitter
client = get_client()
# create_tweet(client, tweet_text)