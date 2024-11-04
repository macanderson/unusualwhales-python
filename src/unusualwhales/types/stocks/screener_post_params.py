# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Literal, TypedDict

__all__ = ["ScreenerPostParams", "Criterion"]


class ScreenerPostParams(TypedDict, total=False):
    criteria: Iterable[Criterion]


class Criterion(TypedDict, total=False):
    field: str
    """The field to apply the criterion on."""

    operator: Literal["eq", "neq", "gt", "gte", "lt", "lte", "in", "nin"]
    """The comparison operator."""

    value: str
    """The value to compare the field against."""
