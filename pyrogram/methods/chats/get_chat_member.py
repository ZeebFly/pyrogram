
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram.errors import UserNotParticipant


class GetChatMember:
    async def get_chat_member(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        user_id: Union[int, str]
    ) -> "types.ChatMember":
        """Get information about one member of a chat.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            user_id (``int`` | ``str``)::
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            :obj:`~pyrogram.types.ChatMember`: On success, a chat member is returned.

        Example:
            .. code-block:: python

                member = await app.get_chat_member(chat_id, "me")
                print(member)
        """
        chat = await self.resolve_peer(chat_id)
        user = await self.resolve_peer(user_id)

        if isinstance(chat, raw.types.InputPeerChat):
            r = await self.invoke(
                raw.functions.messages.GetFullChat(
                    chat_id=chat.chat_id
                )
            )

            members = getattr(r.full_chat.participants, "participants", [])
            users = {i.id: i for i in r.users}

            for member in members:
                member = types.ChatMember._parse(self, member, users, {})

                if isinstance(user, raw.types.InputPeerSelf):
                    if member.user.is_self:
                        return member
                else:
                    if member.user.id == user.user_id:
                        return member
            else:
                raise UserNotParticipant
        elif isinstance(chat, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetParticipant(
                    channel=chat,
                    participant=user
                )
            )

            users = {i.id: i for i in r.users}
            chats = {i.id: i for i in r.chats}

            return types.ChatMember._parse(self, r.participant, users, chats)
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')
