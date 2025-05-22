
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class StartBot:
    async def start_bot(
        self: "pyrogram.Client",
        bot: Union[int, str],
        start_param: str = ""
    ) -> bool:
        """Start bot

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            bot (``int`` | ``str``):
                Unique identifier of the bot you want to be started. You can specify
                a @username (str) or a bot ID (int).

            start_param (``str``):
                Text of the param (up to 64 characters).
                Defaults to "" (empty string).

        Returns:
            ``bool`` - On success, True is returned.

        Example:
            .. code-block:: python

                # Start bot
                await app.start_bot("pyrogrambot")
        """
        r = await self.invoke(
            raw.functions.messages.StartBot(
                bot=await self.resolve_peer(bot),
                peer=raw.types.InputPeerSelf(),
                random_id=self.rnd_id(),
                start_param=start_param
            )
        )

        for i in r.updates:
            if isinstance(i, raw.types.UpdateNewMessage):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )
