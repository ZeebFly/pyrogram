
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


class InputStorePaymentPremiumGiveaway(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.InputStorePaymentPurpose`.

    Details:
        - Layer: ``166``
        - ID: ``7C9375E6``

    Parameters:
        boost_peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        random_id (``int`` ``64-bit``):
            N/A

        until_date (``int`` ``32-bit``):
            N/A

        currency (``str``):
            N/A

        amount (``int`` ``64-bit``):
            N/A

        only_new_subscribers (``bool``, *optional*):
            N/A

        additional_peers (List of :obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

        countries_iso2 (List of ``str``, *optional*):
            N/A

    """

    __slots__: List[str] = ["boost_peer", "random_id", "until_date", "currency", "amount", "only_new_subscribers", "additional_peers", "countries_iso2"]

    ID = 0x7c9375e6
    QUALNAME = "types.InputStorePaymentPremiumGiveaway"

    def __init__(self, *, boost_peer: "raw.base.InputPeer", random_id: int, until_date: int, currency: str, amount: int, only_new_subscribers: Optional[bool] = None, additional_peers: Optional[List["raw.base.InputPeer"]] = None, countries_iso2: Optional[List[str]] = None) -> None:
        self.boost_peer = boost_peer  # InputPeer
        self.random_id = random_id  # long
        self.until_date = until_date  # int
        self.currency = currency  # string
        self.amount = amount  # long
        self.only_new_subscribers = only_new_subscribers  # flags.0?true
        self.additional_peers = additional_peers  # flags.1?Vector<InputPeer>
        self.countries_iso2 = countries_iso2  # flags.2?Vector<string>

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "InputStorePaymentPremiumGiveaway":
        
        flags = Int.read(b)
        
        only_new_subscribers = True if flags & (1 << 0) else False
        boost_peer = TLObject.read(b)
        
        additional_peers = TLObject.read(b) if flags & (1 << 1) else []
        
        countries_iso2 = TLObject.read(b, String) if flags & (1 << 2) else []
        
        random_id = Long.read(b)
        
        until_date = Int.read(b)
        
        currency = String.read(b)
        
        amount = Long.read(b)
        
        return InputStorePaymentPremiumGiveaway(boost_peer=boost_peer, random_id=random_id, until_date=until_date, currency=currency, amount=amount, only_new_subscribers=only_new_subscribers, additional_peers=additional_peers, countries_iso2=countries_iso2)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.only_new_subscribers else 0
        flags |= (1 << 1) if self.additional_peers else 0
        flags |= (1 << 2) if self.countries_iso2 else 0
        b.write(Int(flags))
        
        b.write(self.boost_peer.write())
        
        if self.additional_peers is not None:
            b.write(Vector(self.additional_peers))
        
        if self.countries_iso2 is not None:
            b.write(Vector(self.countries_iso2, String))
        
        b.write(Long(self.random_id))
        
        b.write(Int(self.until_date))
        
        b.write(String(self.currency))
        
        b.write(Long(self.amount))
        
        return b.getvalue()
