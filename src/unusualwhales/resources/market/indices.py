# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.market.index_retrieve_response import IndexRetrieveResponse

__all__ = ["IndicesResource", "AsyncIndicesResource"]


class IndicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> IndicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return IndicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IndicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return IndicesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexRetrieveResponse:
        """Retrieve data on major market indices."""
        return self._get(
            "/market/indices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexRetrieveResponse,
        )


class AsyncIndicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncIndicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIndicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIndicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncIndicesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> IndexRetrieveResponse:
        """Retrieve data on major market indices."""
        return await self._get(
            "/market/indices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=IndexRetrieveResponse,
        )


class IndicesResourceWithRawResponse:
    def __init__(self, indices: IndicesResource) -> None:
        self._indices = indices

        self.retrieve = to_raw_response_wrapper(
            indices.retrieve,
        )


class AsyncIndicesResourceWithRawResponse:
    def __init__(self, indices: AsyncIndicesResource) -> None:
        self._indices = indices

        self.retrieve = async_to_raw_response_wrapper(
            indices.retrieve,
        )


class IndicesResourceWithStreamingResponse:
    def __init__(self, indices: IndicesResource) -> None:
        self._indices = indices

        self.retrieve = to_streamed_response_wrapper(
            indices.retrieve,
        )


class AsyncIndicesResourceWithStreamingResponse:
    def __init__(self, indices: AsyncIndicesResource) -> None:
        self._indices = indices

        self.retrieve = async_to_streamed_response_wrapper(
            indices.retrieve,
        )