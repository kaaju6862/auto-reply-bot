import logging
import logging.config
from pyrogram import Client
from bot.config import Config


# Get logging configurations

logging.getLogger().setLevel(logging.INFO)


class Bot(Client):
    def __init__(self):
        super().__init__(
            "bot",
            api_id=Config.API_ID,
            api_hash=Config.API_HASH,
            bot_token=Config.BOT_TOKEN,
            plugins=dict(root="bot/plugins"),
        )

    async def start(self):
        await super().start()

        me = await self.get_me()

        self.username = f"@{me.username}"

        logging.info("Bot started")

    async def stop(self, *args):
        await super().stop()
