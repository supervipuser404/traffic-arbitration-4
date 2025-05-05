
from pydantic import BaseModel
from datetime import datetime
from typing import Optional


class ArticleBase(BaseModel):
    title: str
    content: str
    image_url: Optional[str] = None
    language: str = "ru"
    category_id: int
    author: Optional[str] = None
    source: Optional[str] = None
    is_top: bool = False


class ArticleCreate(ArticleBase):
    parent_id: Optional[int] = None


class Article(ArticleBase):
    id: int
    created_at: datetime
    parent_id: Optional[int] = None

    class Config:
        from_attributes = True


