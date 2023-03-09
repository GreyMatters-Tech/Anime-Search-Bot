import os
from config import *
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id=int(os.environ.get("API_ID")),
    api_hash=API_HASH,
    bot_token=TOKEN
)
