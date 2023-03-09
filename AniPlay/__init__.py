import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "10683462")),
    api_hash= os.environ.get("API_HASH", "8ab812d6e6849bd6352dcb731e44c31e"),
    bot_token= os.environ.get("TOKEN", "5680348811:AAG-O3TXsyQpO4eSC3j1uFZeqDYyZrmD6sw")
)
