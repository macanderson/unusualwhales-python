# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .options_flows import (
    OptionsFlowsResource,
    AsyncOptionsFlowsResource,
    OptionsFlowsResourceWithRawResponse,
    AsyncOptionsFlowsResourceWithRawResponse,
    OptionsFlowsResourceWithStreamingResponse,
    AsyncOptionsFlowsResourceWithStreamingResponse,
)

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    @cached_property
    def options_flows(self) -> OptionsFlowsResource:
        return OptionsFlowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return OptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return OptionsResourceWithStreamingResponse(self)


class AsyncOptionsResource(AsyncAPIResource):
    @cached_property
    def options_flows(self) -> AsyncOptionsFlowsResource:
        return AsyncOptionsFlowsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncOptionsResourceWithStreamingResponse(self)


class OptionsResourceWithRawResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

    @cached_property
    def options_flows(self) -> OptionsFlowsResourceWithRawResponse:
        return OptionsFlowsResourceWithRawResponse(self._options.options_flows)


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

    @cached_property
    def options_flows(self) -> AsyncOptionsFlowsResourceWithRawResponse:
        return AsyncOptionsFlowsResourceWithRawResponse(self._options.options_flows)


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

    @cached_property
    def options_flows(self) -> OptionsFlowsResourceWithStreamingResponse:
        return OptionsFlowsResourceWithStreamingResponse(self._options.options_flows)


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

    @cached_property
    def options_flows(self) -> AsyncOptionsFlowsResourceWithStreamingResponse:
        return AsyncOptionsFlowsResourceWithStreamingResponse(self._options.options_flows)
