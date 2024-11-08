# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .contracts import (
    ContractsResource,
    AsyncContractsResource,
    ContractsResourceWithRawResponse,
    AsyncContractsResourceWithRawResponse,
    ContractsResourceWithStreamingResponse,
    AsyncContractsResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OptionsResource", "AsyncOptionsResource"]


class OptionsResource(SyncAPIResource):
    @cached_property
    def contracts(self) -> ContractsResource:
        return ContractsResource(self._client)

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
    def contracts(self) -> AsyncContractsResource:
        return AsyncContractsResource(self._client)

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
    def contracts(self) -> ContractsResourceWithRawResponse:
        return ContractsResourceWithRawResponse(self._options.contracts)


class AsyncOptionsResourceWithRawResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithRawResponse:
        return AsyncContractsResourceWithRawResponse(self._options.contracts)


class OptionsResourceWithStreamingResponse:
    def __init__(self, options: OptionsResource) -> None:
        self._options = options

    @cached_property
    def contracts(self) -> ContractsResourceWithStreamingResponse:
        return ContractsResourceWithStreamingResponse(self._options.contracts)


class AsyncOptionsResourceWithStreamingResponse:
    def __init__(self, options: AsyncOptionsResource) -> None:
        self._options = options

    @cached_property
    def contracts(self) -> AsyncContractsResourceWithStreamingResponse:
        return AsyncContractsResourceWithStreamingResponse(self._options.contracts)
