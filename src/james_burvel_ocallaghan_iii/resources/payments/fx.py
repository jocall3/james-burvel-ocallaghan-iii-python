# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.payments import fx_convert_params, fx_retrieve_rates_params
from ...types.payments.fx_convert_response import FxConvertResponse
from ...types.payments.fx_retrieve_rates_response import FxRetrieveRatesResponse

__all__ = ["FxResource", "AsyncFxResource"]


class FxResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> FxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return FxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> FxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return FxResourceWithStreamingResponse(self)

    def convert(
        self,
        *,
        source_account_id: object,
        source_amount: object,
        source_currency: object,
        target_currency: object,
        fx_rate_lock: object | Omit = omit,
        target_account_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FxConvertResponse:
        """
        Executes an instant currency conversion between two currencies, either from a
        balance or into a specified account.

        Args:
          source_account_id: The ID of the account from which funds will be converted.

          source_amount: The amount to convert from the source currency.

          source_currency: The ISO 4217 currency code of the source funds.

          target_currency: The ISO 4217 currency code for the target currency.

          fx_rate_lock: If true, attempts to lock the quoted FX rate for a short period.

          target_account_id: Optional: The ID of the account to deposit the converted funds. If null, funds
              are held in a wallet/balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments/fx/convert",
            body=maybe_transform(
                {
                    "source_account_id": source_account_id,
                    "source_amount": source_amount,
                    "source_currency": source_currency,
                    "target_currency": target_currency,
                    "fx_rate_lock": fx_rate_lock,
                    "target_account_id": target_account_id,
                },
                fx_convert_params.FxConvertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FxConvertResponse,
        )

    def retrieve_rates(
        self,
        *,
        base_currency: object,
        target_currency: object,
        forecast_days: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FxRetrieveRatesResponse:
        """
        Retrieves current and AI-predicted future foreign exchange rates for a specified
        currency pair, including bid/ask spreads and historical volatility data for
        informed decisions.

        Args:
          base_currency: The base currency code (e.g., USD).

          target_currency: The target currency code (e.g., EUR).

          forecast_days: Number of days into the future to provide an AI-driven prediction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/payments/fx/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "base_currency": base_currency,
                        "target_currency": target_currency,
                        "forecast_days": forecast_days,
                    },
                    fx_retrieve_rates_params.FxRetrieveRatesParams,
                ),
            ),
            cast_to=FxRetrieveRatesResponse,
        )


class AsyncFxResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncFxResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncFxResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncFxResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncFxResourceWithStreamingResponse(self)

    async def convert(
        self,
        *,
        source_account_id: object,
        source_amount: object,
        source_currency: object,
        target_currency: object,
        fx_rate_lock: object | Omit = omit,
        target_account_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FxConvertResponse:
        """
        Executes an instant currency conversion between two currencies, either from a
        balance or into a specified account.

        Args:
          source_account_id: The ID of the account from which funds will be converted.

          source_amount: The amount to convert from the source currency.

          source_currency: The ISO 4217 currency code of the source funds.

          target_currency: The ISO 4217 currency code for the target currency.

          fx_rate_lock: If true, attempts to lock the quoted FX rate for a short period.

          target_account_id: Optional: The ID of the account to deposit the converted funds. If null, funds
              are held in a wallet/balance.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments/fx/convert",
            body=await async_maybe_transform(
                {
                    "source_account_id": source_account_id,
                    "source_amount": source_amount,
                    "source_currency": source_currency,
                    "target_currency": target_currency,
                    "fx_rate_lock": fx_rate_lock,
                    "target_account_id": target_account_id,
                },
                fx_convert_params.FxConvertParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FxConvertResponse,
        )

    async def retrieve_rates(
        self,
        *,
        base_currency: object,
        target_currency: object,
        forecast_days: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FxRetrieveRatesResponse:
        """
        Retrieves current and AI-predicted future foreign exchange rates for a specified
        currency pair, including bid/ask spreads and historical volatility data for
        informed decisions.

        Args:
          base_currency: The base currency code (e.g., USD).

          target_currency: The target currency code (e.g., EUR).

          forecast_days: Number of days into the future to provide an AI-driven prediction.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/payments/fx/rates",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "base_currency": base_currency,
                        "target_currency": target_currency,
                        "forecast_days": forecast_days,
                    },
                    fx_retrieve_rates_params.FxRetrieveRatesParams,
                ),
            ),
            cast_to=FxRetrieveRatesResponse,
        )


class FxResourceWithRawResponse:
    def __init__(self, fx: FxResource) -> None:
        self._fx = fx

        self.convert = to_raw_response_wrapper(
            fx.convert,
        )
        self.retrieve_rates = to_raw_response_wrapper(
            fx.retrieve_rates,
        )


class AsyncFxResourceWithRawResponse:
    def __init__(self, fx: AsyncFxResource) -> None:
        self._fx = fx

        self.convert = async_to_raw_response_wrapper(
            fx.convert,
        )
        self.retrieve_rates = async_to_raw_response_wrapper(
            fx.retrieve_rates,
        )


class FxResourceWithStreamingResponse:
    def __init__(self, fx: FxResource) -> None:
        self._fx = fx

        self.convert = to_streamed_response_wrapper(
            fx.convert,
        )
        self.retrieve_rates = to_streamed_response_wrapper(
            fx.retrieve_rates,
        )


class AsyncFxResourceWithStreamingResponse:
    def __init__(self, fx: AsyncFxResource) -> None:
        self._fx = fx

        self.convert = async_to_streamed_response_wrapper(
            fx.convert,
        )
        self.retrieve_rates = async_to_streamed_response_wrapper(
            fx.retrieve_rates,
        )
