
from pyrogram import raw
from ..object import Object


class InputReplyToMessage(Object):
    """Contains information about a target replied message.

    Parameters:
        reply_to_message_id (``int``, *optional*):
            ID of the original message you want to reply.

        message_thread_id (``int``, *optional*):
            Unique identifier for the target message thread (topic) of the forum.
            for forum supergroups only.
    """

    def __init__(
        self, *,
        reply_to_message_id: int = None,
        message_thread_id: int = None
    ):
        super().__init__()

        self.reply_to_message_id = reply_to_message_id
        self.message_thread_id = message_thread_id

    def write(self):
        if not any((self.reply_to_message_id, self.message_thread_id)):
            return None

        return raw.types.InputReplyToMessage(
            reply_to_msg_id=self.reply_to_message_id or message_thread_id,  # type: ignore[arg-type]
            top_msg_id=self.message_thread_id if self.reply_to_message_id else None,
        ).write()
