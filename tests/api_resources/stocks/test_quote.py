# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unusualwhales import Unusualwhales, AsyncUnusualwhales
from unusualwhales.types.stocks import QuoteRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestQuote:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unusualwhales) -> None:
        quote = client.stocks.quote.retrieve(
            "symbol",
        )
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unusualwhales) -> None:
        response = client.stocks.quote.with_raw_response.retrieve(
            "symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = response.parse()
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unusualwhales) -> None:
        with client.stocks.quote.with_streaming_response.retrieve(
            "symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = response.parse()
            assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve(self, client: Unusualwhales) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            client.stocks.quote.with_raw_response.retrieve(
                "",
            )


class TestAsyncQuote:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        quote = await async_client.stocks.quote.retrieve(
            "symbol",
        )
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        response = await async_client.stocks.quote.with_raw_response.retrieve(
            "symbol",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        quote = await response.parse()
        assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        async with async_client.stocks.quote.with_streaming_response.retrieve(
            "symbol",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            quote = await response.parse()
            assert_matches_type(QuoteRetrieveResponse, quote, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `symbol` but received ''"):
            await async_client.stocks.quote.with_raw_response.retrieve(
                "",
            )
