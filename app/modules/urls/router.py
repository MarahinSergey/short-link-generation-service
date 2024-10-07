from fastapi import APIRouter, Depends
from starlette import status

from app.dependencies.authorization import validate_token
from app.modules.urls.schemas import CreateUrlSchema, GetUrlSchema, DeleteUrlSchema, UrlSchema
from app.modules.urls.services.create_url import CreateUrlService
from app.modules.urls.services.delete_url import DeleteUrlService
from app.modules.urls.services.get_url import GetUrlService
from app.utils.settings import settings

router = APIRouter(
    prefix=f"/{settings.PREFIX}/urls",
    tags=["Urls"],
    dependencies=[Depends(validate_token)],
)


@router.get(
    "/",
    status_code=status.HTTP_200_OK,
    description="Получение полного url (на вход короткий url, в ответ полный url)"
)
async def get_long_url(
        body: GetUrlSchema = Depends(),
        service: GetUrlService = Depends(),
) -> str:
    return await service.execute(body)


@router.post(
    "/",
    status_code=status.HTTP_201_CREATED,
    description="Создание короткой ссылки (на вход передаём полный url, в ответ получаем короткий url)"
)
async def create_short_url(
        body: CreateUrlSchema = Depends(),
        service: CreateUrlService = Depends(),
) -> UrlSchema:
    return await service.execute(body)


@router.delete(
    "/",
    status_code=status.HTTP_204_NO_CONTENT,
    description="Удаление ссылки (на вход ранее сгенерированный короткий url, ответ статус  операции)"
)
async def delete_url(
        body: DeleteUrlSchema = Depends(),
        service: DeleteUrlService = Depends(),
):
    return await service.execute(body)
