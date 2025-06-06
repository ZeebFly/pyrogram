
from typing import Union

import pyrogram
from pyrogram import raw


class GetChatAdminInviteLinksCount:
    async def get_chat_admin_invite_links_count(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        admin_id: Union[int, str],
        revoked: bool = False,
    ) -> int:
        """Get the count of the invite links created by an administrator in a chat.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            admin_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            revoked (``bool``, *optional*):
                True, if you want to get revoked links instead.
                Defaults to False (get active links only).

        Returns:
            ``int``: On success, the invite links count is returned.
        """
        r = await self.invoke(
            raw.functions.messages.GetExportedChatInvites(
                peer=await self.resolve_peer(chat_id),
                admin_id=await self.resolve_peer(admin_id),
                limit=1,
                revoked=revoked
            )
        )

        return r.count
