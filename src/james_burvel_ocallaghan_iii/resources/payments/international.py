# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

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
from ...types.payments import international_initiate_params
from ...types.payments.international_payment_status import InternationalPaymentStatus

__all__ = ["InternationalResource", "AsyncInternationalResource"]


class InternationalResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> InternationalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return InternationalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> InternationalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return InternationalResourceWithStreamingResponse(self)

    def initiate(
        self,
        *,
        amount: float,
        beneficiary: international_initiate_params.Beneficiary,
        purpose: str,
        source_account_id: str,
        source_currency: str,
        target_currency: str,
        fx_rate_lock: bool | Omit = omit,
        fx_rate_provider: Literal["proprietary_ai", "market_rate"] | Omit = omit,
        reference: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InternationalPaymentStatus:
        """
        Facilitates the secure initiation of an international wire transfer to a
        beneficiary in another country and currency, leveraging optimal FX rates and
        tracking capabilities.

        Args:
          amount: The amount to send in the source currency.

          beneficiary: Details of the payment beneficiary.

          purpose: Purpose of the payment.

          source_account_id: The ID of the user's source account for the payment.

          source_currency: The ISO 4217 currency code of the source funds.

          target_currency: The ISO 4217 currency code for the beneficiary's currency.

          fx_rate_lock: If true, attempts to lock the quoted FX rate for a short period.

          fx_rate_provider: Indicates whether to use AI-optimized FX rates or standard market rates.

          reference: Optional: Your internal reference for this payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/payments/international/initiate",
            body=maybe_transform(
                {
                    "amount": amount,
                    "beneficiary": beneficiary,
                    "purpose": purpose,
                    "source_account_id": source_account_id,
                    "source_currency": source_currency,
                    "target_currency": target_currency,
                    "fx_rate_lock": fx_rate_lock,
                    "fx_rate_provider": fx_rate_provider,
                    "reference": reference,
                },
                international_initiate_params.InternationalInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InternationalPaymentStatus,
        )

    def retrieve_status(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InternationalPaymentStatus:
        """
        Retrieves the current processing status and details of an initiated
        international payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return self._get(
            f"/payments/international/{payment_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InternationalPaymentStatus,
        )


class AsyncInternationalResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncInternationalResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncInternationalResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncInternationalResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncInternationalResourceWithStreamingResponse(self)

    async def initiate(
        self,
        *,
        amount: float,
        beneficiary: international_initiate_params.Beneficiary,
        purpose: str,
        source_account_id: str,
        source_currency: str,
        target_currency: str,
        fx_rate_lock: bool | Omit = omit,
        fx_rate_provider: Literal["proprietary_ai", "market_rate"] | Omit = omit,
        reference: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InternationalPaymentStatus:
        """
        Facilitates the secure initiation of an international wire transfer to a
        beneficiary in another country and currency, leveraging optimal FX rates and
        tracking capabilities.

        Args:
          amount: The amount to send in the source currency.

          beneficiary: Details of the payment beneficiary.

          purpose: Purpose of the payment.

          source_account_id: The ID of the user's source account for the payment.

          source_currency: The ISO 4217 currency code of the source funds.

          target_currency: The ISO 4217 currency code for the beneficiary's currency.

          fx_rate_lock: If true, attempts to lock the quoted FX rate for a short period.

          fx_rate_provider: Indicates whether to use AI-optimized FX rates or standard market rates.

          reference: Optional: Your internal reference for this payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/payments/international/initiate",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "beneficiary": beneficiary,
                    "purpose": purpose,
                    "source_account_id": source_account_id,
                    "source_currency": source_currency,
                    "target_currency": target_currency,
                    "fx_rate_lock": fx_rate_lock,
                    "fx_rate_provider": fx_rate_provider,
                    "reference": reference,
                },
                international_initiate_params.InternationalInitiateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InternationalPaymentStatus,
        )

    async def retrieve_status(
        self,
        payment_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InternationalPaymentStatus:
        """
        Retrieves the current processing status and details of an initiated
        international payment.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not payment_id:
            raise ValueError(f"Expected a non-empty value for `payment_id` but received {payment_id!r}")
        return await self._get(
            f"/payments/international/{payment_id}/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InternationalPaymentStatus,
        )


class InternationalResourceWithRawResponse:
    def __init__(self, international: InternationalResource) -> None:
        self._international = international

        self.initiate = to_raw_response_wrapper(
            international.initiate,
        )
        self.retrieve_status = to_raw_response_wrapper(
            international.retrieve_status,
        )


class AsyncInternationalResourceWithRawResponse:
    def __init__(self, international: AsyncInternationalResource) -> None:
        self._international = international

        self.initiate = async_to_raw_response_wrapper(
            international.initiate,
        )
        self.retrieve_status = async_to_raw_response_wrapper(
            international.retrieve_status,
        )


class InternationalResourceWithStreamingResponse:
    def __init__(self, international: InternationalResource) -> None:
        self._international = international

        self.initiate = to_streamed_response_wrapper(
            international.initiate,
        )
        self.retrieve_status = to_streamed_response_wrapper(
            international.retrieve_status,
        )


class AsyncInternationalResourceWithStreamingResponse:
    def __init__(self, international: AsyncInternationalResource) -> None:
        self._international = international

        self.initiate = async_to_streamed_response_wrapper(
            international.initiate,
        )
        self.retrieve_status = async_to_streamed_response_wrapper(
            international.retrieve_status,
        )
