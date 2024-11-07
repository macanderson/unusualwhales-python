# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["DividendRetrieveResponse", "Dividend"]


class Dividend(BaseModel):
    amount: Optional[float] = None

    declaration_date: Optional[date] = FieldInfo(alias="declarationDate", default=None)

    ex_dividend_date: Optional[date] = FieldInfo(alias="exDividendDate", default=None)

    payment_date: Optional[date] = FieldInfo(alias="paymentDate", default=None)

    record_date: Optional[date] = FieldInfo(alias="recordDate", default=None)


class DividendRetrieveResponse(BaseModel):
    dividends: Optional[List[Dividend]] = None

    symbol: Optional[str] = None
