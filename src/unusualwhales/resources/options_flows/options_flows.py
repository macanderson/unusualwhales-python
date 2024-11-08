# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date

import httpx

from .chain import (
    ChainResource,
    AsyncChainResource,
    ChainResourceWithRawResponse,
    AsyncChainResourceWithRawResponse,
    ChainResourceWithStreamingResponse,
    AsyncChainResourceWithStreamingResponse,
)
from .greeks import (
    GreeksResource,
    AsyncGreeksResource,
    GreeksResourceWithRawResponse,
    AsyncGreeksResourceWithRawResponse,
    GreeksResourceWithStreamingResponse,
    AsyncGreeksResourceWithStreamingResponse,
)
from ...types import options_flow_list_params, options_flow_retrieve_params
from ..._types import NOT_GIVEN, Body, Query, Headers, NotGiven
from ..._utils import (
    maybe_transform,
    async_maybe_transform,
)
from .contract import (
    ContractResource,
    AsyncContractResource,
    ContractResourceWithRawResponse,
    AsyncContractResourceWithRawResponse,
    ContractResourceWithStreamingResponse,
    AsyncContractResourceWithStreamingResponse,
)
from ..._compat import cached_property
from .oi_change import (
    OiChangeResource,
    AsyncOiChangeResource,
    OiChangeResourceWithRawResponse,
    AsyncOiChangeResourceWithRawResponse,
    OiChangeResourceWithStreamingResponse,
    AsyncOiChangeResourceWithStreamingResponse,
)
from .historical import (
    HistoricalResource,
    AsyncHistoricalResource,
    HistoricalResourceWithRawResponse,
    AsyncHistoricalResourceWithRawResponse,
    HistoricalResourceWithStreamingResponse,
    AsyncHistoricalResourceWithStreamingResponse,
)
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .expirations import (
    ExpirationsResource,
    AsyncExpirationsResource,
    ExpirationsResourceWithRawResponse,
    AsyncExpirationsResourceWithRawResponse,
    ExpirationsResourceWithStreamingResponse,
    AsyncExpirationsResourceWithStreamingResponse,
)
from .greeks_flow import (
    GreeksFlowResource,
    AsyncGreeksFlowResource,
    GreeksFlowResourceWithRawResponse,
    AsyncGreeksFlowResourceWithRawResponse,
    GreeksFlowResourceWithStreamingResponse,
    AsyncGreeksFlowResourceWithStreamingResponse,
)
from .total_volume import (
    TotalVolumeResource,
    AsyncTotalVolumeResource,
    TotalVolumeResourceWithRawResponse,
    AsyncTotalVolumeResourceWithRawResponse,
    TotalVolumeResourceWithStreamingResponse,
    AsyncTotalVolumeResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .greeks_flow_expiry import (
    GreeksFlowExpiryResource,
    AsyncGreeksFlowExpiryResource,
    GreeksFlowExpiryResourceWithRawResponse,
    AsyncGreeksFlowExpiryResourceWithRawResponse,
    GreeksFlowExpiryResourceWithStreamingResponse,
    AsyncGreeksFlowExpiryResourceWithStreamingResponse,
)
from ...types.options_flow_list_response import OptionsFlowListResponse
from ...types.options_flow_retrieve_response import OptionsFlowRetrieveResponse

__all__ = ["OptionsFlowsResource", "AsyncOptionsFlowsResource"]


class OptionsFlowsResource(SyncAPIResource):
    @cached_property
    def chain(self) -> ChainResource:
        return ChainResource(self._client)

    @cached_property
    def expirations(self) -> ExpirationsResource:
        return ExpirationsResource(self._client)

    @cached_property
    def greeks(self) -> GreeksResource:
        return GreeksResource(self._client)

    @cached_property
    def historical(self) -> HistoricalResource:
        return HistoricalResource(self._client)

    @cached_property
    def greeks_flow(self) -> GreeksFlowResource:
        return GreeksFlowResource(self._client)

    @cached_property
    def greeks_flow_expiry(self) -> GreeksFlowExpiryResource:
        return GreeksFlowExpiryResource(self._client)

    @cached_property
    def oi_change(self) -> OiChangeResource:
        return OiChangeResource(self._client)

    @cached_property
    def total_volume(self) -> TotalVolumeResource:
        return TotalVolumeResource(self._client)

    @cached_property
    def contract(self) -> ContractResource:
        return ContractResource(self._client)

    @cached_property
    def with_raw_response(self) -> OptionsFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return OptionsFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OptionsFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return OptionsFlowsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionsFlowRetrieveResponse:
        """
        Retrieve options flow data for a specific symbol.

        Args:
          date: Date to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return self._get(
            f"/options/flow/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform({"date": date}, options_flow_retrieve_params.OptionsFlowRetrieveParams),
            ),
            cast_to=OptionsFlowRetrieveResponse,
        )

    def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionsFlowListResponse:
        """
        Retrieve options flow data.

        Args:
          date: Date to filter the options flow data.

          symbol: Stock symbol to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/options/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                    },
                    options_flow_list_params.OptionsFlowListParams,
                ),
            ),
            cast_to=OptionsFlowListResponse,
        )


