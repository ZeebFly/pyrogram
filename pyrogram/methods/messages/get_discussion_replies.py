
from typing import Union, Optional, AsyncGenerator

import pyrogram
from pyrogram import types, raw


class GetDiscussionReplies:
    async def get_discussion_replies(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        limit: int = 0,
    ) -> Optional[AsyncGenerator["types.Message", None]]:
        """Get the message replies of a discussion thread.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Message id.

            limit (``int``, *optional*):
                Limits the number of messages to be retrieved.
                By default, no limit is applied and all messages are returned.

        Example:
            .. code-block:: python

                async for message in app.get_discussion_replies(chat_id, message_id):
                    print(message)
        """

        current = 0
        total = limit or (1 << 31) - 1
        limit = min(100, total)

        while True:
            r = await self.invoke(
                raw.functions.messages.GetReplies(
                    peer=await self.resolve_peer(chat_id),
                    msg_id=message_id,
                    offset_id=0,
                    offset_date=0,
                    add_offset=current,
                    limit=limit,
                    max_id=0,
                    min_id=0,
                    hash=0
                )
            )

            users = {u.id: u for u in r.users}
            chats = {c.id: c for c in r.chats}
            messages = r.messages

            if not messages:
                return

            for message in messages:
                yield await types.Message._parse(self, message, users, chats, replies=0)

                current += 1

                if current >= total:
                    return
