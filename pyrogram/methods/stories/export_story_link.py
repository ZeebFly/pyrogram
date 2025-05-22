
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class ExportStoryLink:
    async def export_story_link(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        story_id: int,
    ) -> "types.ExportedStoryLink":
        """Export a story link.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            story_id (``int``):
                Unique identifier of the target story.

        Returns:
            ``str``: On success, a link to the exported story is returned.

        Example:
            .. code-block:: python

                # Export a story link
                link = app.export_story_link(chat_id, 1)
        """
        r = await self.invoke(
            raw.functions.stories.ExportStoryLink(
                peer=await self.resolve_peer(chat_id),
                id=story_id
            )
        )

        return r.link
