# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.options_flows import oi_change_retrieve_params
from ...types.options_flows.oi_change_retrieve_response import OiChangeRetrieveResponse

__all__ = ["OiChangeResource", "AsyncOiChangeResource"]


class OiChangeResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> OiChangeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return OiChangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OiChangeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return OiChangeResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OiChangeRetrieveResponse:
        """
        Retrieve open interest change data for a specific stock symbol.

        Args:
          date: Date to filter the OI change data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/options/oi_change/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, oi_change_retrieve_params.OiChangeRetrieveParams),
            ),
            cast_to=OiChangeRetrieveResponse,
        )


class AsyncOiChangeResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncOiChangeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOiChangeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOiChangeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncOiChangeResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OiChangeRetrieveResponse:
        """
        Retrieve open interest change data for a specific stock symbol.

        Args:
          date: Date to filter the OI change data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/options/oi_change/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"date": date}, oi_change_retrieve_params.OiChangeRetrieveParams),
            ),
            cast_to=OiChangeRetrieveResponse,
        )


class OiChangeResourceWithRawResponse:
    def __init__(self, oi_change: OiChangeResource) -> None:
        self._oi_change = oi_change

        self.retrieve = to_raw_response_wrapper(
            oi_change.retrieve,
        )


class AsyncOiChangeResourceWithRawResponse:
    def __init__(self, oi_change: AsyncOiChangeResource) -> None:
        self._oi_change = oi_change

        self.retrieve = async_to_raw_response_wrapper(
            oi_change.retrieve,
        )


class OiChangeResourceWithStreamingResponse:
    def __init__(self, oi_change: OiChangeResource) -> None:
        self._oi_change = oi_change

        self.retrieve = to_streamed_response_wrapper(
            oi_change.retrieve,
        )


class AsyncOiChangeResourceWithStreamingResponse:
    def __init__(self, oi_change: AsyncOiChangeResource) -> None:
        self._oi_change = oi_change

        self.retrieve = async_to_streamed_response_wrapper(
            oi_change.retrieve,
        )