# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from ..._models import BaseModel

__all__ = ["HoldingListResponse", "Holding"]


class Holding(BaseModel):
    name: Optional[str] = None

    shares: Optional[float] = None

    symbol: Optional[str] = None

    weight: Optional[float] = None


class HoldingListResponse(BaseModel):
    etf: Optional[str] = None

    holdings: Optional[List[Holding]] = None
