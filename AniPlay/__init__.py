from os import environ
from pyrogram.client import Client

app = Client(
    "AniPlay",
    api_id= int(environ.get("APP_ID", "2531382")),
    api_hash= environ.get("API_HASH", "12a15ce8f731edb4e9c4b6df278916d9"),
    bot_token= environ.get("TOKEN", "6039304283:AAHo9xR7HBz9o7zn0kViJtfyixmm51DLvi8")
)
