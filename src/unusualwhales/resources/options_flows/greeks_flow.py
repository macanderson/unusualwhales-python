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
from ...types.options_flows import greeks_flow_retrieve_params
from ...types.options_flows.greeks_flow_retrieve_response import GreeksFlowRetrieveResponse

__all__ = ["GreeksFlowResource", "AsyncGreeksFlowResource"]


class GreeksFlowResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GreeksFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return GreeksFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreeksFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return GreeksFlowResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_delta: float | NotGiven = NOT_GIVEN,
        min_delta: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreeksFlowRetrieveResponse:
        """
        Retrieve options flow data with Greek calculations.

        Args:
          date: Date to filter the Greek flow data.

          max_delta: Maximum delta value.

          min_delta: Minimum delta value.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/options/greekflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "max_delta": max_delta,
                        "min_delta": min_delta,
                        "symbol": symbol,
                    },
                    greeks_flow_retrieve_params.GreeksFlowRetrieveParams,
                ),
            ),
            cast_to=GreeksFlowRetrieveResponse,
        )


class AsyncGreeksFlowResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGreeksFlowResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGreeksFlowResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreeksFlowResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncGreeksFlowResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        max_delta: float | NotGiven = NOT_GIVEN,
        min_delta: float | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreeksFlowRetrieveResponse:
        """
        Retrieve options flow data with Greek calculations.

        Args:
          date: Date to filter the Greek flow data.

          max_delta: Maximum delta value.

          min_delta: Minimum delta value.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/options/greekflow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "max_delta": max_delta,
                        "min_delta": min_delta,
                        "symbol": symbol,
                    },
                    greeks_flow_retrieve_params.GreeksFlowRetrieveParams,
                ),
            ),
            cast_to=GreeksFlowRetrieveResponse,
        )


class GreeksFlowResourceWithRawResponse:
    def __init__(self, greeks_flow: GreeksFlowResource) -> None:
        self._greeks_flow = greeks_flow

        self.retrieve = to_raw_response_wrapper(
            greeks_flow.retrieve,
        )


class AsyncGreeksFlowResourceWithRawResponse:
    def __init__(self, greeks_flow: AsyncGreeksFlowResource) -> None:
        self._greeks_flow = greeks_flow

        self.retrieve = async_to_raw_response_wrapper(
            greeks_flow.retrieve,
        )


class GreeksFlowResourceWithStreamingResponse:
    def __init__(self, greeks_flow: GreeksFlowResource) -> None:
        self._greeks_flow = greeks_flow

        self.retrieve = to_streamed_response_wrapper(
            greeks_flow.retrieve,
        )


class AsyncGreeksFlowResourceWithStreamingResponse:
    def __init__(self, greeks_flow: AsyncGreeksFlowResource) -> None:
        self._greeks_flow = greeks_flow

        self.retrieve = async_to_streamed_response_wrapper(
            greeks_flow.retrieve,
        )
