
from typing import AsyncGenerator, Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetStoriesArchive:
    async def get_stories_archive(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        limit: int = 0,
        offset_id: int = 0
    ) -> Optional[AsyncGenerator["types.Story", None]]:
        """Get stories archive.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            limit (``int``, *optional*):
                Limits the number of stories to be retrieved.
                By default, no limit is applied and all stories are returned.

            offset_id (``int``, *optional*):
                Identifier of the first story to be returned.

        Yields:
            :obj:`~pyrogram.types.Story` objects.

        Example:
            .. code-block:: python

                # Get stories archive
                async for story in app.get_stories_archive(chat_id):
                    print(story)
        """
        current = 0
        total = abs(limit) or (1 << 31)
        limit = min(100, total)

        while True:
            peer = await self.resolve_peer(chat_id)
            r = await self.invoke(
                raw.functions.stories.GetStoriesArchive(
                    peer=peer,
                    offset_id=offset_id,
                    limit=limit
                )
            )

            if not r.stories:
                return

            last = r.stories[-1]
            offset_id = last.id

            users = {i.id: i for i in r.users}
            chats = {i.id: i for i in r.chats}

            for story in r.stories:
                yield await types.Story._parse(
                    self,
                    story,
                    users,
                    chats,
                    peer
                )

                current += 1

                if current >= total:
                    return
