# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["NewsListResponse", "Article"]


class Article(BaseModel):
    published_at: Optional[datetime] = FieldInfo(alias="publishedAt", default=None)

    source: Optional[str] = None

    title: Optional[str] = None

    url: Optional[str] = None


class NewsListResponse(BaseModel):
    articles: Optional[List[Article]] = None
