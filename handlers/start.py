from aiogram import F, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, Message
from aiogram.filters import Command
from sqlalchemy.future import select
from sqlalchemy.ext.asyncio import AsyncSession

from bot.database import get_db
from models.user import User
from keyboards.default_keyboards import setup_kbd

starter = Router()

@starter.message(Command("start"))
async def start_handler(message: Message):
    user_id = message.from_user.id
    user_name = message.from_user.full_name

    async with get_db() as session:
        result = await session.execute(select(User).where(User.tg_id == user_id))
        user = result.scalar()

        if not user:
            new_user = User(tg_id=user_id, name=user_name)
            session.add(new_user)
            await session.commit()
            text = f"Привет, {user_name}! Добро пожаловать в наш отель, выбери ниже что интересует?"
        else:
            text = f"С возвращением, {user_name}"

    await message.answer(text, reply_markup=setup_kbd("Отель", "Ресторан"))