class AsyncOptionsFlowsResource(AsyncAPIResource):
    @cached_property
    def chain(self) -> AsyncChainResource:
        return AsyncChainResource(self._client)

    @cached_property
    def expirations(self) -> AsyncExpirationsResource:
        return AsyncExpirationsResource(self._client)

    @cached_property
    def greeks(self) -> AsyncGreeksResource:
        return AsyncGreeksResource(self._client)

    @cached_property
    def historical(self) -> AsyncHistoricalResource:
        return AsyncHistoricalResource(self._client)

    @cached_property
    def greeks_flow(self) -> AsyncGreeksFlowResource:
        return AsyncGreeksFlowResource(self._client)

    @cached_property
    def greeks_flow_expiry(self) -> AsyncGreeksFlowExpiryResource:
        return AsyncGreeksFlowExpiryResource(self._client)

    @cached_property
    def oi_change(self) -> AsyncOiChangeResource:
        return AsyncOiChangeResource(self._client)

    @cached_property
    def total_volume(self) -> AsyncTotalVolumeResource:
        return AsyncTotalVolumeResource(self._client)

    @cached_property
    def contract(self) -> AsyncContractResource:
        return AsyncContractResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOptionsFlowsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return the
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOptionsFlowsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOptionsFlowsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/macanderson/unusualwhales-python#with_streaming_response
        """
        return AsyncOptionsFlowsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        symbol: str,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionsFlowRetrieveResponse:
        """
        Retrieve options flow data for a specific symbol.

        Args:
          date: Date to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not symbol:
            raise ValueError(f"Expected a non-empty value for `symbol` but received {symbol!r}")
        return await self._get(
            f"/options/flow/{symbol}",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {"date": date}, options_flow_retrieve_params.OptionsFlowRetrieveParams
                ),
            ),
            cast_to=OptionsFlowRetrieveResponse,
        )

    async def list(
        self,
        *,
        date: Union[str, date] | NotGiven = NOT_GIVEN,
        symbol: str | NotGiven = NOT_GIVEN,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = NOT_GIVEN,
    ) -> OptionsFlowListResponse:
        """
        Retrieve options flow data.

        Args:
          date: Date to filter the options flow data.

          symbol: Stock symbol to filter the options flow data.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/options/flow",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "date": date,
                        "symbol": symbol,
                    },
                    options_flow_list_params.OptionsFlowListParams,
                ),
            ),
            cast_to=OptionsFlowListResponse,
        )


class OptionsFlowsResourceWithRawResponse:
    def __init__(self, options_flows: OptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = to_raw_response_wrapper(
            options_flows.retrieve,
        )
        self.list = to_raw_response_wrapper(
            options_flows.list,
        )

    @cached_property
    def chain(self) -> ChainResourceWithRawResponse:
        return ChainResourceWithRawResponse(self._options_flows.chain)

    @cached_property
    def expirations(self) -> ExpirationsResourceWithRawResponse:
        return ExpirationsResourceWithRawResponse(self._options_flows.expirations)

    @cached_property
    def greeks(self) -> GreeksResourceWithRawResponse:
        return GreeksResourceWithRawResponse(self._options_flows.greeks)

    @cached_property
    def historical(self) -> HistoricalResourceWithRawResponse:
        return HistoricalResourceWithRawResponse(self._options_flows.historical)

    @cached_property
    def greeks_flow(self) -> GreeksFlowResourceWithRawResponse:
        return GreeksFlowResourceWithRawResponse(self._options_flows.greeks_flow)

    @cached_property
    def greeks_flow_expiry(self) -> GreeksFlowExpiryResourceWithRawResponse:
        return GreeksFlowExpiryResourceWithRawResponse(self._options_flows.greeks_flow_expiry)

    @cached_property
    def oi_change(self) -> OiChangeResourceWithRawResponse:
        return OiChangeResourceWithRawResponse(self._options_flows.oi_change)

    @cached_property
    def total_volume(self) -> TotalVolumeResourceWithRawResponse:
        return TotalVolumeResourceWithRawResponse(self._options_flows.total_volume)

    @cached_property
    def contract(self) -> ContractResourceWithRawResponse:
        return ContractResourceWithRawResponse(self._options_flows.contract)


class AsyncOptionsFlowsResourceWithRawResponse:
    def __init__(self, options_flows: AsyncOptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = async_to_raw_response_wrapper(
            options_flows.retrieve,
        )
        self.list = async_to_raw_response_wrapper(
            options_flows.list,
        )

    @cached_property
    def chain(self) -> AsyncChainResourceWithRawResponse:
        return AsyncChainResourceWithRawResponse(self._options_flows.chain)

    @cached_property
    def expirations(self) -> AsyncExpirationsResourceWithRawResponse:
        return AsyncExpirationsResourceWithRawResponse(self._options_flows.expirations)

    @cached_property
    def greeks(self) -> AsyncGreeksResourceWithRawResponse:
        return AsyncGreeksResourceWithRawResponse(self._options_flows.greeks)

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithRawResponse:
        return AsyncHistoricalResourceWithRawResponse(self._options_flows.historical)

    @cached_property
    def greeks_flow(self) -> AsyncGreeksFlowResourceWithRawResponse:
        return AsyncGreeksFlowResourceWithRawResponse(self._options_flows.greeks_flow)

    @cached_property
    def greeks_flow_expiry(self) -> AsyncGreeksFlowExpiryResourceWithRawResponse:
        return AsyncGreeksFlowExpiryResourceWithRawResponse(self._options_flows.greeks_flow_expiry)

    @cached_property
    def oi_change(self) -> AsyncOiChangeResourceWithRawResponse:
        return AsyncOiChangeResourceWithRawResponse(self._options_flows.oi_change)

    @cached_property
    def total_volume(self) -> AsyncTotalVolumeResourceWithRawResponse:
        return AsyncTotalVolumeResourceWithRawResponse(self._options_flows.total_volume)

    @cached_property
    def contract(self) -> AsyncContractResourceWithRawResponse:
        return AsyncContractResourceWithRawResponse(self._options_flows.contract)


class OptionsFlowsResourceWithStreamingResponse:
    def __init__(self, options_flows: OptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = to_streamed_response_wrapper(
            options_flows.retrieve,
        )
        self.list = to_streamed_response_wrapper(
            options_flows.list,
        )

    @cached_property
    def chain(self) -> ChainResourceWithStreamingResponse:
        return ChainResourceWithStreamingResponse(self._options_flows.chain)

    @cached_property
    def expirations(self) -> ExpirationsResourceWithStreamingResponse:
        return ExpirationsResourceWithStreamingResponse(self._options_flows.expirations)

    @cached_property
    def greeks(self) -> GreeksResourceWithStreamingResponse:
        return GreeksResourceWithStreamingResponse(self._options_flows.greeks)

    @cached_property
    def historical(self) -> HistoricalResourceWithStreamingResponse:
        return HistoricalResourceWithStreamingResponse(self._options_flows.historical)

    @cached_property
    def greeks_flow(self) -> GreeksFlowResourceWithStreamingResponse:
        return GreeksFlowResourceWithStreamingResponse(self._options_flows.greeks_flow)

    @cached_property
    def greeks_flow_expiry(self) -> GreeksFlowExpiryResourceWithStreamingResponse:
        return GreeksFlowExpiryResourceWithStreamingResponse(self._options_flows.greeks_flow_expiry)

    @cached_property
    def oi_change(self) -> OiChangeResourceWithStreamingResponse:
        return OiChangeResourceWithStreamingResponse(self._options_flows.oi_change)

    @cached_property
    def total_volume(self) -> TotalVolumeResourceWithStreamingResponse:
        return TotalVolumeResourceWithStreamingResponse(self._options_flows.total_volume)

    @cached_property
    def contract(self) -> ContractResourceWithStreamingResponse:
        return ContractResourceWithStreamingResponse(self._options_flows.contract)


class AsyncOptionsFlowsResourceWithStreamingResponse:
    def __init__(self, options_flows: AsyncOptionsFlowsResource) -> None:
        self._options_flows = options_flows

        self.retrieve = async_to_streamed_response_wrapper(
            options_flows.retrieve,
        )
        self.list = async_to_streamed_response_wrapper(
            options_flows.list,
        )

    @cached_property
    def chain(self) -> AsyncChainResourceWithStreamingResponse:
        return AsyncChainResourceWithStreamingResponse(self._options_flows.chain)

    @cached_property
    def expirations(self) -> AsyncExpirationsResourceWithStreamingResponse:
        return AsyncExpirationsResourceWithStreamingResponse(self._options_flows.expirations)

    @cached_property
    def greeks(self) -> AsyncGreeksResourceWithStreamingResponse:
        return AsyncGreeksResourceWithStreamingResponse(self._options_flows.greeks)

    @cached_property
    def historical(self) -> AsyncHistoricalResourceWithStreamingResponse:
        return AsyncHistoricalResourceWithStreamingResponse(self._options_flows.historical)

    @cached_property
    def greeks_flow(self) -> AsyncGreeksFlowResourceWithStreamingResponse:
        return AsyncGreeksFlowResourceWithStreamingResponse(self._options_flows.greeks_flow)

    @cached_property
    def greeks_flow_expiry(self) -> AsyncGreeksFlowExpiryResourceWithStreamingResponse:
        return AsyncGreeksFlowExpiryResourceWithStreamingResponse(self._options_flows.greeks_flow_expiry)

    @cached_property
    def oi_change(self) -> AsyncOiChangeResourceWithStreamingResponse:
        return AsyncOiChangeResourceWithStreamingResponse(self._options_flows.oi_change)

    @cached_property
    def total_volume(self) -> AsyncTotalVolumeResourceWithStreamingResponse:
        return AsyncTotalVolumeResourceWithStreamingResponse(self._options_flows.total_volume)

    @cached_property
    def contract(self) -> AsyncContractResourceWithStreamingResponse:
        return AsyncContractResourceWithStreamingResponse(self._options_flows.contract)
