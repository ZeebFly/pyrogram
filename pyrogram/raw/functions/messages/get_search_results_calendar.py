
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


class GetSearchResultsCalendar(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``49F0BDE9``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        filter (:obj:`MessagesFilter <pyrogram.raw.base.MessagesFilter>`):
            N/A

        offset_id (``int`` ``32-bit``):
            N/A

        offset_date (``int`` ``32-bit``):
            N/A

    Returns:
        :obj:`messages.SearchResultsCalendar <pyrogram.raw.base.messages.SearchResultsCalendar>`
    """

    __slots__: List[str] = ["peer", "filter", "offset_id", "offset_date"]

    ID = 0x49f0bde9
    QUALNAME = "functions.messages.GetSearchResultsCalendar"

    def __init__(self, *, peer: "raw.base.InputPeer", filter: "raw.base.MessagesFilter", offset_id: int, offset_date: int) -> None:
        self.peer = peer  # InputPeer
        self.filter = filter  # MessagesFilter
        self.offset_id = offset_id  # int
        self.offset_date = offset_date  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GetSearchResultsCalendar":
        # No flags
        
        peer = TLObject.read(b)
        
        filter = TLObject.read(b)
        
        offset_id = Int.read(b)
        
        offset_date = Int.read(b)
        
        return GetSearchResultsCalendar(peer=peer, filter=filter, offset_id=offset_id, offset_date=offset_date)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.peer.write())
        
        b.write(self.filter.write())
        
        b.write(Int(self.offset_id))
        
        b.write(Int(self.offset_date))
        
        return b.getvalue()
