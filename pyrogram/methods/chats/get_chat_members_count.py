
from typing import Union

import pyrogram
from pyrogram import raw


class GetChatMembersCount:
    async def get_chat_members_count(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> int:
        """Get the number of members in a chat.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            ``int``: On success, the chat members count is returned.

        Raises:
            ValueError: In case a chat id belongs to user.

        Example:
            .. code-block:: python

                count = await app.get_chat_members_count(chat_id)
                print(count)
        """
        peer = await self.resolve_peer(chat_id)

        if isinstance(peer, raw.types.InputPeerChat):
            r = await self.invoke(
                raw.functions.messages.GetChats(
                    id=[peer.chat_id]
                )
            )

            return r.chats[0].participants_count
        elif isinstance(peer, raw.types.InputPeerChannel):
            r = await self.invoke(
                raw.functions.channels.GetFullChannel(
                    channel=peer
                )
            )

            return r.full_chat.participants_count
        else:
            raise ValueError(f'The chat_id "{chat_id}" belongs to a user')
