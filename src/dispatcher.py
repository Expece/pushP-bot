import logging
from aiogram import Bot, Dispatcher
from src.config import BOT_TOKEN
# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)