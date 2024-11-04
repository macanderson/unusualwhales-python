# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ChainRetrieveResponse", "Option"]


class Option(BaseModel):
    ask: Optional[float] = None

    bid: Optional[float] = None

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    last_price: Optional[float] = FieldInfo(alias="lastPrice", default=None)

    open_interest: Optional[int] = FieldInfo(alias="openInterest", default=None)

    option_type: Optional[Literal["CALL", "PUT"]] = FieldInfo(alias="optionType", default=None)

    strike_price: Optional[float] = FieldInfo(alias="strikePrice", default=None)

    symbol: Optional[str] = None

    volume: Optional[int] = None


class ChainRetrieveResponse(BaseModel):
    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    options: Optional[List[Option]] = None

    symbol: Optional[str] = None
