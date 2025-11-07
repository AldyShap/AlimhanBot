import asyncio

from aiogram import Bot,Dispatcher
from confiq import BOT_TOKEN
from app.handlers import router
from app.Callbacks import router2
from database.models import async_main

bot = Bot(BOT_TOKEN)
dp = Dispatcher()

async def main():
    dp.include_router(router)
    dp.include_router(router2)
    await async_main()
    await dp.start_polling(bot)

if __name__ == "__main__":
    try:
        asyncio.run(main())
    except Exception as e:
        print(f"Oh, something went wrong!!! here is the problem: {e}")
    except KeyboardInterrupt:
        print('bot is stopped')
    finally:
        print("Bot made a great job!")