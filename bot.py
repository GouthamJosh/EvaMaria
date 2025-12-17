import logging
import logging.config
import asyncio
import os
import threading

# ---------------- LOGGING ---------------- #
logging.config.fileConfig("logging.conf")
logging.getLogger().setLevel(logging.INFO)
logging.getLogger("pyrogram").setLevel(logging.ERROR)
logging.getLogger("imdbpy").setLevel(logging.ERROR)

# ---------------- PYROGRAM ---------------- #
from pyrogram import Client, __version__, types
from pyrogram.raw.all import layer
from typing import Union, Optional, AsyncGenerator

# ---------------- AIOHTTP WEB SERVER ---------------- #
from aiohttp import web

# ---------------- DATABASE / UTILS ---------------- #
from database.ia_filterdb import Media
from database.users_chats_db import db
from info import SESSION, API_ID, API_HASH, BOT_TOKEN, LOG_STR
from utils import temp

PORT = int(os.environ.get("PORT", 8000))


# ================= WEB SERVER ================= #
async def health_check(request):
    return web.json_response({
        "status": "running",
        "bot": "Telegram Pyrogram Bot"
    })


async def start_webserver():
    app = web.Application()
    app.router.add_get("/", health_check)
    app.router.add_get("/health", health_check)

    runner = web.AppRunner(app)
    await runner.setup()
    site = web.TCPSite(runner, "0.0.0.0", PORT)
    await site.start()

    logging.info(f"🌐 Web service running on port {PORT}")

    # keep web server alive
    while True:
        await asyncio.sleep(3600)


def run_webserver():
    asyncio.run(start_webserver())


# ================= BOT CLIENT ================= #
class Bot(Client):

    def __init__(self):
        super().__init__(
            name=SESSION,
            api_id=API_ID,
            api_hash=API_HASH,
            bot_token=BOT_TOKEN,
            workers=50,
            plugins={"root": "plugins"},
            sleep_threshold=5,
        )

    async def start(self):
        # Load banned users/chats (Motor uses Pyrogram loop ✔)
        b_users, b_chats = await db.get_banned()
        temp.BANNED_USERS = b_users
        temp.BANNED_CHATS = b_chats

        await super().start()

        # Ensure DB indexes
        await Media.ensure_indexes()

        me = await self.get_me()
        temp.ME = me.id
        temp.U_NAME = me.username
        temp.B_NAME = me.first_name
        self.username = f"@{me.username}"

        logging.info(
            f"{me.first_name} started | Pyrogram v{__version__} | "
            f"Layer {layer} | @{me.username}"
        )
        logging.info(LOG_STR)

    async def stop(self, *args):
        await super().stop()
        logging.info("🛑 Bot stopped. Bye.")

    async def iter_messages(
        self,
        chat_id: Union[int, str],
        limit: int,
        offset: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        current = offset
        while True:
            batch = min(200, limit - current)
            if batch <= 0:
                return

            messages = await self.get_messages(
                chat_id,
                list(range(current, current + batch + 1))
            )

            for message in messages:
                yield message
                current += 1


# ================= MAIN ================= #
if __name__ == "__main__":
    # Start web server in background thread
    threading.Thread(target=run_webserver, daemon=True).start()

    # Start Pyrogram (owns main event loop)
    bot = Bot()
    bot.run()
