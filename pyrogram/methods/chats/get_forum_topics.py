
from typing import Union, Optional, AsyncGenerator

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetForumTopics:
    async def get_forum_topics(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        limit: int = 0
    ) -> Optional[AsyncGenerator["types.ForumTopic", None]]:
        """Get one or more topic from a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            limit (``int``, *optional*):
                Limits the number of topics to be retrieved.

        Returns:
            ``Generator``: On success, a generator yielding :obj:`~pyrogram.types.ForumTopic` objects is returned.

        Example:
            .. code-block:: python

                # get all forum topics
                async for topic in app.get_forum_topics(chat_id):
                    print(topic)
        """
        r = await self.invoke(
            raw.functions.channels.GetForumTopics(
                channel=await self.resolve_peer(chat_id),
                offset_date=0,
                offset_id=0,
                offset_topic=0,
                limit=limit
            )
        )

        for topic in r.topics:
            yield types.ForumTopic._parse(topic)
