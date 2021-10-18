from pyrogram import Client, filters
import os, sys
import time

API_ID = os.environ.get("API_ID", None)
API_HASH = os.environ.get("API_HASH", None)
USERBOT_SESSION = os.environ.get("USERBOT_SESSION", None)

Client(USERBOT_SESSION, api_hash=API_HASH,api_id=API_ID).run()

