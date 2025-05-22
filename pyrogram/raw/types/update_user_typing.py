
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


class UpdateUserTyping(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``166``
        - ID: ``C01E857F``

    Parameters:
        user_id (``int`` ``64-bit``):
            N/A

        action (:obj:`SendMessageAction <pyrogram.raw.base.SendMessageAction>`):
            N/A

    """

    __slots__: List[str] = ["user_id", "action"]

    ID = 0xc01e857f
    QUALNAME = "types.UpdateUserTyping"

    def __init__(self, *, user_id: int, action: "raw.base.SendMessageAction") -> None:
        self.user_id = user_id  # long
        self.action = action  # SendMessageAction

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateUserTyping":
        # No flags
        
        user_id = Long.read(b)
        
        action = TLObject.read(b)
        
        return UpdateUserTyping(user_id=user_id, action=action)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.user_id))
        
        b.write(self.action.write())
        
        return b.getvalue()
