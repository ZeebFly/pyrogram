
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


class DocumentAttributeVideo(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.DocumentAttribute`.

    Details:
        - Layer: ``166``
        - ID: ``D38FF1C2``

    Parameters:
        duration (``float`` ``64-bit``):
            N/A

        w (``int`` ``32-bit``):
            N/A

        h (``int`` ``32-bit``):
            N/A

        round_message (``bool``, *optional*):
            N/A

        supports_streaming (``bool``, *optional*):
            N/A

        nosound (``bool``, *optional*):
            N/A

        preload_prefix_size (``int`` ``32-bit``, *optional*):
            N/A

    """

    __slots__: List[str] = ["duration", "w", "h", "round_message", "supports_streaming", "nosound", "preload_prefix_size"]

    ID = 0xd38ff1c2
    QUALNAME = "types.DocumentAttributeVideo"

    def __init__(self, *, duration: float, w: int, h: int, round_message: Optional[bool] = None, supports_streaming: Optional[bool] = None, nosound: Optional[bool] = None, preload_prefix_size: Optional[int] = None) -> None:
        self.duration = duration  # double
        self.w = w  # int
        self.h = h  # int
        self.round_message = round_message  # flags.0?true
        self.supports_streaming = supports_streaming  # flags.1?true
        self.nosound = nosound  # flags.3?true
        self.preload_prefix_size = preload_prefix_size  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "DocumentAttributeVideo":
        
        flags = Int.read(b)
        
        round_message = True if flags & (1 << 0) else False
        supports_streaming = True if flags & (1 << 1) else False
        nosound = True if flags & (1 << 3) else False
        duration = Double.read(b)
        
        w = Int.read(b)
        
        h = Int.read(b)
        
        preload_prefix_size = Int.read(b) if flags & (1 << 2) else None
        return DocumentAttributeVideo(duration=duration, w=w, h=h, round_message=round_message, supports_streaming=supports_streaming, nosound=nosound, preload_prefix_size=preload_prefix_size)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.round_message else 0
        flags |= (1 << 1) if self.supports_streaming else 0
        flags |= (1 << 3) if self.nosound else 0
        flags |= (1 << 2) if self.preload_prefix_size is not None else 0
        b.write(Int(flags))
        
        b.write(Double(self.duration))
        
        b.write(Int(self.w))
        
        b.write(Int(self.h))
        
        if self.preload_prefix_size is not None:
            b.write(Int(self.preload_prefix_size))
        
        return b.getvalue()
