import os
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(os.environ.get("APP_ID", "")),
    api_hash= os.environ.get("API_HASH", ""),
    bot_token= os.environ.get("TOKEN", "")
)
