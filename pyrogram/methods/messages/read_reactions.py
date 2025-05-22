
from typing import Union

import pyrogram
from pyrogram import raw


class ReadReactions:
    async def read_reactions(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Mark a reaction in the chat as read.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool`` - On success, True is returned.

        Example:
            .. code-block:: python

                # Mark the chat reaction as read
                await app.read_reactions(chat_id)
        """
        r = await self.invoke(
            raw.functions.messages.ReadReactions(
                peer=await self.resolve_peer(chat_id)
            )
        )

        return bool(r)
