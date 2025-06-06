
from typing import Union

import pyrogram
from pyrogram import raw


class BlockUser:
    async def block_user(
        self: "pyrogram.Client",
        user_id: Union[int, str]
    ) -> bool:
        """Block a user.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            user_id (``int`` | ``str``)::
                Unique identifier (int) or username (str) of the target user.
                For you yourself you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

        Returns:
            ``bool``: True on success

        Example:
            .. code-block:: python

                await app.block_user(user_id)
        """
        return bool(
            await self.invoke(
                raw.functions.contacts.Block(
                    id=await self.resolve_peer(user_id)
                )
            )
        )
