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
from ...types.spike import detection_list_params
from ..._base_client import make_request_options
from ...types.spike.detection_list_response import DetectionListResponse

__all__ = ["DetectionResource", "AsyncDetectionResource"]


class DetectionResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DetectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return DetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DetectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return DetectionResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectionListResponse:
        """
        Retrieve data on detected spikes in trading activity.

        Args:
          date: Date to filter spike data.

          symbol: Stock symbol to filter spike data.

          threshold: Threshold for spike detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/spike/detection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                        "threshold": threshold,
                    },
                    detection_list_params.DetectionListParams,
                ),
            ),
            cast_to=DetectionListResponse,
        )


class AsyncDetectionResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDetectionResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDetectionResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDetectionResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncDetectionResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        threshold: float | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> DetectionListResponse:
        """
        Retrieve data on detected spikes in trading activity.

        Args:
          date: Date to filter spike data.

          symbol: Stock symbol to filter spike data.

          threshold: Threshold for spike detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/spike/detection",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                        "threshold": threshold,
                    },
                    detection_list_params.DetectionListParams,
                ),
            ),
            cast_to=DetectionListResponse,
        )


class DetectionResourceWithRawResponse:
    def __init__(self, detection: DetectionResource) -> None:
        self._detection = detection

        self.list = to_raw_response_wrapper(
            detection.list,
        )


class AsyncDetectionResourceWithRawResponse:
    def __init__(self, detection: AsyncDetectionResource) -> None:
        self._detection = detection

        self.list = async_to_raw_response_wrapper(
            detection.list,
        )


class DetectionResourceWithStreamingResponse:
    def __init__(self, detection: DetectionResource) -> None:
        self._detection = detection

        self.list = to_streamed_response_wrapper(
            detection.list,
        )


class AsyncDetectionResourceWithStreamingResponse:
    def __init__(self, detection: AsyncDetectionResource) -> None:
        self._detection = detection

        self.list = async_to_streamed_response_wrapper(
            detection.list,
        )
