# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HistoricalRetrieveResponse", "Data"]


class Data(BaseModel):
    adjusted_close: Optional[float] = FieldInfo(alias="adjustedClose", default=None)

    close: Optional[float] = None

    date: Optional[datetime] = None

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    volume: Optional[int] = None


class HistoricalRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None

    symbol: Optional[str] = None
