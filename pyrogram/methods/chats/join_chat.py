
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class JoinChat:
    async def join_chat(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> "types.Chat":
        """Join a group chat or channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat in form of a *t.me/joinchat/* link, a username of the target
                channel/supergroup (in the format @username) or a chat id of a linked chat (channel or supergroup).

        Returns:
            :obj:`~pyrogram.types.Chat`: On success, a chat object is returned.

        Example:
            .. code-block:: python

                # Join chat via invite link
                await app.join_chat("https://t.me/+AbCdEf0123456789")

                # Join chat via username
                await app.join_chat("pyrogram")

                # Join a linked chat
                await app.join_chat(app.get_chat("pyrogram").linked_chat.id)
        """
        match = self.INVITE_LINK_RE.match(str(chat_id))

        if match:
            chat = await self.invoke(
                raw.functions.messages.ImportChatInvite(
                    hash=match.group(1)
                )
            )
            if isinstance(chat.chats[0], raw.types.Chat):
                return types.Chat._parse_chat_chat(self, chat.chats[0])
            elif isinstance(chat.chats[0], raw.types.Channel):
                return types.Chat._parse_channel_chat(self, chat.chats[0])
        else:
            chat = await self.invoke(
                raw.functions.channels.JoinChannel(
                    channel=await self.resolve_peer(chat_id)
                )
            )

            return types.Chat._parse_channel_chat(self, chat.chats[0])
