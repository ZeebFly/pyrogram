
from typing import Union

import pyrogram
from pyrogram import raw


class SetChatProtectedContent:
    async def set_chat_protected_content(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        enabled: bool
    ) -> bool:
        """Set the chat protected content setting.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            enabled (``bool``):
                Pass True to enable the protected content setting, False to disable.

        Returns:
            ``bool``: On success, True is returned.
        """

        await self.invoke(
            raw.functions.messages.ToggleNoForwards(
                peer=await self.resolve_peer(chat_id),
                enabled=enabled
            )
        )

        return True
