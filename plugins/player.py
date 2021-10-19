from pyrogram import Client, filters
import time


@Client.on_message(filters.user(["chtwrsbot"]))
async def send_all(client, message):
  message_id = message.message_id
  chat_id = message.chat.id
  get_inline = message.reply_markup.inline_keyboard
  while True:
    try:
      for inline in get_inline:
        # print(inline)
        check_list = isinstance(inline, list)
        if check_list:
          for lis in inline:
            time.sleep(3)
            print("clicking " + str(lis.callback_data))
            callback_data = lis.callback_data
            a = await client.request_callback_answer(
              chat_id=chat_id,
              message_id=message_id,
              callback_data=callback_data
              )
            print("Waiting for 7 minutes")
            time.sleep(427)
    except Exception as error:
      print(str(error))
      time.sleep(10)