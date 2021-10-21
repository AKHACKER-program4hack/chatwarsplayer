from pyrogram import Client, filters
import time


@Client.on_message(filters.user(["chtwrsbot"]) & filters.incoming & filters.inline_keyboard)
async def send_all(client, message):
  message_id = message.message_id
  chat_id = message.chat.id
  time.sleep(2)
  timer = 427
  if "🌲Forest " in message.text:
    for i in range(0,3):
      try:
        print("clicking " + str(i))
        await message.click(i)
        print("Waiting for " + str(timer))
        time.sleep(427)
      except Exception as error:
        print(error)
    return
