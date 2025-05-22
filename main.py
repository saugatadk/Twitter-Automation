from twitter import get_client, create_tweet
from gemma import client, completion
import re

# Sanitize the tweet:
def sanitize_tweet(text):
    text = text.replace('\n\n', '\n')  # remove double line breaks
    text = re.sub(r'http\S+', '', text)  # remove links
    text = re.sub(r'@\w+', '', text)  # remove mentions
    # text = re.sub(r'#\w+', '', text)  # remove hashtags
    text = text.encode('ascii', errors='ignore').decode()  # remove non-ASCII characters like unusual emojis
    return text.strip()

tweet_text = completion.choices[0].message.content.strip() # create tweet text from gemma
tweet_text = sanitize_tweet(tweet_text)

# Log tweet before sending
print("Sanitized Tweet:\n", tweet_text)

# Post to Twitter
client = get_client()
create_tweet(client, tweet_text)