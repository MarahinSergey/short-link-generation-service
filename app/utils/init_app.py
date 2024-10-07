from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from starlette.responses import RedirectResponse

from app.modules.urls.router import router
from app.utils.logger import get_logger
from app.utils.openapi_config import config
from app.utils.settings import settings

logger = get_logger(__name__)


def init_app():
    app = FastAPI(
        title=config.title,
        description=config.description,
        contact=config.authors,
        docs_url=f"/{settings.PREFIX}/docs/",
        redoc_url=f"/{settings.PREFIX}/redoc",
        openapi_url=f"/{settings.PREFIX}/openapi.json"
    )
    app.add_middleware(
        CORSMiddleware,
        allow_origins=settings.ORIGINS,
        allow_credentials=True,
        allow_methods=["GET, PUT, DELETE"],
        allow_headers=["*"],
    )

    app.include_router(router)
    logger.info(f'app_version: {app.version}')

    @app.get("/", tags=['system'])
    async def read_main():
        response = {
            "app": app.title,
            "description": app.description,
            "version": app.version,
            "api": app.docs_url
        }
        logger.info(response)
        if settings.IN_DOCKER:
            return response
        return RedirectResponse(url=app.docs_url)

    return app
