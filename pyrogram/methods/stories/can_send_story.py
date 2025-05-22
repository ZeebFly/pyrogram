
from typing import Union, Iterable

import pyrogram
from pyrogram import raw
from pyrogram import types


class CanSendStory:
    async def can_send_story(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
    ) -> bool:
        """Can send story

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``str``: On success, a bool is returned.

        Example:
            .. code-block:: python

                # Check if you can send story to chat id
                app.can_send_story(chat_id)
        """
        r = await self.invoke(
            raw.functions.stories.CanSendStory(
                peer=await self.resolve_peer(chat_id),
            )
        )

        return r
