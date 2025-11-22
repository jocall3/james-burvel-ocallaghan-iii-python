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
from ...types.marketplace import product_list_params, product_claim_offer_params, product_simulate_purchase_params
from ...types.marketplace.product_list_response import ProductListResponse
from ...types.marketplace.product_claim_offer_response import ProductClaimOfferResponse
from ...types.marketplace.product_simulate_purchase_response import ProductSimulatePurchaseResponse

__all__ = ["ProductsResource", "AsyncProductsResource"]


class ProductsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return ProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return ProductsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        category: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListResponse:
        """
        Retrieves a list of personalized product recommendations from the Plato AI
        Marketplace.

        Args:
          category: Filter products by category.

          limit: Maximum number of items to return.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/marketplace/products",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "offset": offset,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
        )

    def claim_offer(
        self,
        product_id: str,
        *,
        redemption_channel: Literal["email", "in_app", "external_link"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductClaimOfferResponse:
        """
        Allows the user to claim an exclusive, personalized offer for a marketplace
        product, often involving a discount code or special terms that are then linked
        to their account.

        Args:
          redemption_channel: Preferred channel for offer redemption details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._post(
            f"/marketplace/products/{product_id}/claim-offer",
            body=maybe_transform(
                {"redemption_channel": redemption_channel}, product_claim_offer_params.ProductClaimOfferParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductClaimOfferResponse,
        )

    def simulate_purchase(
        self,
        product_id: str,
        *,
        purchase_option: Literal["full_payment", "financed_12_months", "financed_24_months"],
        target_account_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductSimulatePurchaseResponse:
        """
        Uses Quantum Oracle AI to simulate the short-term and long-term financial impact
        of purchasing a specific marketplace product on the user's budget and cash flow.

        Args:
          purchase_option: The payment method to simulate.

          target_account_id: Optional: The account from which the purchase would be made. If omitted, AI will
              infer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._post(
            f"/marketplace/products/{product_id}/simulate-purchase",
            body=maybe_transform(
                {
                    "purchase_option": purchase_option,
                    "target_account_id": target_account_id,
                },
                product_simulate_purchase_params.ProductSimulatePurchaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductSimulatePurchaseResponse,
        )


class AsyncProductsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncProductsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncProductsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncProductsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncProductsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        category: str | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListResponse:
        """
        Retrieves a list of personalized product recommendations from the Plato AI
        Marketplace.

        Args:
          category: Filter products by category.

          limit: Maximum number of items to return.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/marketplace/products",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "category": category,
                        "limit": limit,
                        "offset": offset,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
        )

    async def claim_offer(
        self,
        product_id: str,
        *,
        redemption_channel: Literal["email", "in_app", "external_link"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductClaimOfferResponse:
        """
        Allows the user to claim an exclusive, personalized offer for a marketplace
        product, often involving a discount code or special terms that are then linked
        to their account.

        Args:
          redemption_channel: Preferred channel for offer redemption details.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._post(
            f"/marketplace/products/{product_id}/claim-offer",
            body=await async_maybe_transform(
                {"redemption_channel": redemption_channel}, product_claim_offer_params.ProductClaimOfferParams
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductClaimOfferResponse,
        )

    async def simulate_purchase(
        self,
        product_id: str,
        *,
        purchase_option: Literal["full_payment", "financed_12_months", "financed_24_months"],
        target_account_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductSimulatePurchaseResponse:
        """
        Uses Quantum Oracle AI to simulate the short-term and long-term financial impact
        of purchasing a specific marketplace product on the user's budget and cash flow.

        Args:
          purchase_option: The payment method to simulate.

          target_account_id: Optional: The account from which the purchase would be made. If omitted, AI will
              infer.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._post(
            f"/marketplace/products/{product_id}/simulate-purchase",
            body=await async_maybe_transform(
                {
                    "purchase_option": purchase_option,
                    "target_account_id": target_account_id,
                },
                product_simulate_purchase_params.ProductSimulatePurchaseParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductSimulatePurchaseResponse,
        )


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_raw_response_wrapper(
            products.list,
        )
        self.claim_offer = to_raw_response_wrapper(
            products.claim_offer,
        )
        self.simulate_purchase = to_raw_response_wrapper(
            products.simulate_purchase,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_raw_response_wrapper(
            products.list,
        )
        self.claim_offer = async_to_raw_response_wrapper(
            products.claim_offer,
        )
        self.simulate_purchase = async_to_raw_response_wrapper(
            products.simulate_purchase,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_streamed_response_wrapper(
            products.list,
        )
        self.claim_offer = to_streamed_response_wrapper(
            products.claim_offer,
        )
        self.simulate_purchase = to_streamed_response_wrapper(
            products.simulate_purchase,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
        self.claim_offer = async_to_streamed_response_wrapper(
            products.claim_offer,
        )
        self.simulate_purchase = async_to_streamed_response_wrapper(
            products.simulate_purchase,
        )
