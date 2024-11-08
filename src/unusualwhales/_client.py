# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, Union, Mapping
from typing_extensions import Self, override

import httpx

from . import resources, _exceptions
from ._qs import Querystring
from ._types import (
    NOT_GIVEN,
    Omit,
    Timeout,
    NotGiven,
    Transport,
    ProxiesTypes,
    RequestOptions,
)
from ._utils import (
    is_given,
    get_async_library,
)
from ._version import __version__
from ._streaming import Stream as Stream, AsyncStream as AsyncStream
from ._exceptions import APIStatusError, UnusualwhalesError
from ._base_client import (
    DEFAULT_MAX_RETRIES,
    SyncAPIClient,
    AsyncAPIClient,
)

__all__ = [
    "Timeout",
    "Transport",
    "ProxiesTypes",
    "RequestOptions",
    "resources",
    "Unusualwhales",
    "AsyncUnusualwhales",
    "Client",
    "AsyncClient",
]


class Unusualwhales(SyncAPIClient):
    stocks: resources.StocksResource
    congress: resources.CongressResource
    institutions: resources.InstitutionsResource
    darkpool: resources.DarkpoolResource
    etf: resources.EtfResource
    options_flows: resources.OptionsFlowsResource
    seasonality: resources.SeasonalityResource
    insider_trades: resources.InsiderTradesResource
    spike: resources.SpikeResource
    calendar: resources.CalendarResource
    correlations: resources.CorrelationsResource
    analyst: resources.AnalystResource
    market: resources.MarketResource
    options: resources.OptionsResource
    with_raw_response: UnusualwhalesWithRawResponse
    with_streaming_response: UnusualwhalesWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#client) for more details.
        http_client: httpx.Client | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new synchronous unusualwhales client instance.

        This automatically infers the `api_key` argument from the `API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise UnusualwhalesError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("UNUSUALWHALES_BASE_URL")
        if base_url is None:
            base_url = f"https://api.unusualwhales.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.stocks = resources.StocksResource(self)
        self.congress = resources.CongressResource(self)
        self.institutions = resources.InstitutionsResource(self)
        self.darkpool = resources.DarkpoolResource(self)
        self.etf = resources.EtfResource(self)
        self.options_flows = resources.OptionsFlowsResource(self)
        self.seasonality = resources.SeasonalityResource(self)
        self.insider_trades = resources.InsiderTradesResource(self)
        self.spike = resources.SpikeResource(self)
        self.calendar = resources.CalendarResource(self)
        self.correlations = resources.CorrelationsResource(self)
        self.analyst = resources.AnalystResource(self)
        self.market = resources.MarketResource(self)
        self.options = resources.OptionsResource(self)
        self.with_raw_response = UnusualwhalesWithRawResponse(self)
        self.with_streaming_response = UnusualwhalesWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": "false",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.Client | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class AsyncUnusualwhales(AsyncAPIClient):
    stocks: resources.AsyncStocksResource
    congress: resources.AsyncCongressResource
    institutions: resources.AsyncInstitutionsResource
    darkpool: resources.AsyncDarkpoolResource
    etf: resources.AsyncEtfResource
    options_flows: resources.AsyncOptionsFlowsResource
    seasonality: resources.AsyncSeasonalityResource
    insider_trades: resources.AsyncInsiderTradesResource
    spike: resources.AsyncSpikeResource
    calendar: resources.AsyncCalendarResource
    correlations: resources.AsyncCorrelationsResource
    analyst: resources.AsyncAnalystResource
    market: resources.AsyncMarketResource
    options: resources.AsyncOptionsResource
    with_raw_response: AsyncUnusualwhalesWithRawResponse
    with_streaming_response: AsyncUnusualwhalesWithStreamedResponse

    # client options
    api_key: str

    def __init__(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: Union[float, Timeout, None, NotGiven] = NOT_GIVEN,
        max_retries: int = DEFAULT_MAX_RETRIES,
        default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        # Configure a custom httpx client.
        # We provide a `DefaultAsyncHttpxClient` class that you can pass to retain the default values we use for `limits`, `timeout` & `follow_redirects`.
        # See the [httpx documentation](https://www.python-httpx.org/api/#asyncclient) for more details.
        http_client: httpx.AsyncClient | None = None,
        # Enable or disable schema validation for data returned by the API.
        # When enabled an error APIResponseValidationError is raised
        # if the API responds with invalid data for the expected schema.
        #
        # This parameter may be removed or changed in the future.
        # If you rely on this feature, please open a GitHub issue
        # outlining your use-case to help us decide if it should be
        # part of our public interface in the future.
        _strict_response_validation: bool = False,
    ) -> None:
        """Construct a new async unusualwhales client instance.

        This automatically infers the `api_key` argument from the `API_KEY` environment variable if it is not provided.
        """
        if api_key is None:
            api_key = os.environ.get("API_KEY")
        if api_key is None:
            raise UnusualwhalesError(
                "The api_key client option must be set either by passing api_key to the client or by setting the API_KEY environment variable"
            )
        self.api_key = api_key

        if base_url is None:
            base_url = os.environ.get("UNUSUALWHALES_BASE_URL")
        if base_url is None:
            base_url = f"https://api.unusualwhales.com"

        super().__init__(
            version=__version__,
            base_url=base_url,
            max_retries=max_retries,
            timeout=timeout,
            http_client=http_client,
            custom_headers=default_headers,
            custom_query=default_query,
            _strict_response_validation=_strict_response_validation,
        )

        self.stocks = resources.AsyncStocksResource(self)
        self.congress = resources.AsyncCongressResource(self)
        self.institutions = resources.AsyncInstitutionsResource(self)
        self.darkpool = resources.AsyncDarkpoolResource(self)
        self.etf = resources.AsyncEtfResource(self)
        self.options_flows = resources.AsyncOptionsFlowsResource(self)
        self.seasonality = resources.AsyncSeasonalityResource(self)
        self.insider_trades = resources.AsyncInsiderTradesResource(self)
        self.spike = resources.AsyncSpikeResource(self)
        self.calendar = resources.AsyncCalendarResource(self)
        self.correlations = resources.AsyncCorrelationsResource(self)
        self.analyst = resources.AsyncAnalystResource(self)
        self.market = resources.AsyncMarketResource(self)
        self.options = resources.AsyncOptionsResource(self)
        self.with_raw_response = AsyncUnusualwhalesWithRawResponse(self)
        self.with_streaming_response = AsyncUnusualwhalesWithStreamedResponse(self)

    @property
    @override
    def qs(self) -> Querystring:
        return Querystring(array_format="comma")

    @property
    @override
    def auth_headers(self) -> dict[str, str]:
        api_key = self.api_key
        return {"Authorization": api_key}

    @property
    @override
    def default_headers(self) -> dict[str, str | Omit]:
        return {
            **super().default_headers,
            "X-Stainless-Async": f"async:{get_async_library()}",
            **self._custom_headers,
        }

    def copy(
        self,
        *,
        api_key: str | None = None,
        base_url: str | httpx.URL | None = None,
        timeout: float | Timeout | None | NotGiven = NOT_GIVEN,
        http_client: httpx.AsyncClient | None = None,
        max_retries: int | NotGiven = NOT_GIVEN,
        default_headers: Mapping[str, str] | None = None,
        set_default_headers: Mapping[str, str] | None = None,
        default_query: Mapping[str, object] | None = None,
        set_default_query: Mapping[str, object] | None = None,
        _extra_kwargs: Mapping[str, Any] = {},
    ) -> Self:
        """
        Create a new client instance re-using the same options given to the current client with optional overriding.
        """
        if default_headers is not None and set_default_headers is not None:
            raise ValueError("The `default_headers` and `set_default_headers` arguments are mutually exclusive")

        if default_query is not None and set_default_query is not None:
            raise ValueError("The `default_query` and `set_default_query` arguments are mutually exclusive")

        headers = self._custom_headers
        if default_headers is not None:
            headers = {**headers, **default_headers}
        elif set_default_headers is not None:
            headers = set_default_headers

        params = self._custom_query
        if default_query is not None:
            params = {**params, **default_query}
        elif set_default_query is not None:
            params = set_default_query

        http_client = http_client or self._client
        return self.__class__(
            api_key=api_key or self.api_key,
            base_url=base_url or self.base_url,
            timeout=self.timeout if isinstance(timeout, NotGiven) else timeout,
            http_client=http_client,
            max_retries=max_retries if is_given(max_retries) else self.max_retries,
            default_headers=headers,
            default_query=params,
            **_extra_kwargs,
        )

    # Alias for `copy` for nicer inline usage, e.g.
    # client.with_options(timeout=10).foo.create(...)
    with_options = copy

    @override
    def _make_status_error(
        self,
        err_msg: str,
        *,
        body: object,
        response: httpx.Response,
    ) -> APIStatusError:
        if response.status_code == 400:
            return _exceptions.BadRequestError(err_msg, response=response, body=body)

        if response.status_code == 401:
            return _exceptions.AuthenticationError(err_msg, response=response, body=body)

        if response.status_code == 403:
            return _exceptions.PermissionDeniedError(err_msg, response=response, body=body)

        if response.status_code == 404:
            return _exceptions.NotFoundError(err_msg, response=response, body=body)

        if response.status_code == 409:
            return _exceptions.ConflictError(err_msg, response=response, body=body)

        if response.status_code == 422:
            return _exceptions.UnprocessableEntityError(err_msg, response=response, body=body)

        if response.status_code == 429:
            return _exceptions.RateLimitError(err_msg, response=response, body=body)

        if response.status_code >= 500:
            return _exceptions.InternalServerError(err_msg, response=response, body=body)
        return APIStatusError(err_msg, response=response, body=body)


class UnusualwhalesWithRawResponse:
    def __init__(self, client: Unusualwhales) -> None:
        self.stocks = resources.StocksResourceWithRawResponse(client.stocks)
        self.congress = resources.CongressResourceWithRawResponse(client.congress)
        self.institutions = resources.InstitutionsResourceWithRawResponse(client.institutions)
        self.darkpool = resources.DarkpoolResourceWithRawResponse(client.darkpool)
        self.etf = resources.EtfResourceWithRawResponse(client.etf)
        self.options_flows = resources.OptionsFlowsResourceWithRawResponse(client.options_flows)
        self.seasonality = resources.SeasonalityResourceWithRawResponse(client.seasonality)
        self.insider_trades = resources.InsiderTradesResourceWithRawResponse(client.insider_trades)
        self.spike = resources.SpikeResourceWithRawResponse(client.spike)
        self.calendar = resources.CalendarResourceWithRawResponse(client.calendar)
        self.correlations = resources.CorrelationsResourceWithRawResponse(client.correlations)
        self.analyst = resources.AnalystResourceWithRawResponse(client.analyst)
        self.market = resources.MarketResourceWithRawResponse(client.market)
        self.options = resources.OptionsResourceWithRawResponse(client.options)


class AsyncUnusualwhalesWithRawResponse:
    def __init__(self, client: AsyncUnusualwhales) -> None:
        self.stocks = resources.AsyncStocksResourceWithRawResponse(client.stocks)
        self.congress = resources.AsyncCongressResourceWithRawResponse(client.congress)
        self.institutions = resources.AsyncInstitutionsResourceWithRawResponse(client.institutions)
        self.darkpool = resources.AsyncDarkpoolResourceWithRawResponse(client.darkpool)
        self.etf = resources.AsyncEtfResourceWithRawResponse(client.etf)
        self.options_flows = resources.AsyncOptionsFlowsResourceWithRawResponse(client.options_flows)
        self.seasonality = resources.AsyncSeasonalityResourceWithRawResponse(client.seasonality)
        self.insider_trades = resources.AsyncInsiderTradesResourceWithRawResponse(client.insider_trades)
        self.spike = resources.AsyncSpikeResourceWithRawResponse(client.spike)
        self.calendar = resources.AsyncCalendarResourceWithRawResponse(client.calendar)
        self.correlations = resources.AsyncCorrelationsResourceWithRawResponse(client.correlations)
        self.analyst = resources.AsyncAnalystResourceWithRawResponse(client.analyst)
        self.market = resources.AsyncMarketResourceWithRawResponse(client.market)
        self.options = resources.AsyncOptionsResourceWithRawResponse(client.options)


class UnusualwhalesWithStreamedResponse:
    def __init__(self, client: Unusualwhales) -> None:
        self.stocks = resources.StocksResourceWithStreamingResponse(client.stocks)
        self.congress = resources.CongressResourceWithStreamingResponse(client.congress)
        self.institutions = resources.InstitutionsResourceWithStreamingResponse(client.institutions)
        self.darkpool = resources.DarkpoolResourceWithStreamingResponse(client.darkpool)
        self.etf = resources.EtfResourceWithStreamingResponse(client.etf)
        self.options_flows = resources.OptionsFlowsResourceWithStreamingResponse(client.options_flows)
        self.seasonality = resources.SeasonalityResourceWithStreamingResponse(client.seasonality)
        self.insider_trades = resources.InsiderTradesResourceWithStreamingResponse(client.insider_trades)
        self.spike = resources.SpikeResourceWithStreamingResponse(client.spike)
        self.calendar = resources.CalendarResourceWithStreamingResponse(client.calendar)
        self.correlations = resources.CorrelationsResourceWithStreamingResponse(client.correlations)
        self.analyst = resources.AnalystResourceWithStreamingResponse(client.analyst)
        self.market = resources.MarketResourceWithStreamingResponse(client.market)
        self.options = resources.OptionsResourceWithStreamingResponse(client.options)


class AsyncUnusualwhalesWithStreamedResponse:
    def __init__(self, client: AsyncUnusualwhales) -> None:
        self.stocks = resources.AsyncStocksResourceWithStreamingResponse(client.stocks)
        self.congress = resources.AsyncCongressResourceWithStreamingResponse(client.congress)
        self.institutions = resources.AsyncInstitutionsResourceWithStreamingResponse(client.institutions)
        self.darkpool = resources.AsyncDarkpoolResourceWithStreamingResponse(client.darkpool)
        self.etf = resources.AsyncEtfResourceWithStreamingResponse(client.etf)
        self.options_flows = resources.AsyncOptionsFlowsResourceWithStreamingResponse(client.options_flows)
        self.seasonality = resources.AsyncSeasonalityResourceWithStreamingResponse(client.seasonality)
        self.insider_trades = resources.AsyncInsiderTradesResourceWithStreamingResponse(client.insider_trades)
        self.spike = resources.AsyncSpikeResourceWithStreamingResponse(client.spike)
        self.calendar = resources.AsyncCalendarResourceWithStreamingResponse(client.calendar)
        self.correlations = resources.AsyncCorrelationsResourceWithStreamingResponse(client.correlations)
        self.analyst = resources.AsyncAnalystResourceWithStreamingResponse(client.analyst)
        self.market = resources.AsyncMarketResourceWithStreamingResponse(client.market)
        self.options = resources.AsyncOptionsResourceWithStreamingResponse(client.options)


Client = Unusualwhales

AsyncClient = AsyncUnusualwhales
