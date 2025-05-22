
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


class RequestWebView(TLObject):  # type: ignore
    """Telegram API function.

    Details:
        - Layer: ``166``
        - ID: ``269DC2C1``

    Parameters:
        peer (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`):
            N/A

        bot (:obj:`InputUser <pyrogram.raw.base.InputUser>`):
            N/A

        platform (``str``):
            N/A

        from_bot_menu (``bool``, *optional*):
            N/A

        silent (``bool``, *optional*):
            N/A

        url (``str``, *optional*):
            N/A

        start_param (``str``, *optional*):
            N/A

        theme_params (:obj:`DataJSON <pyrogram.raw.base.DataJSON>`, *optional*):
            N/A

        reply_to (:obj:`InputReplyTo <pyrogram.raw.base.InputReplyTo>`, *optional*):
            N/A

        send_as (:obj:`InputPeer <pyrogram.raw.base.InputPeer>`, *optional*):
            N/A

    Returns:
        :obj:`WebViewResult <pyrogram.raw.base.WebViewResult>`
    """

    __slots__: List[str] = ["peer", "bot", "platform", "from_bot_menu", "silent", "url", "start_param", "theme_params", "reply_to", "send_as"]

    ID = 0x269dc2c1
    QUALNAME = "functions.messages.RequestWebView"

    def __init__(self, *, peer: "raw.base.InputPeer", bot: "raw.base.InputUser", platform: str, from_bot_menu: Optional[bool] = None, silent: Optional[bool] = None, url: Optional[str] = None, start_param: Optional[str] = None, theme_params: "raw.base.DataJSON" = None, reply_to: "raw.base.InputReplyTo" = None, send_as: "raw.base.InputPeer" = None) -> None:
        self.peer = peer  # InputPeer
        self.bot = bot  # InputUser
        self.platform = platform  # string
        self.from_bot_menu = from_bot_menu  # flags.4?true
        self.silent = silent  # flags.5?true
        self.url = url  # flags.1?string
        self.start_param = start_param  # flags.3?string
        self.theme_params = theme_params  # flags.2?DataJSON
        self.reply_to = reply_to  # flags.0?InputReplyTo
        self.send_as = send_as  # flags.13?InputPeer

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "RequestWebView":
        
        flags = Int.read(b)
        
        from_bot_menu = True if flags & (1 << 4) else False
        silent = True if flags & (1 << 5) else False
        peer = TLObject.read(b)
        
        bot = TLObject.read(b)
        
        url = String.read(b) if flags & (1 << 1) else None
        start_param = String.read(b) if flags & (1 << 3) else None
        theme_params = TLObject.read(b) if flags & (1 << 2) else None
        
        platform = String.read(b)
        
        reply_to = TLObject.read(b) if flags & (1 << 0) else None
        
        send_as = TLObject.read(b) if flags & (1 << 13) else None
        
        return RequestWebView(peer=peer, bot=bot, platform=platform, from_bot_menu=from_bot_menu, silent=silent, url=url, start_param=start_param, theme_params=theme_params, reply_to=reply_to, send_as=send_as)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 4) if self.from_bot_menu else 0
        flags |= (1 << 5) if self.silent else 0
        flags |= (1 << 1) if self.url is not None else 0
        flags |= (1 << 3) if self.start_param is not None else 0
        flags |= (1 << 2) if self.theme_params is not None else 0
        flags |= (1 << 0) if self.reply_to is not None else 0
        flags |= (1 << 13) if self.send_as is not None else 0
        b.write(Int(flags))
        
        b.write(self.peer.write())
        
        b.write(self.bot.write())
        
        if self.url is not None:
            b.write(String(self.url))
        
        if self.start_param is not None:
            b.write(String(self.start_param))
        
        if self.theme_params is not None:
            b.write(self.theme_params.write())
        
        b.write(String(self.platform))
        
        if self.reply_to is not None:
            b.write(self.reply_to.write())
        
        if self.send_as is not None:
            b.write(self.send_as.write())
        
        return b.getvalue()
