# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["StockRetrieveResponse", "SeasonalityData"]


class SeasonalityData(BaseModel):
    average_return: Optional[float] = FieldInfo(alias="averageReturn", default=None)
    """Average return during the period."""

    period: Optional[str] = None
    """The period identifier (e.g., month or week number)."""

    total_periods: Optional[int] = FieldInfo(alias="totalPeriods", default=None)
    """Total number of periods analyzed."""

    win_rate: Optional[float] = FieldInfo(alias="winRate", default=None)
    """Percentage of times the stock had a positive return during the period."""


class StockRetrieveResponse(BaseModel):
    seasonality_data: Optional[List[SeasonalityData]] = FieldInfo(alias="seasonalityData", default=None)

    symbol: Optional[str] = None

    time_frame: Optional[str] = FieldInfo(alias="timeFrame", default=None)
    """The time frame of the seasonality data."""
