from aiogram.types import ReplyKeyboardMarkup, KeyboardButton


base_users_kb = ReplyKeyboardMarkup(
    keyboard=[
        [KeyboardButton(text='Случайная мышца'), KeyboardButton(text='Анатомическое движение')],
        [KeyboardButton(text='Канал EFS')]
    ],
    resize_keyboard=True
)
