# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["EarningRetrieveResponse", "Earning"]


class Earning(BaseModel):
    estimated_eps: Optional[float] = FieldInfo(alias="estimatedEPS", default=None)

    fiscal_date_ending: Optional[date] = FieldInfo(alias="fiscalDateEnding", default=None)

    reported_eps: Optional[float] = FieldInfo(alias="reportedEPS", default=None)

    surprise: Optional[float] = None

    surprise_percentage: Optional[float] = FieldInfo(alias="surprisePercentage", default=None)


class EarningRetrieveResponse(BaseModel):
    earnings: Optional[List[Earning]] = None

    symbol: Optional[str] = None
