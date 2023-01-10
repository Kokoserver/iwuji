import pathlib
import typing
from typing import Union, List
import pydantic
from fastapi import UploadFile, Request
from backend.utils import os_operation
from backend.core.config import settings
from backend.src.media.models import Media


async def save_media_to_db(media_name_list, media_url_list, media_type_list) -> Union[List[Media], bool]:
    try:
        media_objs: List[Media] = []
        for alt, url, content_type in zip(media_name_list, media_url_list, media_type_list):
            new_media: Media = await Media.objects.create(
                alt=alt,
                url=url,
                content_type=content_type
            )
            media_objs.append(new_media)
        if not len(media_objs) < 1:
            return media_objs
        return False
    except Exception as e:
        print(e, "error")


async def remove_media_from_db(media_obj: Media) -> bool:
    old_media: Media = await Media.objects.get_or_none(pk=media_obj.id)
    if not old_media:
        return False
    await old_media.delete()
    return True


def convert_image_name_to_url(image_url: str, request: Request) -> str:
    image_full_url = f"{request.url_for(settings.URL_STATIC_PATH, uri=image_url)}"
    return image_full_url


async def upload(media_objs: List[UploadFile], request: Request, is_pdf=False) -> typing.Union[list[Media], bool]:
    if media_objs:
        media_name_list: List[str] = []
        media_type_list = []
        media_url_list = []
        for media in media_objs:
            if media and media.filename:
                media_type_list.append(media.content_type)
                if is_pdf:
                    media_name = await os_operation.write_file_to_system(media, settings.PDF_MEDIA_DIR)
                else:
                    media_name = await os_operation.write_file_to_system(media, settings.MEDIA_DIR)
                media_name_list.append(media_name)
        media_url_list = [
            convert_image_name_to_url(img_name, request)
            for img_name in media_name_list if img_name
        ]
        new_media_list = await save_media_to_db(
            media_name_list, media_url_list, media_type_list
        )
        return new_media_list
    return False


async def update(media_objs: List[UploadFile], old_medias: Union[List[Media], Media], request: Request,
                 is_pdf: bool = False) -> Union[List[Media], bool]:
    if is_pdf:
        base_path: pydantic.DirectoryPath = settings.PDF_MEDIA_DIR
    else:
        base_path: pydantic.DirectoryPath = settings.MEDIA_DIR
    deleted_media_list = []
    for media in old_medias:
        if media:
            get_media_obj: Media = await Media.objects.filter(pk=media.id).first()
            if get_media_obj:

                await get_media_obj.delete()
                _ = os_operation.remove_path(f"{base_path}/{get_media_obj.alt}")
    new_media_list: List[Media] = await upload(media_objs, request, is_pdf=is_pdf)
    if new_media_list:
        return new_media_list
    return []


async def delete(old_medias: List[Media], is_pdf: bool = False) -> bool:
    if is_pdf:
        base_path: pydantic.DirectoryPath = settings.PDF_MEDIA_DIR
    else:
        base_path: pydantic.DirectoryPath = settings.MEDIA_DIR
    for media in old_medias:
        if media:
            get_media_obj: Media = await Media.objects.get_or_none(id=media.id)
            if get_media_obj:
                await get_media_obj.delete()
                os_operation.remove_path(f"{base_path}/{get_media_obj.alt}")
