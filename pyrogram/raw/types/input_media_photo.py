
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


class InputMediaPhoto(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputMedia`.

    Details:
        - Layer: ``166``
        - ID: ``B3BA0635``

    Parameters:
        id (:obj:`InputPhoto <pyrogram.raw.base.InputPhoto>`):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["id", "spoiler", "ttl_seconds"]

    ID = 0xb3ba0635
    QUALNAME = "types.InputMediaPhoto"

    def __init__(self, *, id: "raw.base.InputPhoto", spoiler: Optional[bool] = None, ttl_seconds: Optional[int] = None) -> None:
        self.id = id  # InputPhoto
        self.spoiler = spoiler  # flags.1?true
        self.ttl_seconds = ttl_seconds  # flags.0?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputMediaPhoto":
        
        flags = Int.read(b)
        
        spoiler = True if flags & (1 << 1) else False
        id = TLObject.read(b)
        
        ttl_seconds = Int.read(b) if flags & (1 << 0) else None
        return InputMediaPhoto(id=id, spoiler=spoiler, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.spoiler else 0
        flags |= (1 << 0) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        b.write(self.id.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
