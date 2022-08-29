import os
from datetime import datetime
import shutil
from typing import Union, List
from fastapi import UploadFile
import pydantic

from pathlib import Path
from fastapi.requests import Request

from app.utils import random_string
from app.core import config

def create_dir(path: str) -> bool:
  try:
    if not os.path.isdir(path):
      os.mkdir(path)
      return True
  except RuntimeError:
    return False
  except OSError:
    return False


def check_dir(path: pydantic.DirectoryPath):
  try:
    if not os.path.isdir(path):
      raise Exception("Directory not found")
    return True
  except RuntimeError:
    return False
  except OSError:
    return False


def remove_path(path: Union[List[pydantic.DirectoryPath], pydantic.DirectoryPath]) -> bool:

  try:
    if isinstance(path, list):
      for p in path:
        if Path(path).exists():
          Path(path).unlink()
          return True
        return False
    else:
      if Path(path).exists():
         Path(path).unlink()
         return True
      return False
  except RuntimeError:
    return False
  except OSError:
    return False


async def write_file_to_system(
  file_obj: UploadFile, 
  path: pydantic.DirectoryPath) -> Union[str, bool]:
  if check_dir(path):
    now = datetime.timestamp(datetime.now())
    ext: str = os.path.splitext(file_obj.filename)[1]
    ext = ext.lower()
    uuid_name: str = random_string.generate_uuid(True)
    filename: str = f"{now}{uuid_name}{ext}"
    with open(f"{path}/{filename}", "wb") as buffer:
      try:
        shutil.copyfileobj(file_obj.file, buffer)
        return filename
      except:
        raise Exception("Error while creating file")


async def create_file(media_obj:UploadFile) -> List[str]:
    new_media = await write_file_to_system(media_obj, config.settings.media_dir)
    return new_media
    



def get_base_url(request: Request) -> str:
  base_url = request.url.scheme.join("://").join(request.url.netloc)
  return base_url

def get_base_dir():
  return Path(__file__).resolve(strict=True).cwd()