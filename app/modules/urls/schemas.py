from pydantic import BaseModel


class CreateUrlSchema(BaseModel):
    long_url: str


class GetUrlSchema(BaseModel):
    short_url: str


class DeleteUrlSchema(BaseModel):
    short_url: str


class UrlSchema(BaseModel):
    short_url: str
    long_url: str
