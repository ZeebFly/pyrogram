
import pyrogram
from pyrogram import raw
from pyrogram import types
from typing import Union


class EditForumTopic:
    async def edit_forum_topic(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        topic_id: int,
        title: str = None,
        icon_emoji_id: int = None,
        closed: bool = None,
        hidden: bool = None
    ) -> bool:
        """Edit a forum topic.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            topic_id (``int``):
                Unique identifier (int) of the target forum topic.

            title (``str``, *optional*):
                The forum topic title.

            icon_emoji_id (``int``, *optional*):
                Unique identifier of the custom emoji shown as the topic icon.

            closed (``bool``, *optional*):
                Close forum topic.

            hidden (``bool``, *optional*):
                Hide forum topic.

        Returns:
            `bool`: On success, a Boolean is returned.

        Example:
            .. code-block:: python

                await app.edit_forum_topic(chat_id,topic_id,"New Topic Title")
        """
        await self.invoke(
            raw.functions.channels.EditForumTopic(
                channel=await self.resolve_peer(chat_id),
                topic_id=topic_id,
                title=title,
                icon_emoji_id=icon_emoji_id,
                closed=closed,
                hidden=hidden
            )
        )

        return True
