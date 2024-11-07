# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ContractRetrieveResponse", "OptionContract"]


class OptionContract(BaseModel):
    ask: Optional[float] = None

    bid: Optional[float] = None

    delta: Optional[float] = None

    expiration_date: Optional[date] = FieldInfo(alias="expirationDate", default=None)

    gamma: Optional[float] = None

    implied_volatility: Optional[float] = FieldInfo(alias="impliedVolatility", default=None)

    last_price: Optional[float] = FieldInfo(alias="lastPrice", default=None)

    open_interest: Optional[int] = FieldInfo(alias="openInterest", default=None)

    option_symbol: Optional[str] = FieldInfo(alias="optionSymbol", default=None)

    option_type: Optional[Literal["CALL", "PUT"]] = FieldInfo(alias="optionType", default=None)

    rho: Optional[float] = None

    strike_price: Optional[float] = FieldInfo(alias="strikePrice", default=None)

    symbol: Optional[str] = None

    theta: Optional[float] = None

    vega: Optional[float] = None

    volume: Optional[int] = None


class ContractRetrieveResponse(BaseModel):
    option_contract: Optional[OptionContract] = FieldInfo(alias="optionContract", default=None)
