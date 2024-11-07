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
from ...types.calendar import economic_retrieve_params
from ...types.calendar.economic_retrieve_response import EconomicRetrieveResponse

__all__ = ["EconomicResource", "AsyncEconomicResource"]


class EconomicResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> EconomicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return EconomicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> EconomicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return EconomicResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EconomicRetrieveResponse:
        """
        Retrieve upcoming economic events and data releases.

        Args:
          country: Country to filter events.

          end_date: End date for the economic calendar data.

          start_date: Start date for the economic calendar data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/calendar/economic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "country": country,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    economic_retrieve_params.EconomicRetrieveParams,
                ),
            ),
            cast_to=EconomicRetrieveResponse,
        )


class AsyncEconomicResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncEconomicResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncEconomicResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncEconomicResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncEconomicResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        country: str | NotGiven = NOT_GIVEN,
        end_date: Union[str, date] | NotGiven = NOT_GIVEN,
        start_date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> EconomicRetrieveResponse:
        """
        Retrieve upcoming economic events and data releases.

        Args:
          country: Country to filter events.

          end_date: End date for the economic calendar data.

          start_date: Start date for the economic calendar data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/calendar/economic",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "country": country,
                        "end_date": end_date,
                        "start_date": start_date,
                    },
                    economic_retrieve_params.EconomicRetrieveParams,
                ),
            ),
            cast_to=EconomicRetrieveResponse,
        )


class EconomicResourceWithRawResponse:
    def __init__(self, economic: EconomicResource) -> None:
        self._economic = economic

        self.retrieve = to_raw_response_wrapper(
            economic.retrieve,
        )


class AsyncEconomicResourceWithRawResponse:
    def __init__(self, economic: AsyncEconomicResource) -> None:
        self._economic = economic

        self.retrieve = async_to_raw_response_wrapper(
            economic.retrieve,
        )


class EconomicResourceWithStreamingResponse:
    def __init__(self, economic: EconomicResource) -> None:
        self._economic = economic

        self.retrieve = to_streamed_response_wrapper(
            economic.retrieve,
        )


class AsyncEconomicResourceWithStreamingResponse:
    def __init__(self, economic: AsyncEconomicResource) -> None:
        self._economic = economic

        self.retrieve = async_to_streamed_response_wrapper(
            economic.retrieve,
        )
