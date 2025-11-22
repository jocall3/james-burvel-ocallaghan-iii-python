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
from ...types.marketplace import product_list_params
from ...types.marketplace.product_list_response import ProductListResponse

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


class ProductsResourceWithRawResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_raw_response_wrapper(
            products.list,
        )


class AsyncProductsResourceWithRawResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_raw_response_wrapper(
            products.list,
        )


class ProductsResourceWithStreamingResponse:
    def __init__(self, products: ProductsResource) -> None:
        self._products = products

        self.list = to_streamed_response_wrapper(
            products.list,
        )


class AsyncProductsResourceWithStreamingResponse:
    def __init__(self, products: AsyncProductsResource) -> None:
        self._products = products

        self.list = async_to_streamed_response_wrapper(
            products.list,
        )
