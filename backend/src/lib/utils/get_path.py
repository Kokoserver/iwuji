from pathlib import Path


def get_base_dir():
    return Path(__file__).resolve(strict=True).cwd()


def get_template_dir():
    return f"{get_base_dir()}/templates"


def get_static_file_dir():
    return f"{get_base_dir()}/static"


def get_media_file_dir():
    return f"{get_base_dir()}/static/medias"


def get_pdf_file_dir():
    return f"{get_base_dir()}/static/pdf"
