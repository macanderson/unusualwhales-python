# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

from ..._models import BaseModel

__all__ = ["TransactionRetrieveResponse", "Data"]


class Data(BaseModel):
    exchange: Optional[str] = None

    price: Optional[float] = None

    size: Optional[int] = None

    symbol: Optional[str] = None

    timestamp: Optional[datetime] = None


class TransactionRetrieveResponse(BaseModel):
    data: Optional[List[Data]] = None
