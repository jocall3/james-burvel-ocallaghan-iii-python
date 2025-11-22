# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

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
from ...types.marketplace import (
    product_list_params,
    product_simulate_purchase_params,
    product_redeem_marketplace_offer_params,
)
from ...types.marketplace.product_list_response import ProductListResponse
from ...types.marketplace.product_simulate_purchase_response import ProductSimulatePurchaseResponse
from ...types.marketplace.product_redeem_marketplace_offer_response import ProductRedeemMarketplaceOfferResponse

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
        ai_personalization_level: Literal["low", "medium", "high"] | Omit = omit,
        category: Literal[
            "loans", "insurance", "credit_cards", "investments", "budgeting_tools", "smart_home", "travel", "education"
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        min_rating: float | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListResponse:
        """
        Retrieves a personalized, AI-curated list of products and services from the
        Plato AI marketplace, tailored to the user's financial profile, goals, and
        spending patterns. Includes options for filtering and advanced search.

        Args:
          ai_personalization_level: Filter by AI personalization level (e.g., low, medium, high). 'High' means
              highly relevant to user's specific needs.

          category: Filter products by category (e.g., loans, insurance, credit_cards, investments).

          limit: Maximum number of items to return in a single page.

          min_rating: Minimum user rating for products (0-5).

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
                        "ai_personalization_level": ai_personalization_level,
                        "category": category,
                        "limit": limit,
                        "min_rating": min_rating,
                        "offset": offset,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
        )

    def redeem_marketplace_offer(
        self,
        offer_id: str,
        *,
        payment_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRedeemMarketplaceOfferResponse:
        """
        Redeems a personalized, exclusive offer from the Plato AI marketplace, often
        resulting in a discount, special rate, or credit to the user's account.

        Args:
          payment_account_id: Optional: The ID of the account to use for any associated payment or credit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offer_id:
            raise ValueError(f"Expected a non-empty value for `offer_id` but received {offer_id!r}")
        return self._post(
            f"/marketplace/offers/{offer_id}/redeem",
            body=maybe_transform(
                {"payment_account_id": payment_account_id},
                product_redeem_marketplace_offer_params.ProductRedeemMarketplaceOfferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRedeemMarketplaceOfferResponse,
        )

    def simulate_purchase(
        self,
        product_id: str,
        *,
        simulation_parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductSimulatePurchaseResponse:
        """
        Uses the Quantum Oracle to simulate the long-term financial impact of purchasing
        or subscribing to a specific marketplace product, such as a loan, investment, or
        insurance policy, on the user's overall financial health and goals.

        Args:
          simulation_parameters: Dynamic parameters specific to the product type (e.g., loan amount, investment
              term).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return self._post(
            f"/marketplace/products/{product_id}/impact-simulate",
            body=maybe_transform(
                {"simulation_parameters": simulation_parameters},
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
        ai_personalization_level: Literal["low", "medium", "high"] | Omit = omit,
        category: Literal[
            "loans", "insurance", "credit_cards", "investments", "budgeting_tools", "smart_home", "travel", "education"
        ]
        | Omit = omit,
        limit: int | Omit = omit,
        min_rating: float | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductListResponse:
        """
        Retrieves a personalized, AI-curated list of products and services from the
        Plato AI marketplace, tailored to the user's financial profile, goals, and
        spending patterns. Includes options for filtering and advanced search.

        Args:
          ai_personalization_level: Filter by AI personalization level (e.g., low, medium, high). 'High' means
              highly relevant to user's specific needs.

          category: Filter products by category (e.g., loans, insurance, credit_cards, investments).

          limit: Maximum number of items to return in a single page.

          min_rating: Minimum user rating for products (0-5).

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
                        "ai_personalization_level": ai_personalization_level,
                        "category": category,
                        "limit": limit,
                        "min_rating": min_rating,
                        "offset": offset,
                    },
                    product_list_params.ProductListParams,
                ),
            ),
            cast_to=ProductListResponse,
        )

    async def redeem_marketplace_offer(
        self,
        offer_id: str,
        *,
        payment_account_id: str | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductRedeemMarketplaceOfferResponse:
        """
        Redeems a personalized, exclusive offer from the Plato AI marketplace, often
        resulting in a discount, special rate, or credit to the user's account.

        Args:
          payment_account_id: Optional: The ID of the account to use for any associated payment or credit.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not offer_id:
            raise ValueError(f"Expected a non-empty value for `offer_id` but received {offer_id!r}")
        return await self._post(
            f"/marketplace/offers/{offer_id}/redeem",
            body=await async_maybe_transform(
                {"payment_account_id": payment_account_id},
                product_redeem_marketplace_offer_params.ProductRedeemMarketplaceOfferParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=ProductRedeemMarketplaceOfferResponse,
        )

    async def simulate_purchase(
        self,
        product_id: str,
        *,
        simulation_parameters: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> ProductSimulatePurchaseResponse:
        """
        Uses the Quantum Oracle to simulate the long-term financial impact of purchasing
        or subscribing to a specific marketplace product, such as a loan, investment, or
        insurance policy, on the user's overall financial health and goals.

        Args:
          simulation_parameters: Dynamic parameters specific to the product type (e.g., loan amount, investment
              term).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not product_id:
            raise ValueError(f"Expected a non-empty value for `product_id` but received {product_id!r}")
        return await self._post(
            f"/marketplace/products/{product_id}/impact-simulate",
            body=await async_maybe_transform(
                {"simulation_parameters": simulation_parameters},
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
        self.redeem_marketplace_offer = to_raw_response_wrapper(
            products.redeem_marketplace_offer,
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
        self.redeem_marketplace_offer = async_to_raw_response_wrapper(
            products.redeem_marketplace_offer,
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
        self.redeem_marketplace_offer = to_streamed_response_wrapper(
            products.redeem_marketplace_offer,
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
        self.redeem_marketplace_offer = async_to_streamed_response_wrapper(
            products.redeem_marketplace_offer,
        )
        self.simulate_purchase = async_to_streamed_response_wrapper(
            products.simulate_purchase,
        )
