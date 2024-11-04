from aiogram import Bot, Dispatcher
from aiogram.filters import Command
from aiogram.types import Message
from hugchat import hugchat
from hugchat.login import Login


BOT_TOKEN = "YOU Token"
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher()

def AiDialog(user_input, email, passwork):
    sing = Login(email, passwork)

    cooke = sing.login()

    chat_bot = hugchat.ChatBot(cookies=cooke.get_dict())

    return chat_bot.chat(user_input)



@dp.message(Command(commands=["ai"]))
async def Ai_progress(message: Message):

    message.text.replace("/AI", "")
    message.text.strip()

    r = "" + AiDialog(str(message.text), "email", "pas")
    await message.reply(r)



if __name__ == "__main__":
    dp.run_polling(bot)
