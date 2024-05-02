import asyncio
import logging

from aiogram import Bot, Dispatcher
from aiogram.client.bot import DefaultBotProperties

from config import Config
from src.database import create_session_factory
from src.dialogs.setup import setup_dialogs
from src.handlers import setup_handlers
from src.middlewares.setup import setup_middlewares


async def main():
    logging.basicConfig(level=logging.INFO, format="%(asctime)s - %(levelname)s - %(name)s - %(message)s")

    config = Config.from_file("config.toml")

    session_maker = create_session_factory(config.database.dsn)

    dp = Dispatcher()

    setup_middlewares(dp, session_maker=session_maker)
    setup_handlers(dp)
    setup_dialogs(dp)

    bot = Bot(config.telegram.bot_token, default=DefaultBotProperties(parse_mode='HTML'))

    await bot.delete_webhook(drop_pending_updates=True)
    await dp.start_polling(bot)


if __name__ == '__main__':
    asyncio.run(main())
