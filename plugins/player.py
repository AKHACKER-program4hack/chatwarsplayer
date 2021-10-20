from pyrogram import Client, filters
import time


@Client.on_message(filters.user(["chtwrsbot"]))
async def send_all(client, message):
  message_id = message.message_id
  chat_id = message.chat.id
  try:
    get_inline = message.reply_markup.inline_keyboard
  except Exception as error:
    pass
  timer = 427
  try:
    call_backs = []
    i = 0
    for inline in get_inline:
      try:
        check_list = isinstance(inline, list)
        if check_list:
          for lis in inline:
            if i <= 2:
              call_backs.append(lis.callback_data)
        else:
          print(check_list)
          # print(inline)
      except Exception as error:
        print(error)
    print(call_backs)
    for callback_data in call_backs:
      try:
        time.sleep(3)
        print("clicking " + str(callback_data))
        while True:
          a = await client.request_callback_answer(
                chat_id=chat_id,
                message_id=message_id,
                callback_data=callback_data,
                timeout=5
                )
          if len(a) > 2:
            print(a)
            break
          else:
            time.sleep(10)
            print("not getting response waiting for 10 sec")  
        print("Waiting for "+ str(timer) +" seconds")
        time.sleep(timer)
      except Exception as error:
        print(error)
  except Exception as error:
    print(error)
