# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ...types import sustainability_purchase_carbon_offsets_params
from ..._types import Body, Query, Headers, NotGiven, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .investments import (
    InvestmentsResource,
    AsyncInvestmentsResource,
    InvestmentsResourceWithRawResponse,
    AsyncInvestmentsResourceWithRawResponse,
    InvestmentsResourceWithStreamingResponse,
    AsyncInvestmentsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from ...types.sustainability_purchase_carbon_offsets_response import SustainabilityPurchaseCarbonOffsetsResponse
from ...types.sustainability_retrieve_carbon_footprint_response import SustainabilityRetrieveCarbonFootprintResponse

__all__ = ["SustainabilityResource", "AsyncSustainabilityResource"]


class SustainabilityResource(SyncAPIResource):
    @cached_property
    def investments(self) -> InvestmentsResource:
        return InvestmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> SustainabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return SustainabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SustainabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return SustainabilityResourceWithStreamingResponse(self)

    def purchase_carbon_offsets(
        self,
        *,
        amount_kg_co2e: float,
        offset_project: Optional[str],
        payment_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SustainabilityPurchaseCarbonOffsetsResponse:
        """
        Allows users to purchase carbon offsets to neutralize their estimated carbon
        footprint, supporting environmental initiatives.

        Args:
          amount_kg_co2e: The amount of carbon dioxide equivalent to offset in kilograms.

          offset_project: Optional: The specific carbon offset project to support.

          payment_account_id: The ID of the user's account to use for payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/sustainability/carbon-offsets",
            body=maybe_transform(
                {
                    "amount_kg_co2e": amount_kg_co2e,
                    "offset_project": offset_project,
                    "payment_account_id": payment_account_id,
                },
                sustainability_purchase_carbon_offsets_params.SustainabilityPurchaseCarbonOffsetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SustainabilityPurchaseCarbonOffsetsResponse,
        )

    def retrieve_carbon_footprint(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SustainabilityRetrieveCarbonFootprintResponse:
        """
        Generates a detailed report of the user's estimated carbon footprint based on
        transaction data, lifestyle choices, and AI-driven impact assessments, offering
        insights and reduction strategies.
        """
        return self._get(
            "/sustainability/carbon-footprint",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SustainabilityRetrieveCarbonFootprintResponse,
        )


class AsyncSustainabilityResource(AsyncAPIResource):
    @cached_property
    def investments(self) -> AsyncInvestmentsResource:
        return AsyncInvestmentsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncSustainabilityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSustainabilityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSustainabilityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncSustainabilityResourceWithStreamingResponse(self)

    async def purchase_carbon_offsets(
        self,
        *,
        amount_kg_co2e: float,
        offset_project: Optional[str],
        payment_account_id: str,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SustainabilityPurchaseCarbonOffsetsResponse:
        """
        Allows users to purchase carbon offsets to neutralize their estimated carbon
        footprint, supporting environmental initiatives.

        Args:
          amount_kg_co2e: The amount of carbon dioxide equivalent to offset in kilograms.

          offset_project: Optional: The specific carbon offset project to support.

          payment_account_id: The ID of the user's account to use for payment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/sustainability/carbon-offsets",
            body=await async_maybe_transform(
                {
                    "amount_kg_co2e": amount_kg_co2e,
                    "offset_project": offset_project,
                    "payment_account_id": payment_account_id,
                },
                sustainability_purchase_carbon_offsets_params.SustainabilityPurchaseCarbonOffsetsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SustainabilityPurchaseCarbonOffsetsResponse,
        )

    async def retrieve_carbon_footprint(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SustainabilityRetrieveCarbonFootprintResponse:
        """
        Generates a detailed report of the user's estimated carbon footprint based on
        transaction data, lifestyle choices, and AI-driven impact assessments, offering
        insights and reduction strategies.
        """
        return await self._get(
            "/sustainability/carbon-footprint",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SustainabilityRetrieveCarbonFootprintResponse,
        )


class SustainabilityResourceWithRawResponse:
    def __init__(self, sustainability: SustainabilityResource) -> None:
        self._sustainability = sustainability

        self.purchase_carbon_offsets = to_raw_response_wrapper(
            sustainability.purchase_carbon_offsets,
        )
        self.retrieve_carbon_footprint = to_raw_response_wrapper(
            sustainability.retrieve_carbon_footprint,
        )

    @cached_property
    def investments(self) -> InvestmentsResourceWithRawResponse:
        return InvestmentsResourceWithRawResponse(self._sustainability.investments)


class AsyncSustainabilityResourceWithRawResponse:
    def __init__(self, sustainability: AsyncSustainabilityResource) -> None:
        self._sustainability = sustainability

        self.purchase_carbon_offsets = async_to_raw_response_wrapper(
            sustainability.purchase_carbon_offsets,
        )
        self.retrieve_carbon_footprint = async_to_raw_response_wrapper(
            sustainability.retrieve_carbon_footprint,
        )

    @cached_property
    def investments(self) -> AsyncInvestmentsResourceWithRawResponse:
        return AsyncInvestmentsResourceWithRawResponse(self._sustainability.investments)


class SustainabilityResourceWithStreamingResponse:
    def __init__(self, sustainability: SustainabilityResource) -> None:
        self._sustainability = sustainability

        self.purchase_carbon_offsets = to_streamed_response_wrapper(
            sustainability.purchase_carbon_offsets,
        )
        self.retrieve_carbon_footprint = to_streamed_response_wrapper(
            sustainability.retrieve_carbon_footprint,
        )

    @cached_property
    def investments(self) -> InvestmentsResourceWithStreamingResponse:
        return InvestmentsResourceWithStreamingResponse(self._sustainability.investments)


class AsyncSustainabilityResourceWithStreamingResponse:
    def __init__(self, sustainability: AsyncSustainabilityResource) -> None:
        self._sustainability = sustainability

        self.purchase_carbon_offsets = async_to_streamed_response_wrapper(
            sustainability.purchase_carbon_offsets,
        )
        self.retrieve_carbon_footprint = async_to_streamed_response_wrapper(
            sustainability.retrieve_carbon_footprint,
        )

    @cached_property
    def investments(self) -> AsyncInvestmentsResourceWithStreamingResponse:
        return AsyncInvestmentsResourceWithStreamingResponse(self._sustainability.investments)
