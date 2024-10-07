from fastapi import Depends

from app.modules.urls.repository import UrlRepository
from app.modules.urls.schemas import GetUrlSchema


class GetUrlService:
    def __init__(self, repo: UrlRepository = Depends()):
        self.repo = repo

    async def execute(self, url: GetUrlSchema) -> str:
        return await self.repo.get(url.short_url)
