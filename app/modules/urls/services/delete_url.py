from fastapi import Depends

from app.modules.urls.repository import UrlRepository
from app.modules.urls.schemas import DeleteUrlSchema


class DeleteUrlService:
    def __init__(self, repo: UrlRepository = Depends()):
        self.repo = repo

    async def execute(self, url: DeleteUrlSchema):
        return await self.repo.delete(url.short_url)
