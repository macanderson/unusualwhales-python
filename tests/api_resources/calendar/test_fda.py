# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from unusualwhales import Unusualwhales, AsyncUnusualwhales
from unusualwhales._utils import parse_date
from unusualwhales.types.calendar import FdaRetrieveResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFda:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: Unusualwhales) -> None:
        fda = client.calendar.fda.retrieve()
        assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

    @parametrize
    def test_method_retrieve_with_all_params(self, client: Unusualwhales) -> None:
        fda = client.calendar.fda.retrieve(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            symbol="symbol",
        )
        assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: Unusualwhales) -> None:
        response = client.calendar.fda.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fda = response.parse()
        assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: Unusualwhales) -> None:
        with client.calendar.fda.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fda = response.parse()
            assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFda:
    parametrize = pytest.mark.parametrize("async_client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        fda = await async_client.calendar.fda.retrieve()
        assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

    @parametrize
    async def test_method_retrieve_with_all_params(self, async_client: AsyncUnusualwhales) -> None:
        fda = await async_client.calendar.fda.retrieve(
            end_date=parse_date("2019-12-27"),
            start_date=parse_date("2019-12-27"),
            symbol="symbol",
        )
        assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        response = await async_client.calendar.fda.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fda = await response.parse()
        assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncUnusualwhales) -> None:
        async with async_client.calendar.fda.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fda = await response.parse()
            assert_matches_type(FdaRetrieveResponse, fda, path=["response"])

        assert cast(Any, response.is_closed) is True
