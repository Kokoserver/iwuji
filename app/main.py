from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware

from app.core.config import settings
from app.database import init_db, close_db
from app.src._base.schemas import HealthCheck
from app.src._base.router import v1  as version_1_router
def get_application():
    _app = FastAPI(
    title=settings.PROJECT_NAME, 
    version=settings.API_VERSION,
    openapi_url=f"{settings.API_PREFIX}/openapi.json",
    redoc_url=f"{settings.API_PREFIX}/redoc",
    docs_url=f"{settings.API_PREFIX}/docs",
     debug=settings.DEBUG
    )

    _app.add_middleware(
        CORSMiddleware,
        allow_origins=[str(origin) for origin in settings.BACKEND_CORS_ORIGINS],
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )

    return _app


app = get_application()
@app.on_event("startup")
async def startup():
   init_db(app)

@app.on_event("shutdown")
async def shutdown():
    await close_db()

@app.get("/", response_model=HealthCheck, tags=["status"])
def health_check():
    return {
        "name": settings.PROJECT_NAME,
        "version": settings.API_VERSION,
        "description": settings.PROJECT_DESCRIPTION,
    }
app.include_router(version_1_router.router, prefix=f"{settings.API_PREFIX}")