# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unusualwhales import Unusualwhales, AsyncUnusualwhales
from unusualwhales.types.stocks import NewsListResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestNews:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: Unusualwhales) -> None:
        news = client.stocks.news.list()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: Unusualwhales) -> None:
        news = client.stocks.news.list(
            symbols="symbols",
        )
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: Unusualwhales) -> None:
        response = client.stocks.news.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = response.parse()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: Unusualwhales) -> None:
        with client.stocks.news.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = response.parse()
            assert_matches_type(NewsListResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncNews:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_list(self, async_client: AsyncUnusualwhales) -> None:
        news = await async_client.stocks.news.list()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncUnusualwhales) -> None:
        news = await async_client.stocks.news.list(
            symbols="symbols",
        )
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncUnusualwhales) -> None:
        response = await async_client.stocks.news.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        news = await response.parse()
        assert_matches_type(NewsListResponse, news, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncUnusualwhales) -> None:
        async with async_client.stocks.news.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            news = await response.parse()
            assert_matches_type(NewsListResponse, news, path=["response"])

        assert cast(Any, response.is_closed) is True
