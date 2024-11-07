# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ScreenerPostResponse", "Data"]


class Data(BaseModel):
    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    industry: Optional[str] = None

    market_cap: Optional[float] = FieldInfo(alias="marketCap", default=None)

    price: Optional[float] = None

    sector: Optional[str] = None

    symbol: Optional[str] = None

    volume: Optional[float] = None


class ScreenerPostResponse(BaseModel):
    data: Optional[List[Data]] = None
