# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import correlation_list_params
from .._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from .._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.correlation_list_response import CorrelationListResponse

__all__ = ["CorrelationsResource", "AsyncCorrelationsResource"]


class CorrelationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CorrelationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return CorrelationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CorrelationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return CorrelationsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        symbols: str,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        interval: Literal["1d", "1wk", "1mo"] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CorrelationListResponse:
        """
        Retrieve correlation data between different stocks or assets.

        Args:
          symbols: Comma-separated list of stock symbols.

          end_date: End date for the correlation data.

          interval: Data interval (e.g., '1d', '1wk').

          start_date: Start date for the correlation data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/correlations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "interval": interval,
                        "start_date": start_date,
                    },
                    correlation_list_params.CorrelationListParams,
                ),
            ),
            cast_to=CorrelationListResponse,
        )


class AsyncCorrelationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCorrelationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCorrelationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCorrelationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncCorrelationsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        symbols: str,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        interval: Literal["1d", "1wk", "1mo"] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> CorrelationListResponse:
        """
        Retrieve correlation data between different stocks or assets.

        Args:
          symbols: Comma-separated list of stock symbols.

          end_date: End date for the correlation data.

          interval: Data interval (e.g., '1d', '1wk').

          start_date: Start date for the correlation data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/correlations",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "symbols": symbols,
                        "end_date": end_date,
                        "interval": interval,
                        "start_date": start_date,
                    },
                    correlation_list_params.CorrelationListParams,
                ),
            ),
            cast_to=CorrelationListResponse,
        )


class CorrelationsResourceWithRawResponse:
    def __init__(self, correlations: CorrelationsResource) -> None:
        self._correlations = correlations

        self.list = to_raw_response_wrapper(
            correlations.list,
        )


class AsyncCorrelationsResourceWithRawResponse:
    def __init__(self, correlations: AsyncCorrelationsResource) -> None:
        self._correlations = correlations

        self.list = async_to_raw_response_wrapper(
            correlations.list,
        )


class CorrelationsResourceWithStreamingResponse:
    def __init__(self, correlations: CorrelationsResource) -> None:
        self._correlations = correlations

        self.list = to_streamed_response_wrapper(
            correlations.list,
        )


class AsyncCorrelationsResourceWithStreamingResponse:
    def __init__(self, correlations: AsyncCorrelationsResource) -> None:
        self._correlations = correlations

        self.list = async_to_streamed_response_wrapper(
            correlations.list,
        )
