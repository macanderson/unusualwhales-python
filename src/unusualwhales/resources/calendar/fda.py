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
from ...types.calendar import fda_retrieve_params
from ...types.calendar.fda_retrieve_response import FdaRetrieveResponse

__all__ = ["FdaResource", "AsyncFdaResource"]


class FdaResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FdaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return FdaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FdaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return FdaResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FdaRetrieveResponse:
        """
        Retrieve upcoming FDA approval dates and drug event data.

        Args:
          end_date: End date for the FDA calendar data.

          start_date: Start date for the FDA calendar data.

          symbol: Stock symbol to filter FDA events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/calendar/fda",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "symbol": symbol,
                    },
                    fda_retrieve_params.FdaRetrieveParams,
                ),
            ),
            cast_to=FdaRetrieveResponse,
        )


class AsyncFdaResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFdaResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFdaResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFdaResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncFdaResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> FdaRetrieveResponse:
        """
        Retrieve upcoming FDA approval dates and drug event data.

        Args:
          end_date: End date for the FDA calendar data.

          start_date: Start date for the FDA calendar data.

          symbol: Stock symbol to filter FDA events.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/calendar/fda",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "start_date": start_date,
                        "symbol": symbol,
                    },
                    fda_retrieve_params.FdaRetrieveParams,
                ),
            ),
            cast_to=FdaRetrieveResponse,
        )


class FdaResourceWithRawResponse:
    def __init__(self, fda: FdaResource) -> None:
        self._fda = fda

        self.retrieve = to_raw_response_wrapper(
            fda.retrieve,
        )


class AsyncFdaResourceWithRawResponse:
    def __init__(self, fda: AsyncFdaResource) -> None:
        self._fda = fda

        self.retrieve = async_to_raw_response_wrapper(
            fda.retrieve,
        )


class FdaResourceWithStreamingResponse:
    def __init__(self, fda: FdaResource) -> None:
        self._fda = fda

        self.retrieve = to_streamed_response_wrapper(
            fda.retrieve,
        )


class AsyncFdaResourceWithStreamingResponse:
    def __init__(self, fda: AsyncFdaResource) -> None:
        self._fda = fda

        self.retrieve = async_to_streamed_response_wrapper(
            fda.retrieve,
        )
