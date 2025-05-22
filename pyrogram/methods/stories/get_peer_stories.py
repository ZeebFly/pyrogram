
from typing import AsyncGenerator, Union, Optional

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetPeerStories:
    async def get_peer_stories(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> Optional[AsyncGenerator["types.Story", None]]:
        """Get all active stories from an user by using user identifiers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For your personal story you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.Story` objects is returned.

        Example:
            .. code-block:: python

                # Get all active story from spesific user
                async for story in app.get_peer_stories(chat_id):
                    print(story)

        Raises:
            ValueError: In case of invalid arguments.
        """
        peer = await self.resolve_peer(chat_id)

        r = await self.invoke(
            raw.functions.stories.GetPeerStories(
                peer=peer
            )
        )

        users = {i.id: i for i in r.users}
        chats = {i.id: i for i in r.chats}

        for story in r.stories.stories:
            yield await types.Story._parse(
                self,
                story,
                users,
                chats,
                r.stories.peer
            )
