from config import *
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id=API_ID,
    api_hash=API_HASH,
    bot_token=TOKEN
)
