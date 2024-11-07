# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["MoverListResponse", "Mover"]


class Mover(BaseModel):
    change: Optional[float] = None

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    percent_change: Optional[float] = FieldInfo(alias="percentChange", default=None)

    price: Optional[float] = None

    symbol: Optional[str] = None

    volume: Optional[int] = None


class MoverListResponse(BaseModel):
    movers: Optional[List[Mover]] = None

    type: Optional[str] = None
    """gainers or losers"""
