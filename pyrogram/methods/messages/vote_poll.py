
from typing import Union, List

import pyrogram
from pyrogram import raw
from pyrogram import types


class VotePoll:
    async def vote_poll(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: id,
        options: Union[int, List[int]]
    ) -> "types.Poll":
        """Vote a poll.

        .. include:: /_includes/usable-by/users.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Identifier of the original message with the poll.

            options (``Int`` | List of ``int``):
                Index or list of indexes (for multiple answers) of the poll option(s) you want to vote for (0 to 9).

        Returns:
            :obj:`~pyrogram.types.Poll` - On success, the poll with the chosen option is returned.

        Example:
            .. code-block:: python

                await app.vote_poll(chat_id, message_id, 6)
        """

        poll = (await self.get_messages(chat_id, message_id)).poll
        options = [options] if not isinstance(options, list) else options

        r = await self.invoke(
            raw.functions.messages.SendVote(
                peer=await self.resolve_peer(chat_id),
                msg_id=message_id,
                options=[poll.options[option].data for option in options]
            )
        )

        return types.Poll._parse(self, r.updates[0])
