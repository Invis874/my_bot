import asyncio
import logging

from app.bot import create_bot, create_dispatcher
from config import settings


logging.basicConfig(level=logging.INFO)


async def main():
    bot = create_bot()
    dp = create_dispatcher()
    await dp.start_polling(bot)


if __name__ == "__main__":
    asyncio.run(main())