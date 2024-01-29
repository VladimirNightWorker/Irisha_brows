from aiogram import Bot, Dispatcher, Router, types
from aiogram.filters import CommandStart
from aiogram.types import Message, BotCommand
from aiogram.utils import keyboard
from aiogram.enums import ParseMode
from aiogram.utils.markdown import hbold
import asyncio
import sys, logging
from os import getenv
from lexicon.lexicon_ru import LEXICON_COMMANDS_RU
from keyboards.set_menu import set_main_menu


TOKEN: str = getenv('BOT_TOKEN')
dp = Dispatcher()


@dp.message(CommandStart())
async def command_start_handler(message: Message) -> None:
    await message.answer(f"{hbold(message.from_user.first_name)}, Приветствую тебя красотка!!!")



async def main():
    bot = Bot(token=TOKEN, parse_mode=ParseMode.HTML)
    dp.startup.register(set_main_menu)
    await dp.start_polling(bot)


if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO, stream=sys.stdout)
    asyncio.run(main())
