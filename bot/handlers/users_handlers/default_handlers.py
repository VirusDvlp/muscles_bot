"""Базовые обработчики, такие как команда /start или выдача ссылки на канал"""

from aiogram import types, Dispatcher, F
from aiogram.filters import CommandStart

from keyboards import base_users_kb
from muscles_config import CHANNEL_INFO_MESSAGE


async def start_cmd(m: types.Message):
    await m.answer(
        'Начально сообщение',
        reply_markup=base_users_kb
    )


async def show_channel(m: types.Message):
    """Ссылка на канал"""
    await m.answer(CHANNEL_INFO_MESSAGE)


def register_default_handlers(dp: Dispatcher):
    dp.message.register(start_cmd, CommandStart())
    dp.message.register(show_channel, F.text == 'Канал EFS')
