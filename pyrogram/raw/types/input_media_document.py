
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


class InputMediaDocument(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``166``
        - ID: ``33473058``

    Parameters:
        id (:obj:`InputDocument <pyrogram.raw.base.InputDocument>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

        query (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "spoiler", "ttl_seconds", "query"]

    ID = 0x33473058
    QUALNAME = "types.InputMediaDocument"

    def __init__(self, *, id: "raw.base.InputDocument", spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None, query: Optional[str] = None) -> None:
        self.id = id  # InputDocument
        self.spoiler = spoiler  # flags.2?true
        self.ttl_seconds = ttl_seconds  # flags.0?int
        self.query = query  # flags.1?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaDocument":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 2) else False
        id = TLObject.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        query = String.read(b) if flags & (1 << 1) else None
        return InputMediaDocument(id=id, spoiler=spoiler, ttl_seconds=ttl_seconds, query=query)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.spoiler else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        flags |= (1 << 1) if self.query is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        if self.query is not None:
            b.write(String(self.query))
        
        return b.getvalue()
