
from typing import List, Union

import pyrogram
from pyrogram import raw, types


class ReadStories:
    async def read_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        max_id: int = 0,
    ) -> List[int]:
        """Read stories.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            max_id (``int``, *optional*):
                Maximum identifier of the target story to read.

        Returns:
            List of ``int``: On success, a list of read stories is returned.

        Example:
            .. code-block:: python

                # Read stories
                await app.read_stories(chat_id)
        """
        r = await self.invoke(
            raw.functions.stories.ReadStories(
                peer=await self.resolve_peer(chat_id),
                max_id=max_id
            )
        )

        return types.List(r)
