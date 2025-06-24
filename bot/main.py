from asyncio import run

from createBot import bot, dp
from handlers import register_all_handlers


async def on_startup():
    register_all_handlers(dp)
    print('Бот начал свою работу')


async def on_shutdown():
    print('Бот завершил свою работу')


async def main():
    dp.startup.register(on_startup)
    dp.shutdown.register(on_shutdown)
    await dp.start_polling(bot)


if __name__ == '__main__':
    run(main(), debug=True)
