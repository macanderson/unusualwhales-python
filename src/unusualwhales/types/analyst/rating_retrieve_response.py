# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

import datetime
from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["RatingRetrieveResponse", "Rating"]


class Rating(BaseModel):
    action: Optional[str] = None
    """The action taken (e.g., Initiated, Upgraded, Downgraded)."""

    analyst: Optional[str] = None

    date: Optional[datetime.date] = None

    price_target: Optional[float] = FieldInfo(alias="priceTarget", default=None)
    """The price target set by the analyst."""

    rating: Optional[str] = None
    """Analyst's rating (e.g., Buy, Hold, Sell)."""


class RatingRetrieveResponse(BaseModel):
    ratings: Optional[List[Rating]] = None

    symbol: Optional[str] = None
