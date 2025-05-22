
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

InputMedia = Union[raw.types.InputMediaContact, raw.types.InputMediaDice, raw.types.InputMediaDocument, raw.types.InputMediaDocumentExternal, raw.types.InputMediaEmpty, raw.types.InputMediaGame, raw.types.InputMediaGeoLive, raw.types.InputMediaGeoPoint, raw.types.InputMediaInvoice, raw.types.InputMediaPhoto, raw.types.InputMediaPhotoExternal, raw.types.InputMediaPoll, raw.types.InputMediaStory, raw.types.InputMediaUploadedDocument, raw.types.InputMediaUploadedPhoto, raw.types.InputMediaVenue, raw.types.InputMediaWebPage]


# noinspection PyRedeclaration
class InputMedia:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 17 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            InputMediaContact
            InputMediaDice
            InputMediaDocument
            InputMediaDocumentExternal
            InputMediaEmpty
            InputMediaGame
            InputMediaGeoLive
            InputMediaGeoPoint
            InputMediaInvoice
            InputMediaPhoto
            InputMediaPhotoExternal
            InputMediaPoll
            InputMediaStory
            InputMediaUploadedDocument
            InputMediaUploadedPhoto
            InputMediaVenue
            InputMediaWebPage
    """

    QUALNAME = "pyrogram.raw.base.InputMedia"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/input-media")
