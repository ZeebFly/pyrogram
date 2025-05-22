
from io import BytesIO

from pyrogram.raw.core.primitives import Int, Long, Int128, Int256, Bool, Bytes, String, Double, Vector
from pyrogram.raw.core import TLObject
from pyrogram import raw
from typing import List, Optional, Any

# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #


class MessageMediaGiveaway(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``166``
        - ID: ``58260664``

    Parameters:
        channels (List of ``int`` ``64-bit``):
            N/A

        quantity (``int`` ``32-bit``):
            N/A

        months (``int`` ``32-bit``):
            N/A

        until_date (``int`` ``32-bit``):
            N/A

        only_new_subscribers (``bool``, *optional*):
            N/A

        countries_iso2 (List of ``str``, *optional*):
            N/A

    Functions:
        This object can be returned by 3 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.GetWebPagePreview
            messages.UploadMedia
            messages.UploadImportedMedia
    """

    __slots__: List[str] = ["channels", "quantity", "months", "until_date", "only_new_subscribers", "countries_iso2"]

    ID = 0x58260664
    QUALNAME = "types.MessageMediaGiveaway"

    def __init__(self, *, channels: List[int], quantity: int, months: int, until_date: int, only_new_subscribers: Optional[bool] = None, countries_iso2: Optional[List[str]] = None) -> None:
        self.channels = channels  # Vector<long>
        self.quantity = quantity  # int
        self.months = months  # int
        self.until_date = until_date  # int
        self.only_new_subscribers = only_new_subscribers  # flags.0?true
        self.countries_iso2 = countries_iso2  # flags.1?Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaGiveaway":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        channels = TLObject.read(b, Long)
        
        countries_iso2 = TLObject.read(b, String) if flags & (1 << 1) else []
        
        quantity = Int.read(b)
        
        months = Int.read(b)
        
        until_date = Int.read(b)
        
        return MessageMediaGiveaway(channels=channels, quantity=quantity, months=months, until_date=until_date, only_new_subscribers=only_new_subscribers, countries_iso2=countries_iso2)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 1) if self.countries_iso2 else 0
        b.write(Int(flags))
        
        b.write(Vector(self.channels, Long))
        
        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))
        
        b.write(Int(self.quantity))
        
        b.write(Int(self.months))
        
        b.write(Int(self.until_date))
        
        return b.getvalue()
