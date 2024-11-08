# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["CompanyRetrieveResponse"]


class CompanyRetrieveResponse(BaseModel):
    address: Optional[str] = None

    ceo: Optional[str] = None

    company_name: Optional[str] = FieldInfo(alias="companyName", default=None)

    description: Optional[str] = None

    employees: Optional[int] = None

    industry: Optional[str] = None

    sector: Optional[str] = None

    symbol: Optional[str] = None

    website: Optional[str] = None
