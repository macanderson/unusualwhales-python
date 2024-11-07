# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TradeListResponse", "Trade"]


class Trade(BaseModel):
    amount: Optional[str] = None

    disclosure_date: Optional[date] = FieldInfo(alias="disclosureDate", default=None)

    member: Optional[str] = None

    symbol: Optional[str] = None

    transaction_date: Optional[date] = FieldInfo(alias="transactionDate", default=None)

    transaction_type: Optional[Literal["Purchase", "Sale", "Exchange"]] = FieldInfo(
        alias="transactionType", default=None
    )


class TradeListResponse(BaseModel):
    trades: Optional[List[Trade]] = None
