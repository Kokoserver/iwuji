from typing import List
from fastapi import Request, UploadFile, File
from fastapi import HTTPException, status, APIRouter
from fastapi.responses import FileResponse, StreamingResponse
from app.core.config import settings
from app.src.media import crud 
from app.src.media.models import Media

media = APIRouter(include_in_schema=True)


def iterMedia(file_path:str, content_type:str):
  path = ""
  if content_type.split('/')[0] == 'image':
    path = f"{settings.MEDIA_DIR}/{file_path}"
  elif content_type.split('/')[0] == 'video':
    path = f"{settings.MEDIA_DIR}/{file_path}"
  elif content_type.split('/')[0] == 'application':
    path = f"{settings.PDF_MEDIA_DIR}/{file_path}"
  else: raise HTTPException(status_code=status.HTTP_400_BAD_REQUEST, detail="Invalid media type")
  with open(
     path,
      mode="rb",
      buffering=1024
  ) as fileobj:  #
    yield from fileobj


@media.get('/download/{uri}', name='media_file_download')
async def get_drive(uri: str) -> FileResponse:
  check_file = await Media.filter(Media.alt==uri).first()
  if not check_file:
    raise HTTPException(status_code=404, detail='file Not found')
  return FileResponse(
      f"{settings.MEDIA_DIR}/{uri}",
      status_code=status.HTTP_200_OK,
      filename=uri
  )


@media.get('/{uri}', name=settings.URL_STATIC_PATH)
async def get_drive(uri: str) -> FileResponse:
  
  check_file = await Media.filter(alt=uri).first()
  if not check_file:
    raise HTTPException(status_code=404, detail='file Not found')
  return StreamingResponse(
      iterMedia(check_file.alt, content_type=check_file.content_type), media_type=check_file.content_type
  )


@media.post('/upload')
async def upload_drive(
    request: Request, files:List[UploadFile] = File(None)
) -> List[int]:
  create_file = await crud.upload(files, request)
  if (create_file):
    return create_file