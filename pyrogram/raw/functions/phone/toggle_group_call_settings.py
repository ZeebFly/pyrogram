
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


class ToggleGroupCallSettings(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``74BBB43D``

    Parameters:
        call (:obj:`InputGroupCall <pyrogram.raw.base.InputGroupCall>`):
            N/A

        reset_invite_hash (``bool``, *optional*):
            N/A

        join_muted (``bool``, *optional*):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["call", "reset_invite_hash", "join_muted"]

    ID = 0x74bbb43d
    QUALNAME = "functions.phone.ToggleGroupCallSettings"

    def __init__(self, *, call: "raw.base.InputGroupCall", reset_invite_hash: Optional[bool] = None, join_muted: Optional[bool] = None) -> None:
        self.call = call  # InputGroupCall
        self.reset_invite_hash = reset_invite_hash  # flags.1?true
        self.join_muted = join_muted  # flags.0?Bool

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "ToggleGroupCallSettings":
        
        flags = Int.read(b)
        
        reset_invite_hash = True if flags & (1 << 1) else False
        call = TLObject.read(b)
        
        join_muted = Bool.read(b) if flags & (1 << 0) else None
        return ToggleGroupCallSettings(call=call, reset_invite_hash=reset_invite_hash, join_muted=join_muted)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 1) if self.reset_invite_hash else 0
        flags |= (1 << 0) if self.join_muted is not None else 0
        b.write(Int(flags))
        
        b.write(self.call.write())
        
        if self.join_muted is not None:
            b.write(Bool(self.join_muted))
        
        return b.getvalue()
