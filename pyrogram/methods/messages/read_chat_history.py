
from typing import Union

import pyrogram
from pyrogram import raw


class ReadChatHistory:
    async def read_chat_history(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        max_id: int = 0
    ) -> bool:
        """Mark a chat's message history as read.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            max_id (``int``, *optional*):
                The id of the last message you want to mark as read; all the messages before this one will be marked as
                read as well. Defaults to 0 (mark every unread message as read).

        Returns:
            ``bool`` - On success, True is returned.

        Example:
            .. code-block:: python

                # Mark the whole chat as read
                await app.read_chat_history(chat_id)

                # Mark messages as read only up to the given message id
                await app.read_chat_history(chat_id, 12345)
        """

        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChannel):
            q = raw.functions.channels.ReadHistory(
                channel=peer,
                max_id=max_id
            )
        else:
            q = raw.functions.messages.ReadHistory(
                peer=peer,
                max_id=max_id
            )

        await self.invoke(q)

        return True
