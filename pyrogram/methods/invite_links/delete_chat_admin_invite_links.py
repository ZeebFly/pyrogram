
from typing import Union

import pyrogram
from pyrogram import raw


class DeleteChatAdminInviteLinks:
    async def delete_chat_admin_invite_links(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        admin_id: Union[int, str],
    ) -> bool:
        """Delete all revoked invite links of an administrator.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier for the target chat or username of the target channel/supergroup
                (in the format @username).

            admin_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: On success ``True`` is returned.
        """

        return await self.invoke(
            raw.functions.messages.DeleteRevokedExportedChatInvites(
                peer=await self.resolve_peer(chat_id),
                admin_id=await self.resolve_peer(admin_id),
            )
        )
