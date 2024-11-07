# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["FinancialRetrieveResponse"]


class FinancialRetrieveResponse(BaseModel):
    period: Optional[str] = None

    statements: Optional[List[Dict[str, object]]] = None

    statement_type: Optional[str] = FieldInfo(alias="statementType", default=None)

    symbol: Optional[str] = None
