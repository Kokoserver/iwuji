import logging
import os
from core import settings
from src.lib.utils import random_string
from datetime import datetime
import shutil
from typing import Union, List
from fastapi import UploadFile
import pydantic
from src.lib.utils import get_path
from pathlib import Path
from fastapi.requests import Request


logger = logging.getLogger()

logger.setLevel(logging.DEBUG)

# create file handler which logs messages with level INFO
file_handler = logging.FileHandler(f"{get_path.get_base_dir()}/logs/os_operation.log")

file_handler.setLevel(logging.INFO)

# create formatter and add it to the file handler
formatter = logging.Formatter("%(asctime)s - %(name)s - %(levelname)s - %(message)s")
file_handler.setFormatter(formatter)

# add the file handler to the logger
logger.addHandler(file_handler)


def create_dir(path: str) -> bool:
    try:
        if not os.path.isdir(path):
            os.mkdir(path)
            return True
    except Exception as e:
        logging.error(f"Error creating directory: {path}. Error message: {e}")
        return False


def check_dir(path: pydantic.DirectoryPath) -> bool:
    try:
        if os.path.isdir(path):
            return True
    except OSError:
        logger.error("Failed to create directory: %s", path)
        return False
    finally:
        return True


def remove_path(
    path: Union[List[pydantic.DirectoryPath], pydantic.DirectoryPath]
) -> bool:
    try:
        if isinstance(path, list):
            for p in path:
                if Path(p).exists():
                    Path(p).unlink()
                    logger.info(f"Removed directory {p}")
            return True
        else:
            if Path(path).exists():
                Path(path).unlink()
                logger.info(f"Removed directory {path}")
                return True
            return False
    except RuntimeError:
        logger.error("Runtime error occurred while removing directory.")
        return False
    except OSError:
        logger.error("OS error occurred while removing directory.")
        return False


def write_file_to_system(
    file_obj: UploadFile,
    path: pydantic.DirectoryPath,
    existing_name: str = None,
) -> str:
    if check_dir(path):
        if existing_name:
            file_path = f"{path}/{existing_name}"
        else:
            now = datetime.timestamp(datetime.now())
            ext: str = os.path.splitext(file_obj.filename)[1]
            ext = ext.lower()
            uuid_name: str = random_string.generate_uuid(True)
            filename: str = f"{now}{uuid_name}{ext}"
            file_path = f"{path}/{filename}"

        with open(file_path, "wb") as buffer:
            try:
                shutil.copyfileobj(file_obj.file, buffer)
                return file_path.split("/")[-1]
            except Exception as e:
                logger.error("Failed to write file to system: %s", e)
                raise Exception("Error while creating file")
    else:
        raise Exception("Failed to create directory")


def create_file(media_obj: UploadFile) -> List[str]:
    new_media = write_file_to_system(media_obj, settings.config.media_dir)
    return new_media


def get_base_url(request: Request) -> str:
    base_url = request.url.scheme.join("://").join(request.url.netloc)
    return base_url


def get_base_dir():
    return Path(__file__).resolve(strict=True).cwd()
