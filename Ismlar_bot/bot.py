import asyncio
import logging
import sys
from aiogram import Bot, Dispatcher,types
from aiogram.enums import ParseMode
from aiogram.filters import CommandStart,Command
from aiogram import F
from aiogram.types import Message
from ismlar_bot import ismlar_manosi
from aiogram.client.session.aiohttp import AiohttpSession

TOKEN = "7026082741:AAGhvzkGqYI-j3HZXehlVv5xyVLc_0TuvQY"
dp = Dispatcher()

@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:

    full_name = message.from_user.full_name
    text = f"Assalomu alaykum,{full_name}\n Bu bot ismingizni ma'nosini topib beradi.Ismingizni kiriting !!!"
    await message.reply(text=text)
   
@dp.message(F.text)
async def name(message:Message):
    ism = message.text 
    natija = ismlar_manosi(ism=ism)

    await message.answer(text=natija)


async def main() -> None:

    bot = Bot(TOKEN, parse_mode=ParseMode.HTML)
    await dp.start_polling(bot)


if __name__ == "__main__":
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())