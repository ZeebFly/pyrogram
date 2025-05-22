
from typing import Union

import pyrogram
from pyrogram import raw


class IncrementStoryViews:
    async def increment_story_views(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
    ) -> bool:
        """Increment story views.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            story_id (``int``):
                Unique identifier of the target story.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Increment story views
                await app.increment_story_views(chat_id, 1)
        """
        r = await self.invoke(
            raw.functions.stories.IncrementStoryViews(
                peer=await self.resolve_peer(chat_id),
                id=story_id
            )
        )

        return r
