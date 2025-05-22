
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


class MessageActionPaymentSent(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.MessageAction`.

    Details:
        - Layer: ``166``
        - ID: ``96163F56``

    Parameters:
        currency (``str``):
            N/A

        total_amount (``int`` ``64-bit``):
            N/A

        recurring_init (``bool``, *optional*):
            N/A

        recurring_used (``bool``, *optional*):
            N/A

        invoice_slug (``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["currency", "total_amount", "recurring_init", "recurring_used", "invoice_slug"]

    ID = 0x96163f56
    QUALNAME = "types.MessageActionPaymentSent"

    def __init__(self, *, currency: str, total_amount: int, recurring_init: Optional[bool] = None, recurring_used: Optional[bool] = None, invoice_slug: Optional[str] = None) -> None:
        self.currency = currency  # string
        self.total_amount = total_amount  # long
        self.recurring_init = recurring_init  # flags.2?true
        self.recurring_used = recurring_used  # flags.3?true
        self.invoice_slug = invoice_slug  # flags.0?string

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "MessageActionPaymentSent":
        
        flags = Int.read(b)
        
        recurring_init = True if flags & (1 << 2) else False
        recurring_used = True if flags & (1 << 3) else False
        currency = String.read(b)
        
        total_amount = Long.read(b)
        
        invoice_slug = String.read(b) if flags & (1 << 0) else None
        return MessageActionPaymentSent(currency=currency, total_amount=total_amount, recurring_init=recurring_init, recurring_used=recurring_used, invoice_slug=invoice_slug)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 2) if self.recurring_init else 0
        flags |= (1 << 3) if self.recurring_used else 0
        flags |= (1 << 0) if self.invoice_slug is not None else 0
        b.write(Int(flags))
        
        b.write(String(self.currency))
        
        b.write(Long(self.total_amount))
        
        if self.invoice_slug is not None:
            b.write(String(self.invoice_slug))
        
        return b.getvalue()
