# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .fda import (
    FdaResource,
    AsyncFdaResource,
    FdaResourceWithRawResponse,
    AsyncFdaResourceWithRawResponse,
    FdaResourceWithStreamingResponse,
    AsyncFdaResourceWithStreamingResponse,
)
from .economic import (
    EconomicResource,
    AsyncEconomicResource,
    EconomicResourceWithRawResponse,
    AsyncEconomicResourceWithRawResponse,
    EconomicResourceWithStreamingResponse,
    AsyncEconomicResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["CalendarResource", "AsyncCalendarResource"]


class CalendarResource(SyncAPIResource):
    @cached_property
    def economic(self) -> EconomicResource:
        return EconomicResource(self._client)

    @cached_property
    def fda(self) -> FdaResource:
        return FdaResource(self._client)

    @cached_property
    def with_raw_response(self) -> CalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return CalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return CalendarResourceWithStreamingResponse(self)


class AsyncCalendarResource(AsyncAPIResource):
    @cached_property
    def economic(self) -> AsyncEconomicResource:
        return AsyncEconomicResource(self._client)

    @cached_property
    def fda(self) -> AsyncFdaResource:
        return AsyncFdaResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncCalendarResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCalendarResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCalendarResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncCalendarResourceWithStreamingResponse(self)


class CalendarResourceWithRawResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

    @cached_property
    def economic(self) -> EconomicResourceWithRawResponse:
        return EconomicResourceWithRawResponse(self._calendar.economic)

    @cached_property
    def fda(self) -> FdaResourceWithRawResponse:
        return FdaResourceWithRawResponse(self._calendar.fda)


class AsyncCalendarResourceWithRawResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

    @cached_property
    def economic(self) -> AsyncEconomicResourceWithRawResponse:
        return AsyncEconomicResourceWithRawResponse(self._calendar.economic)

    @cached_property
    def fda(self) -> AsyncFdaResourceWithRawResponse:
        return AsyncFdaResourceWithRawResponse(self._calendar.fda)


class CalendarResourceWithStreamingResponse:
    def __init__(self, calendar: CalendarResource) -> None:
        self._calendar = calendar

    @cached_property
    def economic(self) -> EconomicResourceWithStreamingResponse:
        return EconomicResourceWithStreamingResponse(self._calendar.economic)

    @cached_property
    def fda(self) -> FdaResourceWithStreamingResponse:
        return FdaResourceWithStreamingResponse(self._calendar.fda)


class AsyncCalendarResourceWithStreamingResponse:
    def __init__(self, calendar: AsyncCalendarResource) -> None:
        self._calendar = calendar

    @cached_property
    def economic(self) -> AsyncEconomicResourceWithStreamingResponse:
        return AsyncEconomicResourceWithStreamingResponse(self._calendar.economic)

    @cached_property
    def fda(self) -> AsyncFdaResourceWithStreamingResponse:
        return AsyncFdaResourceWithStreamingResponse(self._calendar.fda)
