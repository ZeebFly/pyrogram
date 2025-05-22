
# # # # # # # # # # # # # # # # # # # # # # # #
#               !!! WARNING !!!               #
#          This is a generated file!          #
# All changes made in this file will be lost! #
# # # # # # # # # # # # # # # # # # # # # # # #

from typing import Union
from pyrogram import raw
from pyrogram.raw.core import TLObject

ChannelAdminLogEventAction = Union[raw.types.ChannelAdminLogEventActionChangeAbout, raw.types.ChannelAdminLogEventActionChangeAvailableReactions, raw.types.ChannelAdminLogEventActionChangeBackgroundEmoji, raw.types.ChannelAdminLogEventActionChangeColor, raw.types.ChannelAdminLogEventActionChangeHistoryTTL, raw.types.ChannelAdminLogEventActionChangeLinkedChat, raw.types.ChannelAdminLogEventActionChangeLocation, raw.types.ChannelAdminLogEventActionChangePhoto, raw.types.ChannelAdminLogEventActionChangeStickerSet, raw.types.ChannelAdminLogEventActionChangeTitle, raw.types.ChannelAdminLogEventActionChangeUsername, raw.types.ChannelAdminLogEventActionChangeUsernames, raw.types.ChannelAdminLogEventActionCreateTopic, raw.types.ChannelAdminLogEventActionDefaultBannedRights, raw.types.ChannelAdminLogEventActionDeleteMessage, raw.types.ChannelAdminLogEventActionDeleteTopic, raw.types.ChannelAdminLogEventActionDiscardGroupCall, raw.types.ChannelAdminLogEventActionEditMessage, raw.types.ChannelAdminLogEventActionEditTopic, raw.types.ChannelAdminLogEventActionExportedInviteDelete, raw.types.ChannelAdminLogEventActionExportedInviteEdit, raw.types.ChannelAdminLogEventActionExportedInviteRevoke, raw.types.ChannelAdminLogEventActionParticipantInvite, raw.types.ChannelAdminLogEventActionParticipantJoin, raw.types.ChannelAdminLogEventActionParticipantJoinByInvite, raw.types.ChannelAdminLogEventActionParticipantJoinByRequest, raw.types.ChannelAdminLogEventActionParticipantLeave, raw.types.ChannelAdminLogEventActionParticipantMute, raw.types.ChannelAdminLogEventActionParticipantToggleAdmin, raw.types.ChannelAdminLogEventActionParticipantToggleBan, raw.types.ChannelAdminLogEventActionParticipantUnmute, raw.types.ChannelAdminLogEventActionParticipantVolume, raw.types.ChannelAdminLogEventActionPinTopic, raw.types.ChannelAdminLogEventActionSendMessage, raw.types.ChannelAdminLogEventActionStartGroupCall, raw.types.ChannelAdminLogEventActionStopPoll, raw.types.ChannelAdminLogEventActionToggleAntiSpam, raw.types.ChannelAdminLogEventActionToggleForum, raw.types.ChannelAdminLogEventActionToggleGroupCallSetting, raw.types.ChannelAdminLogEventActionToggleInvites, raw.types.ChannelAdminLogEventActionToggleNoForwards, raw.types.ChannelAdminLogEventActionTogglePreHistoryHidden, raw.types.ChannelAdminLogEventActionToggleSignatures, raw.types.ChannelAdminLogEventActionToggleSlowMode, raw.types.ChannelAdminLogEventActionUpdatePinned]


# noinspection PyRedeclaration
class ChannelAdminLogEventAction:  # type: ignore
    """Telegram API base type.

    Constructors:
        This base type has 45 constructors available.

        .. currentmodule:: pyrogram.raw.types

        .. autosummary::
            :nosignatures:

            ChannelAdminLogEventActionChangeAbout
            ChannelAdminLogEventActionChangeAvailableReactions
            ChannelAdminLogEventActionChangeBackgroundEmoji
            ChannelAdminLogEventActionChangeColor
            ChannelAdminLogEventActionChangeHistoryTTL
            ChannelAdminLogEventActionChangeLinkedChat
            ChannelAdminLogEventActionChangeLocation
            ChannelAdminLogEventActionChangePhoto
            ChannelAdminLogEventActionChangeStickerSet
            ChannelAdminLogEventActionChangeTitle
            ChannelAdminLogEventActionChangeUsername
            ChannelAdminLogEventActionChangeUsernames
            ChannelAdminLogEventActionCreateTopic
            ChannelAdminLogEventActionDefaultBannedRights
            ChannelAdminLogEventActionDeleteMessage
            ChannelAdminLogEventActionDeleteTopic
            ChannelAdminLogEventActionDiscardGroupCall
            ChannelAdminLogEventActionEditMessage
            ChannelAdminLogEventActionEditTopic
            ChannelAdminLogEventActionExportedInviteDelete
            ChannelAdminLogEventActionExportedInviteEdit
            ChannelAdminLogEventActionExportedInviteRevoke
            ChannelAdminLogEventActionParticipantInvite
            ChannelAdminLogEventActionParticipantJoin
            ChannelAdminLogEventActionParticipantJoinByInvite
            ChannelAdminLogEventActionParticipantJoinByRequest
            ChannelAdminLogEventActionParticipantLeave
            ChannelAdminLogEventActionParticipantMute
            ChannelAdminLogEventActionParticipantToggleAdmin
            ChannelAdminLogEventActionParticipantToggleBan
            ChannelAdminLogEventActionParticipantUnmute
            ChannelAdminLogEventActionParticipantVolume
            ChannelAdminLogEventActionPinTopic
            ChannelAdminLogEventActionSendMessage
            ChannelAdminLogEventActionStartGroupCall
            ChannelAdminLogEventActionStopPoll
            ChannelAdminLogEventActionToggleAntiSpam
            ChannelAdminLogEventActionToggleForum
            ChannelAdminLogEventActionToggleGroupCallSetting
            ChannelAdminLogEventActionToggleInvites
            ChannelAdminLogEventActionToggleNoForwards
            ChannelAdminLogEventActionTogglePreHistoryHidden
            ChannelAdminLogEventActionToggleSignatures
            ChannelAdminLogEventActionToggleSlowMode
            ChannelAdminLogEventActionUpdatePinned
    """

    QUALNAME = "pyrogram.raw.base.ChannelAdminLogEventAction"

    def __init__(self):
        raise TypeError("Base types can only be used for type checking purposes: "
                        "you tried to use a base type instance as argument, "
                        "but you need to instantiate one of its constructors instead. "
                        "More info: https://docs.pyrogram.org/telegram/base/channel-admin-log-event-action")
