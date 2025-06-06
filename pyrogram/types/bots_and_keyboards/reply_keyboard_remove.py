
import pyrogram
from pyrogram import raw
from ..object import Object


class ReplyKeyboardRemove(Object):
    """Object used to tell clients to remove a bot keyboard.

    Upon receiving a message with this object, Telegram clients will remove the current custom keyboard and display
    the default letter-keyboard. By default, custom keyboards are displayed until a new keyboard is sent by a bot.
    An exception is made for one-time keyboards that are hidden immediately after the user presses a button
    (see ReplyKeyboardMarkup).

    Parameters:
        selective (``bool``, *optional*):
            Use this parameter if you want to remove the keyboard for specific users only. Targets:
            1) users that are @mentioned in the text of the Message object;
            2) if the bot's message is a reply (has reply_to_message_id), sender of the original message.
            Example: A user votes in a poll, bot returns confirmation message in reply to the vote and removes the
            keyboard for that user, while still showing the keyboard with poll options to users who haven't voted yet.
    """

    def __init__(
        self,
        selective: bool = None
    ):
        super().__init__()

        self.selective = selective

    @staticmethod
    def read(b):
        return ReplyKeyboardRemove(
            selective=b.selective
        )

    async def write(self, _: "pyrogram.Client"):
        return raw.types.ReplyKeyboardHide(
            selective=self.selective or None
        )
