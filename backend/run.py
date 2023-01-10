import uvicorn
from backend.core.config import settings

if __name__ == '__main__':
    uvicorn.run("backend.main:app", reload=settings.DEBUG, debug=settings.DEBUG)


def run_server():
    uvicorn.run("backend.main:app", reload=settings.DEBUG, debug=settings.DEBUG)