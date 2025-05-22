
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


class UpdateGroupCall(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.Update`.

    Details:
        - Layer: ``166``
        - ID: ``14B24500``

    Parameters:
        chat_id (``int`` ``64-bit``):
            N/A

        call (:obj:`GroupCall <pyrogram.raw.base.GroupCall>`):
            N/A

    """

    __slots__: List[str] = ["chat_id", "call"]

    ID = 0x14b24500
    QUALNAME = "types.UpdateGroupCall"

    def __init__(self, *, chat_id: int, call: "raw.base.GroupCall") -> None:
        self.chat_id = chat_id  # long
        self.call = call  # GroupCall

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "UpdateGroupCall":
        # No flags
        
        chat_id = Long.read(b)
        
        call = TLObject.read(b)
        
        return UpdateGroupCall(chat_id=chat_id, call=call)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Long(self.chat_id))
        
        b.write(self.call.write())
        
        return b.getvalue()
