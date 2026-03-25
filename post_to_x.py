import tweepy
import os
from dotenv import load_dotenv

load_dotenv()

client = tweepy.Client(
    consumer_key=os.getenv("X_API_KEY"),
    consumer_secret=os.getenv("X_API_SECRET"),
    access_token=os.getenv("X_ACCESS_TOKEN"),
    access_token_secret=os.getenv("X_ACCESS_TOKEN_SECRET"),
)

# テスト投稿
response = client.create_tweet(text="テスト投稿 from Claude Code")
print(f"投稿成功！ https://x.com/kawa_it_toushi/status/{response.data['id']}")
