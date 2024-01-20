import contextlib
import asyncio
import sys
import types


from aiogram.types import ChatJoinRequest, InputFile, FSInputFile
from aiogram import Bot, Dispatcher, F
import logging
from config import TOKEN_BOT, ID_CHANNEL, ADMIN_ID, SESSION


TOKEN_BOT = TOKEN_BOT
ID_CHANNEL = ID_CHANNEL
ADMIN_ID = ADMIN_ID
dp = Dispatcher()


async def approve_request(chat_join: ChatJoinRequest, bot: Bot):
    msg = f'<b>⚡ Ваша заявка одобрена, ссылка для вступления:</b>\n' \
          f"https://t.me/+I713mwFVxvkyOGQy\n"
    photo = FSInputFile("img.png")
    await bot.send_photo(chat_id=chat_join.from_user.id, photo=photo, caption=msg, parse_mode="HTML")
    # await bot.send_photo(chat_id = chat_join.from_user.id, photo=photo)
    # await bot.send_message(chat_id=chat_join.from_user.id, text=msg,  parse_mode="HTML", disable_web_page_preview=True)


async def start():
    logging.basicConfig(level=logging.DEBUG,
                        format="%(asctime)s - [%(levelname)s] - %(name)s - "
                               "(%(filename)s).%(funcName)s(%lineno)d) - %(message)s")

    # session = AiohttpSession(proxy=SESSION)
    # bot: Bot = Bot(token=TOKEN_BOT, session=session)
    bot: Bot = Bot(token=TOKEN_BOT)
    dp.chat_join_request.register(approve_request, F.chat.id == ID_CHANNEL)

    try:
        await dp.start_polling(bot, allowed_updates=dp.resolve_used_update_types())
    except Exception as ex:
        logging.error(f'[Exception] - {ex}', exc_info=True)
    finally:
        await bot.session.close()


if __name__ == '__main__':
    with contextlib.suppress(KeyboardInterrupt, SystemExit):
        logging.basicConfig(level=logging.INFO, stream=sys.stdout)
        asyncio.run(start())
