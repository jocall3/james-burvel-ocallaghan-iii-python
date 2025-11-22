# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .products import (
    ProductsResource,
    AsyncProductsResource,
    ProductsResourceWithRawResponse,
    AsyncProductsResourceWithRawResponse,
    ProductsResourceWithStreamingResponse,
    AsyncProductsResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["MarketplaceResource", "AsyncMarketplaceResource"]


class MarketplaceResource(SyncAPIResource):
    @cached_property
    def products(self) -> ProductsResource:
        return ProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> MarketplaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return MarketplaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> MarketplaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return MarketplaceResourceWithStreamingResponse(self)


class AsyncMarketplaceResource(AsyncAPIResource):
    @cached_property
    def products(self) -> AsyncProductsResource:
        return AsyncProductsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncMarketplaceResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncMarketplaceResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncMarketplaceResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncMarketplaceResourceWithStreamingResponse(self)


class MarketplaceResourceWithRawResponse:
    def __init__(self, marketplace: MarketplaceResource) -> None:
        self._marketplace = marketplace

    @cached_property
    def products(self) -> ProductsResourceWithRawResponse:
        return ProductsResourceWithRawResponse(self._marketplace.products)


class AsyncMarketplaceResourceWithRawResponse:
    def __init__(self, marketplace: AsyncMarketplaceResource) -> None:
        self._marketplace = marketplace

    @cached_property
    def products(self) -> AsyncProductsResourceWithRawResponse:
        return AsyncProductsResourceWithRawResponse(self._marketplace.products)


class MarketplaceResourceWithStreamingResponse:
    def __init__(self, marketplace: MarketplaceResource) -> None:
        self._marketplace = marketplace

    @cached_property
    def products(self) -> ProductsResourceWithStreamingResponse:
        return ProductsResourceWithStreamingResponse(self._marketplace.products)


class AsyncMarketplaceResourceWithStreamingResponse:
    def __init__(self, marketplace: AsyncMarketplaceResource) -> None:
        self._marketplace = marketplace

    @cached_property
    def products(self) -> AsyncProductsResourceWithStreamingResponse:
        return AsyncProductsResourceWithStreamingResponse(self._marketplace.products)
