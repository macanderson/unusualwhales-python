# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from ..._compat import cached_property
from .detection import (
    DetectionResource,
    AsyncDetectionResource,
    DetectionResourceWithRawResponse,
    AsyncDetectionResourceWithRawResponse,
    DetectionResourceWithStreamingResponse,
    AsyncDetectionResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["SpikeResource", "AsyncSpikeResource"]


class SpikeResource(SyncAPIResource):
    @cached_property
    def detection(self) -> DetectionResource:
        return DetectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> SpikeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return SpikeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SpikeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return SpikeResourceWithStreamingResponse(self)


class AsyncSpikeResource(AsyncAPIResource):
    @cached_property
    def detection(self) -> AsyncDetectionResource:
        return AsyncDetectionResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSpikeResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSpikeResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSpikeResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncSpikeResourceWithStreamingResponse(self)


class SpikeResourceWithRawResponse:
    def __init__(self, spike: SpikeResource) -> None:
        self._spike = spike

    @cached_property
    def detection(self) -> DetectionResourceWithRawResponse:
        return DetectionResourceWithRawResponse(self._spike.detection)


class AsyncSpikeResourceWithRawResponse:
    def __init__(self, spike: AsyncSpikeResource) -> None:
        self._spike = spike

    @cached_property
    def detection(self) -> AsyncDetectionResourceWithRawResponse:
        return AsyncDetectionResourceWithRawResponse(self._spike.detection)


class SpikeResourceWithStreamingResponse:
    def __init__(self, spike: SpikeResource) -> None:
        self._spike = spike

    @cached_property
    def detection(self) -> DetectionResourceWithStreamingResponse:
        return DetectionResourceWithStreamingResponse(self._spike.detection)


class AsyncSpikeResourceWithStreamingResponse:
    def __init__(self, spike: AsyncSpikeResource) -> None:
        self._spike = spike

    @cached_property
    def detection(self) -> AsyncDetectionResourceWithStreamingResponse:
        return AsyncDetectionResourceWithStreamingResponse(self._spike.detection)
