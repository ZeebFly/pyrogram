
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


class AssignAppStoreTransaction(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``80ED747D``

    Parameters:
        receipt (``bytes``):
            N/A

        purpose (:obj:`InputStorePaymentPurpose <pyrogram.raw.base.InputStorePaymentPurpose>`):
            N/A

    Returns:
        :obj:`Updates <pyrogram.raw.base.Updates>`
    """

    __slots__: List[str] = ["receipt", "purpose"]

    ID = 0x80ed747d
    QUALNAME = "functions.payments.AssignAppStoreTransaction"

    def __init__(self, *, receipt: bytes, purpose: "raw.base.InputStorePaymentPurpose") -> None:
        self.receipt = receipt  # bytes
        self.purpose = purpose  # InputStorePaymentPurpose

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "AssignAppStoreTransaction":
        # No flags
        
        receipt = Bytes.read(b)
        
        purpose = TLObject.read(b)
        
        return AssignAppStoreTransaction(receipt=receipt, purpose=purpose)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        # No flags
        
        b.write(Bytes(self.receipt))
        
        b.write(self.purpose.write())
        
        return b.getvalue()
