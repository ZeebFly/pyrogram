
from pyrogram import raw
from ..object import Object


class Username(Object):
    """A Telegram user's or chat's username.

    Parameters:
        username (``str``):
            User's or chat's username.
        editable (``bool``, *optional*):
            True, if it's a basic username; False, if it's a collectible username.
        active (``bool``, *optional*):
            True, if the collectible username is active.
    """

    def __init__(self, *, username: str, editable: bool = None, active: bool = None):
        super().__init__(None)

        self.username = username
        self.editable = editable
        self.active = active

    @staticmethod
    def _parse(username: "raw.types.Username") -> "Username":
        return Username(
            username=username.username,
            editable=username.editable,
            active=username.active
        )
