
import pyrogram
from pyrogram import raw
from pyrogram import types
from typing import Union


class DeleteForumTopic:
    async def delete_forum_topic(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_id: int
    ) -> bool:
        """Delete a forum topic.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_id (``int``):
                Unique identifier (int) of the target forum topic.

        Returns:
            `bool`: On success, a Boolean is returned.

        Example:
            .. code-block:: python

                await app.delete_forum_topic(chat_id, topic_id)
        """
        await self.invoke(
            raw.functions.channels.DeleteTopicHistory(
                channel=await self.resolve_peer(chat_id),
                top_msg_id=topic_id
            )
        )

        return True
