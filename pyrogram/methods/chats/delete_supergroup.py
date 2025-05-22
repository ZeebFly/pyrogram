
from typing import Union

import pyrogram
from pyrogram import raw


class DeleteSupergroup:
    async def delete_supergroup(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> bool:
        """Delete a supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The id of the supergroup to be deleted.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.delete_supergroup(supergroup_id)
        """
        await self.invoke(
            raw.functions.channels.DeleteChannel(
                channel=await self.resolve_peer(chat_id)
            )
        )

        return True
