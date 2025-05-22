
from typing import Union

import pyrogram
from pyrogram import raw


class SendReaction:
    async def send_reaction(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int = None,
        story_id: int = None,
        emoji: Union[int, str] = None,
        big: bool = False
    ) -> bool:
        """Send a reaction to a message.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.

            message_id (``int``):
                Identifier of the message.

            story_id (``int``):
                Identifier of the story.

            emoji (``int`` | ``str``, *optional*):
                Reaction emoji.
                Pass "" as emoji (default) to retract the reaction.

            big (``bool``, *optional*):
                Pass True to show a bigger and longer reaction.
                Defaults to False.

        Returns:
            ``bool``: On success, True is returned.

        Example:
            .. code-block:: python

                # Send a reaction
                await app.send_reaction(chat_id, message_id, "🔥")

                # Retract a reaction
                await app.send_reaction(chat_id, message_id)
        """
        if isinstance(emoji, int):
            emoji = [raw.types.ReactionCustomEmoji(document_id=emoji)]
        else:
            emoji = [raw.types.ReactionEmoji(emoticon=emoji)] if emoji else None

        if story_id:
            rpc = raw.functions.stories.SendReaction(
                peer=await self.resolve_peer(chat_id),
                story_id=story_id,
                reaction=emoji[0],
            )
        else:
            rpc = raw.functions.messages.SendReaction(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                reaction=emoji,
                big=big
            )

        await self.invoke(rpc)

        return True
