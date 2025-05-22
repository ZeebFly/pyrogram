
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import errors


class ToggleForumTopics:
    async def toggle_forum_topics(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        enabled: bool = False
    ) -> bool:
        """Enable or disable forum functionality in a supergroup.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            enabled (``bool``):
                The new status. Pass True to enable forum topics.

        Returns:
            ``bool``: True on success. False otherwise.

        Example:
            .. code-block:: python

                # Change status of topics to disabled
                await app.toggle_topics()

                # Change status of topics to enabled
                await app.toggle_topics(enabled=True)
        """
        try:
            r = await self.invoke(
                raw.functions.channels.ToggleForum(
                    channel=await self.resolve_peer(chat_id),
                    enabled=enabled
                )
            )

            return bool(r)
        except errors.RPCError:
            return False
