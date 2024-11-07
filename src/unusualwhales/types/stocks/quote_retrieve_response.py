# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["QuoteRetrieveResponse"]


class QuoteRetrieveResponse(BaseModel):
    change: Optional[float] = None

    change_percent: Optional[float] = FieldInfo(alias="changePercent", default=None)

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    previous_close: Optional[float] = FieldInfo(alias="previousClose", default=None)

    price: Optional[float] = None

    symbol: Optional[str] = None

    timestamp: Optional[datetime] = None

    volume: Optional[int] = None
