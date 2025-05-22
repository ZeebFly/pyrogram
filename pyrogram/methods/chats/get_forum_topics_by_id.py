
import logging
from typing import Union, List, Iterable

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram import utils

log = logging.getLogger(__name__)


class GetForumTopicsByID:
    async def get_forum_topics_by_id(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_ids: Union[int, Iterable[int]]
    ) -> Union["types.ForumTopic", List["types.ForumTopic"]]:
        """Get one or more topic from a chat by using topic identifiers.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_ids (``int`` | Iterable of ``int``, *optional*):
                Pass a single topic identifier or an iterable of topic ids (as integers) to get the information of the
                topic themselves.

        Returns:
            :obj:`~pyrogram.types.ForumTopic` | List of :obj:`~pyrogram.types.ForumTopic`: In case *topic_ids* was not
            a list, a single topic is returned, otherwise a list of topics is returned.

        Example:
            .. code-block:: python

                # Get one topic
                await app.get_forum_topics_by_id(chat_id, 12345)

                # Get more than one topic (list of topics)
                await app.get_forum_topics_by_id(chat_id, [12345, 12346])

        Raises:
            ValueError: In case of invalid arguments.
        """
        is_iterable = not isinstance(topic_ids, int)
        ids = list(topic_ids) if is_iterable else [topic_ids]

        r = await self.invoke(
            raw.functions.channels.GetForumTopicsByID(
                channel=await self.resolve_peer(chat_id),
                topics=ids
            )
        )

        topics = types.List()

        for i in r:
            topics.append(types.ForumTopic._parse(i))

        return topics if is_iterable else topics[0]
