
from typing import Union

import pyrogram
from pyrogram import raw


class DeleteChannel:
    async def delete_channel(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> bool:
        """Delete a channel.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                The id of the channel to be deleted.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                await app.delete_channel(channel_id)
        """
        await self.invoke(
            raw.functions.channels.DeleteChannel(
                channel=await self.resolve_peer(chat_id)
            )
        )

        return True
