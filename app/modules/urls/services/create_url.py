import secrets

from fastapi import Depends

from app.models import UrlModel
from app.modules.urls.repository import UrlRepository
from app.modules.urls.schemas import UrlSchema, CreateUrlSchema


class CreateUrlService:
    def __init__(self, repo: UrlRepository = Depends()):
        self.repo = repo

    async def execute(self, long_url: CreateUrlSchema) -> UrlModel:
        short_url = f"const.com/{secrets.token_urlsafe(5)}"
        url = UrlSchema(
            short_url=short_url,
            long_url=long_url.long_url,
        )
        return await self.repo.create(url)
