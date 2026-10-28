from aiogram import Router
from aiogram.filters import CommandStart
from aiogram.types import Message

router = Router()


@router.message(CommandStart())
async def start_handler(message: Message):
    await message.answer("Привет!")

@router.message(Command("help"))
async def help_handler(message: Message):
    await message.answer("Доступные команды:\n/start — приветствие\n/help — эта справка")


@router.message(Command("about"))
async def about_handler(message: Message):
    await message.answer("Шаблон Telegram-бота на aiogram 3.")