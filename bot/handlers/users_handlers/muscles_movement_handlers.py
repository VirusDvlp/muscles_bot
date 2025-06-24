from aiogram import types, Dispatcher, F
from aiogram.enums import ParseMode

from random import choice

from muscles_config import MUSCLES_MOVEMENT

async def random_movement(m: types.Message):
    if MUSCLES_MOVEMENT:
        muscle_movement: dict = choice(MUSCLES_MOVEMENT)

        movement_name = muscle_movement.get('name', '')
        muscles: list = muscle_movement.get('muscles', [])

        await m.answer(
            movement_name + ':'
        )
        digit_emojis = {
            '0': '0️⃣', '1': '1️⃣', '2': '2️⃣', '3': '3️⃣', '4': '4️⃣', '5': '5️⃣', '6': '6️⃣', '7': '7️⃣', '8': '8️⃣', '9': '9️⃣' # преобразование числа в эмодзи
        }

        if muscles:
            for i in range(len(muscles)):
                await m.answer(
                    f'{"".join([digit_emojis.get(s) for s in str(i + 1)])}\\. ||{muscles[i]}||',
            	    parse_mode=ParseMode.MARKDOWN_V2
                )

    else:
        await m.answer(
            'Не удалось получить информацию о каком-либо анатомическом движении'
        )
        print('Ошибка: невозможно получить информацию об анатомических движениях(пустой массив)')


def register_muscles_movement_handlers(dp: Dispatcher):
        dp.message.register(random_movement, F.text == 'Анатомическое движение')
