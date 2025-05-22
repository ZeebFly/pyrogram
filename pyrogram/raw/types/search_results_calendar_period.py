
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


class SearchResultsCalendarPeriod(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.SearchResultsCalendarPeriod`.

    Details:
        - Layer: ``166``
        - ID: ``C9B0539F``

    Parameters:
        date (``int`` ``32-bit``):
            N/A

        min_msg_id (``int`` ``32-bit``):
            N/A

        max_msg_id (``int`` ``32-bit``):
            N/A

        count (``int`` ``32-bit``):
            N/A

    """

    __slots__: List[str] = ["date", "min_msg_id", "max_msg_id", "count"]

    ID = 0xc9b0539f
    QUALNAME = "types.SearchResultsCalendarPeriod"

    def __init__(self, *, date: int, min_msg_id: int, max_msg_id: int, count: int) -> None:
        self.date = date  # int
        self.min_msg_id = min_msg_id  # int
        self.max_msg_id = max_msg_id  # int
        self.count = count  # int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "SearchResultsCalendarPeriod":
        # No flags
        
        date = Int.read(b)
        
        min_msg_id = Int.read(b)
        
        max_msg_id = Int.read(b)
        
        count = Int.read(b)
        
        return SearchResultsCalendarPeriod(date=date, min_msg_id=min_msg_id, max_msg_id=max_msg_id, count=count)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Int(self.date))
        
        b.write(Int(self.min_msg_id))
        
        b.write(Int(self.max_msg_id))
        
        b.write(Int(self.count))
        
        return b.getvalue()
