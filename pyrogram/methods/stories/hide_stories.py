
from typing import Union

import pyrogram
from pyrogram import raw


class HideStories:
    async def hide_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        hidden: bool = None
    ) -> bool:
        """Toggle peer stories hidden

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``str``: On success, a bool is returned.

        Example:
            .. code-block:: python

                # Export a story link
                link = app.hide_stories("me")
        """
        r = await self.invoke(
            raw.functions.stories.TogglePeerStoriesHidden(
                peer=await self.resolve_peer(chat_id),
                hidden=hidden
            )
        )

        return r
