import logging

from aiogram import Bot, Dispatcher
from aiogram.client.session.aiohttp import AiohttpSession

from app.handlers import start
from config import settings


def create_bot() -> Bot:
    if settings.proxy_url:
        logging.info(f"Использую прокси: {settings.proxy_url}")
        session = AiohttpSession(proxy=settings.proxy_url, timeout=30)
    else:
        logging.info("Прокси не задан, подключаюсь напрямую")
        session = AiohttpSession(timeout=30)
    return Bot(token=settings.bot_token, session=session)


def create_dispatcher() -> Dispatcher:
    dp = Dispatcher()
    dp.include_router(start.router)
    # сюда же будешь добавлять другие роутеры:
    # dp.include_router(admin.router)
    # dp.include_router(echo.router)
    return dp