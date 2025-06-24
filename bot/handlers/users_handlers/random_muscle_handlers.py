from aiogram import types, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.exceptions import TelegramNetworkError

from random import choice

from muscles_config import MUSCLES

async def random_muscle(m: types.Message):
    if MUSCLES:
        muscle: dict = choice(MUSCLES)

        muscle_name = muscle.get('name', '')
        muscle_start_point = muscle.get('start_point', '')
        muscle_attachment = muscle.get('attachment', '')
        muscle_function = muscle.get('function', '')

        muscle_image = muscle.get('image')
        if muscle_name:
            if muscle_image:
                try:
                    image_file = types.FSInputFile('static/muscles_images/' + muscle_image)
                    await m.answer_photo(
                        photo=image_file,
                        caption=muscle_name
                    )
                except TelegramNetworkError as ex:
                    print(f'Не найдена картинка с именем "{muscle_image}" для мышцы {muscle_name}')
            else:
                await m.answer(
                    muscle_name
                )

        await m.answer(
            'Точка начала: ' + f'||{muscle_start_point}||',
            parse_mode=ParseMode.MARKDOWN_V2
        )
        await m.answer(
            'Точка крепления: ' + f'||{muscle_attachment}||',
            parse_mode=ParseMode.MARKDOWN_V2
        )
        await m.answer(
            'Функции: ' + f'||{muscle_function}||',
            parse_mode=ParseMode.MARKDOWN_V2
        )

    else:
        await m.answer(
            'Не удалось получить информацию о какой-либо мышце'
        )
        print('Ошибка: невозможно получить информацию о мышцах(пустой массив)')


def register_random_muscle_handlers(dp: Dispatcher):
    dp.message.register(random_muscle, F.text == 'Случайная мышца')
