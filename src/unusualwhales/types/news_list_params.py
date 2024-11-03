# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["NewsListParams"]


class NewsListParams(TypedDict, total=False):
    symbols: str
    """Comma-separated list of stock symbols to filter news."""
