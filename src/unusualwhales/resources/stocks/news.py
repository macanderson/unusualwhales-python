# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.stocks import news_list_params
from ...types.stocks.news_list_response import NewsListResponse

__all__ = ["NewsResource", "AsyncNewsResource"]


class NewsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> NewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return NewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> NewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return NewsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        symbols: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsListResponse:
        """
        Retrieve the latest financial news.

        Args:
          symbols: Comma-separated list of stock symbols to filter news.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"symbols": symbols}, news_list_params.NewsListParams),
            ),
            cast_to=NewsListResponse,
        )


class AsyncNewsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncNewsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncNewsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncNewsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncNewsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        symbols: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> NewsListResponse:
        """
        Retrieve the latest financial news.

        Args:
          symbols: Comma-separated list of stock symbols to filter news.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/news",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform({"symbols": symbols}, news_list_params.NewsListParams),
            ),
            cast_to=NewsListResponse,
        )


class NewsResourceWithRawResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.list = to_raw_response_wrapper(
            news.list,
        )


class AsyncNewsResourceWithRawResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.list = async_to_raw_response_wrapper(
            news.list,
        )


class NewsResourceWithStreamingResponse:
    def __init__(self, news: NewsResource) -> None:
        self._news = news

        self.list = to_streamed_response_wrapper(
            news.list,
        )


class AsyncNewsResourceWithStreamingResponse:
    def __init__(self, news: AsyncNewsResource) -> None:
        self._news = news

        self.list = async_to_streamed_response_wrapper(
            news.list,
        )
