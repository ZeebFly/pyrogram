
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types


class GetBoostsStatus:
    async def get_boosts_status(
        self: "pyrogram.Client",
        chat_id: Union[int, str]
    ) -> bool:
        """Get boosts status of channel

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

        Returns:
            :obj:`~pyrogram.types.BoostsStatus`: On success.

        Example:
            .. code-block:: python

                # get boosts list
                app.get_boosts()
        """
        r = await self.invoke(
            raw.functions.premium.GetBoostsStatus(peer=await self.resolve_peer(chat_id))
        )

        return types.BoostsStatus._parse(r)
