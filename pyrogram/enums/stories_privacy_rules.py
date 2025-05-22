
from enum import auto
from .auto_name import AutoName


class StoriesPrivacyRules(AutoName):
    """Stories privacy rules type enumeration used in :obj:`~pyrogram.method.SendStory`."""

    PUBLIC = auto()
    "Public stories"

    CONTACTS = auto()
    "Contacts only stories"

    CLOSE_FRIENDS = auto()
    "Close friends stories"

    SELECTED_USERS = auto()
    "Selected users stories"
