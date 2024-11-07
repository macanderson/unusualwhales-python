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
from ...types.options_flows import greeks_flow_expiry_retrieve_params
from ...types.options_flows.greeks_flow_expiry_retrieve_response import GreeksFlowExpiryRetrieveResponse

__all__ = ["GreeksFlowExpiryResource", "AsyncGreeksFlowExpiryResource"]


class GreeksFlowExpiryResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GreeksFlowExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return GreeksFlowExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GreeksFlowExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return GreeksFlowExpiryResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreeksFlowExpiryRetrieveResponse:
        """
        Retrieve options Greek flow data aggregated by expiration date.

        Args:
          date: Date to filter the Greek flow data.

          expiration: Option expiration date.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/options/greekflow/expiry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "expiration": expiration,
                        "symbol": symbol,
                    },
                    greeks_flow_expiry_retrieve_params.GreeksFlowExpiryRetrieveParams,
                ),
            ),
            cast_to=GreeksFlowExpiryRetrieveResponse,
        )


class AsyncGreeksFlowExpiryResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGreeksFlowExpiryResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGreeksFlowExpiryResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGreeksFlowExpiryResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncGreeksFlowExpiryResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        expiration: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> GreeksFlowExpiryRetrieveResponse:
        """
        Retrieve options Greek flow data aggregated by expiration date.

        Args:
          date: Date to filter the Greek flow data.

          expiration: Option expiration date.

          symbol: Stock symbol to filter the Greek flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/options/greekflow/expiry",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "expiration": expiration,
                        "symbol": symbol,
                    },
                    greeks_flow_expiry_retrieve_params.GreeksFlowExpiryRetrieveParams,
                ),
            ),
            cast_to=GreeksFlowExpiryRetrieveResponse,
        )


class GreeksFlowExpiryResourceWithRawResponse:
    def __init__(self, greeks_flow_expiry: GreeksFlowExpiryResource) -> None:
        self._greeks_flow_expiry = greeks_flow_expiry

        self.retrieve = to_raw_response_wrapper(
            greeks_flow_expiry.retrieve,
        )


class AsyncGreeksFlowExpiryResourceWithRawResponse:
    def __init__(self, greeks_flow_expiry: AsyncGreeksFlowExpiryResource) -> None:
        self._greeks_flow_expiry = greeks_flow_expiry

        self.retrieve = async_to_raw_response_wrapper(
            greeks_flow_expiry.retrieve,
        )


class GreeksFlowExpiryResourceWithStreamingResponse:
    def __init__(self, greeks_flow_expiry: GreeksFlowExpiryResource) -> None:
        self._greeks_flow_expiry = greeks_flow_expiry

        self.retrieve = to_streamed_response_wrapper(
            greeks_flow_expiry.retrieve,
        )


class AsyncGreeksFlowExpiryResourceWithStreamingResponse:
    def __init__(self, greeks_flow_expiry: AsyncGreeksFlowExpiryResource) -> None:
        self._greeks_flow_expiry = greeks_flow_expiry

        self.retrieve = async_to_streamed_response_wrapper(
            greeks_flow_expiry.retrieve,
        )
