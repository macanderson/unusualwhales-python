# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["OverviewRetrieveResponse", "Index"]


class Index(BaseModel):
    change: Optional[float] = None

    name: Optional[str] = None

    percent_change: Optional[float] = FieldInfo(alias="percentChange", default=None)

    price: Optional[float] = None

    symbol: Optional[str] = None


class OverviewRetrieveResponse(BaseModel):
    indices: Optional[List[Index]] = None

    market_status: Optional[str] = FieldInfo(alias="marketStatus", default=None)
    """Current market status (e.g., Open, Closed)."""

    timestamp: Optional[datetime] = None
