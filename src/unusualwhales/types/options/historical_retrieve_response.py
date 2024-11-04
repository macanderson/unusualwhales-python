# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["HistoricalRetrieveResponse", "Data"]


class Data(BaseModel):
    close: Optional[float] = None

    date: Optional[datetime.date] = None

    expiration_date: Optional[datetime.date] = FieldInfo(alias="expirationDate", default=None)

    high: Optional[float] = None

    low: Optional[float] = None

    open: Optional[float] = None

    open_interest: Optional[int] = FieldInfo(alias="openInterest", default=None)

    option_type: Optional[Literal["CALL", "PUT"]] = FieldInfo(alias="optionType", default=None)

    strike_price: Optional[float] = FieldInfo(alias="strikePrice", default=None)

    symbol: Optional[str] = None

    volume: Optional[int] = None


class HistoricalRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None

    symbol: Optional[str] = None
