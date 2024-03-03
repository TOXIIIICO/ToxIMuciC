from pyrogram import Client, errors
from pyrogram.enums import ChatMemberStatus, ParseMode

import config

from ..logging import LOGGER


class Anony(Client):
    def __init__(self):
        LOGGER(__name__).info(f"جاري دخول البـوت لي فيجا")
        super().__init__(
            name="AnonXMusic",
            api_id=config.API_ID,
            api_hash=config.API_HASH,
            bot_token=config.BOT_TOKEN,
        )

    async def start(self):
        await super().start()
        self.id = self.me.id
        self.name = self.me.first_name + " " + (self.me.last_name or "")
        self.username = self.me.username
        self.mention = self.me.mention

        try:
            await self.send_message(
                chat_id=config.LOGGER_ID,
                text=f"⬢<u><b>» {self.mention}\n╮⭗ تم تشغيل البـوت\n╯⦿ علي سورس فيجا :</b><u>\n\n╭⭗ ɪᴅ : <code>{self.id}</code>\n│᚜⦿ᚐ ɴᴀᴍᴇ : {self.name}\n╰⭗ ᴜꜱᴇʀ ɴᴀᴍᴇ : @{self.username}",
            )
        except (errors.ChannelInvalid, errors.PeerIdInvalid):
            LOGGER(__name__).error(
                "Bot has failed to access the log group/channel. Make sure that you have added your bot to your log group/channel."
            )
            exit()
        except Exception as ex:
            LOGGER(__name__).error(
                f"فشل الروبوت في الوصول إلى مجموعة قناة السجل.\n السبب : {type(ex).__name__}."
            )
            exit()

        LOGGER(__name__).info(f"تم دخول المساعد{self.name} الي فيجا")

    async def stop(self):
        await super().stop()
