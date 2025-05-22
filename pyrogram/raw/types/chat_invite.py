
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


class ChatInvite(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.ChatInvite`.

    Details:
        - Layer: ``166``
        - ID: ``CDE0EC40``

    Parameters:
        title (``str``):
            N/A

        photo (:obj:`Photo <pyrogram.raw.base.Photo>`):
            N/A

        participants_count (``int`` ``32-bit``):
            N/A

        color (``int`` ``32-bit``):
            N/A

        channel (``bool``, *optional*):
            N/A

        broadcast (``bool``, *optional*):
            N/A

        public (``bool``, *optional*):
            N/A

        megagroup (``bool``, *optional*):
            N/A

        request_needed (``bool``, *optional*):
            N/A

        verified (``bool``, *optional*):
            N/A

        scam (``bool``, *optional*):
            N/A

        fake (``bool``, *optional*):
            N/A

        about (``str``, *optional*):
            N/A

        participants (List of :obj:`User <pyrogram.raw.base.User>`, *optional*):
            N/A

    Functions:
        This object can be returned by 1 function.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            messages.CheckChatInvite
    """

    __slots__: List[str] = ["title", "photo", "participants_count", "color", "channel", "broadcast", "public", "megagroup", "request_needed", "verified", "scam", "fake", "about", "participants"]

    ID = 0xcde0ec40
    QUALNAME = "types.ChatInvite"

    def __init__(self, *, title: str, photo: "raw.base.Photo", participants_count: int, color: int, channel: Optional[bool] = None, broadcast: Optional[bool] = None, public: Optional[bool] = None, megagroup: Optional[bool] = None, request_needed: Optional[bool] = None, verified: Optional[bool] = None, scam: Optional[bool] = None, fake: Optional[bool] = None, about: Optional[str] = None, participants: Optional[List["raw.base.User"]] = None) -> None:
        self.title = title  # string
        self.photo = photo  # Photo
        self.participants_count = participants_count  # int
        self.color = color  # int
        self.channel = channel  # flags.0?true
        self.broadcast = broadcast  # flags.1?true
        self.public = public  # flags.2?true
        self.megagroup = megagroup  # flags.3?true
        self.request_needed = request_needed  # flags.6?true
        self.verified = verified  # flags.7?true
        self.scam = scam  # flags.8?true
        self.fake = fake  # flags.9?true
        self.about = about  # flags.5?string
        self.participants = participants  # flags.4?Vector<User>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ChatInvite":
        
        flags = Int.read(b)
        
        channel = True if flags & (1 << 0) else False
        broadcast = True if flags & (1 << 1) else False
        public = True if flags & (1 << 2) else False
        megagroup = True if flags & (1 << 3) else False
        request_needed = True if flags & (1 << 6) else False
        verified = True if flags & (1 << 7) else False
        scam = True if flags & (1 << 8) else False
        fake = True if flags & (1 << 9) else False
        title = String.read(b)
        
        about = String.read(b) if flags & (1 << 5) else None
        photo = TLObject.read(b)
        
        participants_count = Int.read(b)
        
        participants = TLObject.read(b) if flags & (1 << 4) else []
        
        color = Int.read(b)
        
        return ChatInvite(title=title, photo=photo, participants_count=participants_count, color=color, channel=channel, broadcast=broadcast, public=public, megagroup=megagroup, request_needed=request_needed, verified=verified, scam=scam, fake=fake, about=about, participants=participants)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.channel else 0
        flags |= (1 << 1) if self.broadcast else 0
        flags |= (1 << 2) if self.public else 0
        flags |= (1 << 3) if self.megagroup else 0
        flags |= (1 << 6) if self.request_needed else 0
        flags |= (1 << 7) if self.verified else 0
        flags |= (1 << 8) if self.scam else 0
        flags |= (1 << 9) if self.fake else 0
        flags |= (1 << 5) if self.about is not None else 0
        flags |= (1 << 4) if self.participants else 0
        b.write(Int(flags))
        
        b.write(String(self.title))
        
        if self.about is not None:
            b.write(String(self.about))
        
        b.write(self.photo.write())
        
        b.write(Int(self.participants_count))
        
        if self.participants is not None:
            b.write(Vector(self.participants))
        
        b.write(Int(self.color))
        
        return b.getvalue()
