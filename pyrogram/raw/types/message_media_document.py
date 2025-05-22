
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


class MessageMediaDocument(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageMedia`.

    Details:
        - Layer: ``166``
        - ID: ``4CF4D72D``

    Parameters:
        nopremium (``bool``, *optional*):
            N/A

        spoiler (``bool``, *optional*):
            N/A

        document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        alt_document (:obj:`Document <pyrogram.raw.base.Document>`, *optional*):
            N/A

        ttl_seconds (``int`` ``32-bit``, *optional*):
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

    __slots__: List[str] = ["nopremium", "spoiler", "document", "alt_document", "ttl_seconds"]

    ID = 0x4cf4d72d
    QUALNAME = "types.MessageMediaDocument"

    def __init__(self, *, nopremium: Optional[bool] = None, spoiler: Optional[bool] = None, document: "raw.base.Document" = None, alt_document: "raw.base.Document" = None, ttl_seconds: Optional[int] = None) -> None:
        self.nopremium = nopremium  # flags.3?true
        self.spoiler = spoiler  # flags.4?true
        self.document = document  # flags.0?Document
        self.alt_document = alt_document  # flags.5?Document
        self.ttl_seconds = ttl_seconds  # flags.2?int

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageMediaDocument":
        
        flags = Int.read(b)
        
        nopremium = True if flags & (1 << 3) else False
        spoiler = True if flags & (1 << 4) else False
        document = TLObject.read(b) if flags & (1 << 0) else None
        
        alt_document = TLObject.read(b) if flags & (1 << 5) else None
        
        ttl_seconds = Int.read(b) if flags & (1 << 2) else None
        return MessageMediaDocument(nopremium=nopremium, spoiler=spoiler, document=document, alt_document=alt_document, ttl_seconds=ttl_seconds)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 3) if self.nopremium else 0
        flags |= (1 << 4) if self.spoiler else 0
        flags |= (1 << 0) if self.document is not None else 0
        flags |= (1 << 5) if self.alt_document is not None else 0
        flags |= (1 << 2) if self.ttl_seconds is not None else 0
        b.write(Int(flags))
        
        if self.document is not None:
            b.write(self.document.write())
        
        if self.alt_document is not None:
            b.write(self.alt_document.write())
        
        if self.ttl_seconds is not None:
            b.write(Int(self.ttl_seconds))
        
        return b.getvalue()
