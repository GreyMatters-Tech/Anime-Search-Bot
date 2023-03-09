from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "")),
    api_hash= environ.get("API_HASH", ""),
    bot_token= environ.get("TOKEN", "")
)
