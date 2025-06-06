
import io
import os
import re
from typing import Union

import pyrogram
from pyrogram import raw
from pyrogram import types
from pyrogram import utils
from pyrogram.file_id import FileType


class EditMessageMedia:
    async def edit_message_media(
        self: "pyrogram.Client",
        chat_id: Union[int, str],
        message_id: int,
        media: "types.InputMedia",
        invert_media: bool = None,
        reply_markup: "types.InlineKeyboardMarkup" = None,
        file_name: str = None
    ) -> "types.Message":
        """Edit animation, audio, document, photo or video messages.

        If a message is a part of a message album, then it can be edited only to a photo or a video. Otherwise, the
        message type can be changed arbitrarily.

        .. include:: /_includes/usable-by/users-bots.rst

        Parameters:
            chat_id (``int`` | ``str``):
                Unique identifier (int) or username (str) of the target chat.
                For your personal cloud (Saved Messages) you can simply use "me" or "self".
                For a contact that exists in your Telegram address book you can use his phone number (str).

            message_id (``int``):
                Message identifier in the chat specified in chat_id.

            media (:obj:`~pyrogram.types.InputMedia`):
                One of the InputMedia objects describing an animation, audio, document, photo or video.

            invert_media (``bool``, *optional*):
                Invert media.

            reply_markup (:obj:`~pyrogram.types.InlineKeyboardMarkup`, *optional*):
                An InlineKeyboardMarkup object.

            file_name (``str``, *optional*):
                File name of the media to be sent. Not applicable to photos.
                Defaults to file's path basename.

        Returns:
            :obj:`~pyrogram.types.Message`: On success, the edited message is returned.

        Example:
            .. code-block:: python

                from pyrogram.types import InputMediaPhoto, InputMediaVideo, InputMediaAudio

                # Replace the current media with a local photo
                await app.edit_message_media(chat_id, message_id,
                    InputMediaPhoto("new_photo.jpg"))

                # Replace the current media with a local video
                await app.edit_message_media(chat_id, message_id,
                    InputMediaVideo("new_video.mp4"))

                # Replace the current media with a local audio
                await app.edit_message_media(chat_id, message_id,
                    InputMediaAudio("new_audio.mp3"))
        """
        caption = media.caption
        parse_mode = media.parse_mode

        message, entities = None, None

        if caption is not None:
            message, entities = (await self.parser.parse(caption, parse_mode)).values()

        if isinstance(media, types.InputMediaPhoto):
            if isinstance(media.media, io.BytesIO) or os.path.isfile(media.media):
                uploaded_media = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=await self.resolve_peer(chat_id),
                        media=raw.types.InputMediaUploadedPhoto(
                            file=await self.save_file(media.media),
                            spoiler=media.has_spoiler
                        )
                    )
                )

                media = raw.types.InputMediaPhoto(
                    id=raw.types.InputPhoto(
                        id=uploaded_media.photo.id,
                        access_hash=uploaded_media.photo.access_hash,
                        file_reference=uploaded_media.photo.file_reference
                    ),
                    spoiler=media.has_spoiler
                )
            elif re.match("^https?://", media.media):
                media = raw.types.InputMediaPhotoExternal(
                    url=media.media,
                    spoiler=media.has_spoiler
                )
            else:
                media = utils.get_input_media_from_file_id(media.media, FileType.PHOTO, has_spoiler=media.has_spoiler)
        elif isinstance(media, types.InputMediaVideo):
            if isinstance(media.media, io.BytesIO) or os.path.isfile(media.media):
                uploaded_media = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=await self.resolve_peer(chat_id),
                        media=raw.types.InputMediaUploadedDocument(
                            mime_type=self.guess_mime_type(media.media) or "video/mp4",
                            thumb=await self.save_file(media.thumb),
                            spoiler=media.has_spoiler,
                            file=await self.save_file(media.media),
                            attributes=[
                                raw.types.DocumentAttributeVideo(
                                    supports_streaming=media.supports_streaming or None,
                                    duration=media.duration,
                                    w=media.width,
                                    h=media.height
                                ),
                                raw.types.DocumentAttributeFilename(
                                    file_name=file_name or os.path.basename(media.media)
                                )
                            ]
                        )
                    )
                )

                media = raw.types.InputMediaDocument(
                    id=raw.types.InputDocument(
                        id=uploaded_media.document.id,
                        access_hash=uploaded_media.document.access_hash,
                        file_reference=uploaded_media.document.file_reference
                    ),
                    spoiler=media.has_spoiler
                )
            elif re.match("^https?://", media.media):
                media = raw.types.InputMediaDocumentExternal(
                    url=media.media,
                    spoiler=media.has_spoiler
                )
            else:
                media = utils.get_input_media_from_file_id(media.media, FileType.VIDEO, has_spoiler=media.has_spoiler)
        elif isinstance(media, types.InputMediaAudio):
            if isinstance(media.media, io.BytesIO) or os.path.isfile(media.media):
                media = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=await self.resolve_peer(chat_id),
                        media=raw.types.InputMediaUploadedDocument(
                            mime_type=self.guess_mime_type(media.media) or "audio/mpeg",
                            thumb=await self.save_file(media.thumb),
                            file=await self.save_file(media.media),
                            attributes=[
                                raw.types.DocumentAttributeAudio(
                                    duration=media.duration,
                                    performer=media.performer,
                                    title=media.title
                                ),
                                raw.types.DocumentAttributeFilename(
                                    file_name=file_name or os.path.basename(media.media)
                                )
                            ]
                        )
                    )
                )

                media = raw.types.InputMediaDocument(
                    id=raw.types.InputDocument(
                        id=media.document.id,
                        access_hash=media.document.access_hash,
                        file_reference=media.document.file_reference
                    )
                )
            elif re.match("^https?://", media.media):
                media = raw.types.InputMediaDocumentExternal(
                    url=media.media
                )
            else:
                media = utils.get_input_media_from_file_id(media.media, FileType.AUDIO)
        elif isinstance(media, types.InputMediaAnimation):
            if isinstance(media.media, io.BytesIO) or os.path.isfile(media.media):
                uploaded_media = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=await self.resolve_peer(chat_id),
                        media=raw.types.InputMediaUploadedDocument(
                            mime_type=self.guess_mime_type(media.media) or "video/mp4",
                            thumb=await self.save_file(media.thumb),
                            spoiler=media.has_spoiler,
                            file=await self.save_file(media.media),
                            attributes=[
                                raw.types.DocumentAttributeVideo(
                                    supports_streaming=True,
                                    duration=media.duration,
                                    w=media.width,
                                    h=media.height
                                ),
                                raw.types.DocumentAttributeFilename(
                                    file_name=file_name or os.path.basename(media.media)
                                ),
                                raw.types.DocumentAttributeAnimated()
                            ]
                        )
                    )
                )

                media = raw.types.InputMediaDocument(
                    id=raw.types.InputDocument(
                        id=uploaded_media.document.id,
                        access_hash=uploaded_media.document.access_hash,
                        file_reference=uploaded_media.document.file_reference
                    ),
                    spoiler=media.has_spoiler
                )
            elif re.match("^https?://", media.media):
                media = raw.types.InputMediaDocumentExternal(
                    url=media.media,
                    spoiler=media.has_spoiler
                )
            else:
                media = utils.get_input_media_from_file_id(media.media, FileType.ANIMATION, has_spoiler=media.has_spoiler)
        elif isinstance(media, types.InputMediaDocument):
            if isinstance(media.media, io.BytesIO) or os.path.isfile(media.media):
                media = await self.invoke(
                    raw.functions.messages.UploadMedia(
                        peer=await self.resolve_peer(chat_id),
                        media=raw.types.InputMediaUploadedDocument(
                            mime_type=self.guess_mime_type(media.media) or "application/zip",
                            thumb=await self.save_file(media.thumb),
                            file=await self.save_file(media.media),
                            attributes=[
                                raw.types.DocumentAttributeFilename(
                                    file_name=file_name or os.path.basename(media.media)
                                )
                            ]
                        )
                    )
                )

                media = raw.types.InputMediaDocument(
                    id=raw.types.InputDocument(
                        id=media.document.id,
                        access_hash=media.document.access_hash,
                        file_reference=media.document.file_reference
                    )
                )
            elif re.match("^https?://", media.media):
                media = raw.types.InputMediaDocumentExternal(
                    url=media.media
                )
            else:
                media = utils.get_input_media_from_file_id(media.media, FileType.DOCUMENT)

        r = await self.invoke(
            raw.functions.messages.EditMessage(
                peer=await self.resolve_peer(chat_id),
                id=message_id,
                invert_media=invert_media,
                media=media,
                reply_markup=await reply_markup.write(self) if reply_markup else None,
                message=message,
                entities=entities
            )
        )

        for i in r.updates:
            if isinstance(i, (raw.types.UpdateEditMessage, raw.types.UpdateEditChannelMessage)):
                return await types.Message._parse(
                    self, i.message,
                    {i.id: i for i in r.users},
                    {i.id: i for i in r.chats}
                )
