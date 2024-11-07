# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["SectorListResponse", "Sector"]


class Sector(BaseModel):
    change: Optional[float] = None

    percent_change: Optional[float] = FieldInfo(alias="percentChange", default=None)

    sector: Optional[str] = None


class SectorListResponse(BaseModel):
    sectors: Optional[List[Sector]] = None

    time_frame: Optional[str] = FieldInfo(alias="timeFrame", default=None)
