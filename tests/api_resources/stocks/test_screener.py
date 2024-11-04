# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unusualwhales import Unusualwhales, AsyncUnusualwhales
from unusualwhales.types.stocks import (
    ScreenerGetResponse,
    ScreenerPostResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestScreener:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_get(self, client: Unusualwhales) -> None:
        screener = client.stocks.screener.get()
        assert_matches_type(ScreenerGetResponse, screener, path=["response"])

    @parametrize
    def test_method_get_with_all_params(self, client: Unusualwhales) -> None:
        screener = client.stocks.screener.get(
            industry="industry",
            market_cap_max=0,
            market_cap_min=0,
            price_max=0,
            price_min=0,
            sector="sector",
            volume_max=0,
            volume_min=0,
        )
        assert_matches_type(ScreenerGetResponse, screener, path=["response"])

    @parametrize
    def test_raw_response_get(self, client: Unusualwhales) -> None:
        response = client.stocks.screener.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = response.parse()
        assert_matches_type(ScreenerGetResponse, screener, path=["response"])

    @parametrize
    def test_streaming_response_get(self, client: Unusualwhales) -> None:
        with client.stocks.screener.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = response.parse()
            assert_matches_type(ScreenerGetResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_post(self, client: Unusualwhales) -> None:
        screener = client.stocks.screener.post()
        assert_matches_type(ScreenerPostResponse, screener, path=["response"])

    @parametrize
    def test_method_post_with_all_params(self, client: Unusualwhales) -> None:
        screener = client.stocks.screener.post(
            criteria=[
                {
                    "field": "field",
                    "operator": "eq",
                    "value": "value",
                },
                {
                    "field": "field",
                    "operator": "eq",
                    "value": "value",
                },
                {
                    "field": "field",
                    "operator": "eq",
                    "value": "value",
                },
            ],
        )
        assert_matches_type(ScreenerPostResponse, screener, path=["response"])

    @parametrize
    def test_raw_response_post(self, client: Unusualwhales) -> None:
        response = client.stocks.screener.with_raw_response.post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = response.parse()
        assert_matches_type(ScreenerPostResponse, screener, path=["response"])

    @parametrize
    def test_streaming_response_post(self, client: Unusualwhales) -> None:
        with client.stocks.screener.with_streaming_response.post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = response.parse()
            assert_matches_type(ScreenerPostResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncScreener:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_get(self, async_client: AsyncUnusualwhales) -> None:
        screener = await async_client.stocks.screener.get()
        assert_matches_type(ScreenerGetResponse, screener, path=["response"])

    @parametrize
    async def test_method_get_with_all_params(self, async_client: AsyncUnusualwhales) -> None:
        screener = await async_client.stocks.screener.get(
            industry="industry",
            market_cap_max=0,
            market_cap_min=0,
            price_max=0,
            price_min=0,
            sector="sector",
            volume_max=0,
            volume_min=0,
        )
        assert_matches_type(ScreenerGetResponse, screener, path=["response"])

    @parametrize
    async def test_raw_response_get(self, async_client: AsyncUnusualwhales) -> None:
        response = await async_client.stocks.screener.with_raw_response.get()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = await response.parse()
        assert_matches_type(ScreenerGetResponse, screener, path=["response"])

    @parametrize
    async def test_streaming_response_get(self, async_client: AsyncUnusualwhales) -> None:
        async with async_client.stocks.screener.with_streaming_response.get() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = await response.parse()
            assert_matches_type(ScreenerGetResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_post(self, async_client: AsyncUnusualwhales) -> None:
        screener = await async_client.stocks.screener.post()
        assert_matches_type(ScreenerPostResponse, screener, path=["response"])

    @parametrize
    async def test_method_post_with_all_params(self, async_client: AsyncUnusualwhales) -> None:
        screener = await async_client.stocks.screener.post(
            criteria=[
                {
                    "field": "field",
                    "operator": "eq",
                    "value": "value",
                },
                {
                    "field": "field",
                    "operator": "eq",
                    "value": "value",
                },
                {
                    "field": "field",
                    "operator": "eq",
                    "value": "value",
                },
            ],
        )
        assert_matches_type(ScreenerPostResponse, screener, path=["response"])

    @parametrize
    async def test_raw_response_post(self, async_client: AsyncUnusualwhales) -> None:
        response = await async_client.stocks.screener.with_raw_response.post()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        screener = await response.parse()
        assert_matches_type(ScreenerPostResponse, screener, path=["response"])

    @parametrize
    async def test_streaming_response_post(self, async_client: AsyncUnusualwhales) -> None:
        async with async_client.stocks.screener.with_streaming_response.post() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            screener = await response.parse()
            assert_matches_type(ScreenerPostResponse, screener, path=["response"])

        assert cast(Any, response.is_closed) is True
