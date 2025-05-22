
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


class EditUserInfo(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``66B91B70``

    Parameters:
        user_id (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        message (``str``):
            N/A

        entities (List of :obj:`MessageEntity <pyrogram.raw.base.MessageEntity>`):
            N/A

    Returns:
        :obj:`help.UserInfo <pyrogram.raw.base.help.UserInfo>`
    """

    __slots__: List[str] = ["user_id", "message", "entities"]

    ID = 0x66b91b70
    QUALNAME = "functions.help.EditUserInfo"

    def __init__(self, *, user_id: "raw.base.InputUser", message: str, entities: List["raw.base.MessageEntity"]) -> None:
        self.user_id = user_id  # InputUser
        self.message = message  # string
        self.entities = entities  # Vector<MessageEntity>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "EditUserInfo":
        # No flags
        
        user_id = TLObject.read(b)
        
        message = String.read(b)
        
        entities = TLObject.read(b)
        
        return EditUserInfo(user_id=user_id, message=message, entities=entities)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(self.user_id.write())
        
        b.write(String(self.message))
        
        b.write(Vector(self.entities))
        
        return b.getvalue()
