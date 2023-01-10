from typing import List
from fastapi import Request, UploadFile, File
from fastapi import HTTPException, status, APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from backend.core.config import settings
from backend.src.media import crud
from backend.src.media.models import Media

media = APIRouter(include_in_schema=False)


def iter_media(file_path: str, content_type: str) -> object:
    path = ""
    if content_type.split('/')[0] == 'image':
        path = f"{settings.MEDIA_DIR}/{file_path}"
    elif content_type.split('/')[0] == 'video':
        path = f"{settings.MEDIA_DIR}/{file_path}"
    elif content_type.split('/')[0] == 'application':
        path = f"{settings.PDF_MEDIA_DIR}/{file_path}"
    else:
        raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST,
                            detail="Invalid media type")
    with open(
            path,
            mode="rb",
            buffering=1024
    ) as file_obj:  #
        yield from file_obj


@media.get('/download/{uri}', name='media_file_download')
async def get_drive(uri: str) -> FileResponse:
    check_file = await Media.objects.filter(Media.alt == uri).first()
    if not check_file:
        raise HTTPException(status_code=404, detail='file Not found')
    return FileResponse(
        f"{settings.PDF_MEDIA_DIR}/{uri}",
        status_code=status.HTTP_200_OK,
        filename=uri
    )


@media.get('/{uri}', name=settings.URL_STATIC_PATH)
async def get_drive(uri: str) -> StreamingResponse:
    check_file = await Media.objects.filter(alt=uri).first()
    if not check_file:
        raise HTTPException(status_code=404, detail='file Not found')
    return StreamingResponse(
        iter_media(check_file.alt,
                   content_type=check_file.content_type),
        media_type=check_file.content_type
    )


@media.post('/upload')
async def upload_drive(
        request: Request, files: List[UploadFile] = File(None)
) -> list[Media]:
    create_file = await crud.upload(files, request)
    if create_file:
        return create_file
