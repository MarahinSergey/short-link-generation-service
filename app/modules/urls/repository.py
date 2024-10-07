from fastapi import Depends

from app.models import UrlModel
from app.modules.urls.schemas import UrlSchema
from app.utils.db_utils import DbUtils


class UrlRepository:
    def __init__(self, db_utils: DbUtils = Depends()) -> None:
        self.db_utils = db_utils

    async def get(self, short_url: str) -> UrlModel.long_url:
        url: UrlModel = self.db_utils.get_entity_by(
            [UrlModel.short_url == short_url],
            UrlModel,
        )
        return url.long_url

    async def create(self, entity: UrlSchema) -> UrlModel:
        return self.db_utils.create_entity(entity, UrlModel)

    async def delete(self, short_url: str):
        return self.db_utils.delete_entities_by(
            [UrlModel.short_url == short_url],
            UrlModel,
        )
