
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


class GlobalPrivacySettings(TLObject):  # type: ignore
    """Telegram API type.

    Constructor of :obj:`~pyrogram.raw.base.GlobalPrivacySettings`.

    Details:
        - Layer: ``166``
        - ID: ``734C4CCB``

    Parameters:
        archive_and_mute_new_noncontact_peers (``bool``, *optional*):
            N/A

        keep_archived_unmuted (``bool``, *optional*):
            N/A

        keep_archived_folders (``bool``, *optional*):
            N/A

    Functions:
        This object can be returned by 2 functions.

        .. currentmodule:: pyrogram.raw.functions

        .. autosummary::
            :nosignatures:

            account.GetGlobalPrivacySettings
            account.SetGlobalPrivacySettings
    """

    __slots__: List[str] = ["archive_and_mute_new_noncontact_peers", "keep_archived_unmuted", "keep_archived_folders"]

    ID = 0x734c4ccb
    QUALNAME = "types.GlobalPrivacySettings"

    def __init__(self, *, archive_and_mute_new_noncontact_peers: Optional[bool] = None, keep_archived_unmuted: Optional[bool] = None, keep_archived_folders: Optional[bool] = None) -> None:
        self.archive_and_mute_new_noncontact_peers = archive_and_mute_new_noncontact_peers  # flags.0?true
        self.keep_archived_unmuted = keep_archived_unmuted  # flags.1?true
        self.keep_archived_folders = keep_archived_folders  # flags.2?true

    @staticmethod
    def read(b: BytesIO, *args: Any) -> "GlobalPrivacySettings":
        
        flags = Int.read(b)
        
        archive_and_mute_new_noncontact_peers = True if flags & (1 << 0) else False
        keep_archived_unmuted = True if flags & (1 << 1) else False
        keep_archived_folders = True if flags & (1 << 2) else False
        return GlobalPrivacySettings(archive_and_mute_new_noncontact_peers=archive_and_mute_new_noncontact_peers, keep_archived_unmuted=keep_archived_unmuted, keep_archived_folders=keep_archived_folders)

    def write(self, *args) -> bytes:
        b = BytesIO()
        b.write(Int(self.ID, False))

        flags = 0
        flags |= (1 << 0) if self.archive_and_mute_new_noncontact_peers else 0
        flags |= (1 << 1) if self.keep_archived_unmuted else 0
        flags |= (1 << 2) if self.keep_archived_folders else 0
        b.write(Int(flags))
        
        return b.getvalue()
