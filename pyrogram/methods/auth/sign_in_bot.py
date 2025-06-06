
import logging

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram.errors import UserMigrate
from pyrogram.session import Session, Auth

log = logging.getLogger(__name__)


class SignInBot:
    async def sign_in_bot(
        self: "pyrogram.Client",
        bot_token: str
    ) -> "types.User":
        """Authorize a bot using its bot token generated by BotFather.

        .. include:: /_includes/usable-by/bots.rst

        Parameters:
            bot_token (``str``):
                The bot token generated by BotFather

        Returns:
            :obj:`~pyrogram.types.User`: On success, the bot identity is return in form of a user object.

        Raises:
            BadRequest: In case the bot token is invalid.
        """
        while True:
            try:
                r = await self.invoke(
                    raw.functions.auth.ImportBotAuthorization(
                        flags=0,
                        api_id=self.api_id,
                        api_hash=self.api_hash,
                        bot_auth_token=bot_token
                    )
                )
            except UserMigrate as e:
                await self.session.stop()

                await self.storage.dc_id(e.value)
                await self.storage.auth_key(
                    await Auth(
                        self, await self.storage.dc_id(),
                        await self.storage.test_mode()
                    ).create()
                )
                self.session = Session(
                    self, await self.storage.dc_id(),
                    await self.storage.auth_key(), await self.storage.test_mode()
                )

                await self.session.start()
            else:
                await self.storage.user_id(r.user.id)
                await self.storage.is_bot(True)

                return types.User._parse(self, r.user)
