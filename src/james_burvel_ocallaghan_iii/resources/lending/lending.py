# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .offers import (
    OffersResource,
    AsyncOffersResource,
    OffersResourceWithRawResponse,
    AsyncOffersResourceWithRawResponse,
    OffersResourceWithStreamingResponse,
    AsyncOffersResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from .applications import (
    ApplicationsResource,
    AsyncApplicationsResource,
    ApplicationsResourceWithRawResponse,
    AsyncApplicationsResourceWithRawResponse,
    ApplicationsResourceWithStreamingResponse,
    AsyncApplicationsResourceWithStreamingResponse,
)

__all__ = ["LendingResource", "AsyncLendingResource"]


class LendingResource(SyncAPIResource):
    @cached_property
    def applications(self) -> ApplicationsResource:
        return ApplicationsResource(self._client)

    @cached_property
    def offers(self) -> OffersResource:
        return OffersResource(self._client)

    @cached_property
    def with_raw_response(self) -> LendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return LendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return LendingResourceWithStreamingResponse(self)


class AsyncLendingResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        return AsyncApplicationsResource(self._client)

    @cached_property
    def offers(self) -> AsyncOffersResource:
        return AsyncOffersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncLendingResourceWithStreamingResponse(self)


class LendingResourceWithRawResponse:
    def __init__(self, lending: LendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        return ApplicationsResourceWithRawResponse(self._lending.applications)

    @cached_property
    def offers(self) -> OffersResourceWithRawResponse:
        return OffersResourceWithRawResponse(self._lending.offers)


class AsyncLendingResourceWithRawResponse:
    def __init__(self, lending: AsyncLendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        return AsyncApplicationsResourceWithRawResponse(self._lending.applications)

    @cached_property
    def offers(self) -> AsyncOffersResourceWithRawResponse:
        return AsyncOffersResourceWithRawResponse(self._lending.offers)


class LendingResourceWithStreamingResponse:
    def __init__(self, lending: LendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        return ApplicationsResourceWithStreamingResponse(self._lending.applications)

    @cached_property
    def offers(self) -> OffersResourceWithStreamingResponse:
        return OffersResourceWithStreamingResponse(self._lending.offers)


class AsyncLendingResourceWithStreamingResponse:
    def __init__(self, lending: AsyncLendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        return AsyncApplicationsResourceWithStreamingResponse(self._lending.applications)

    @cached_property
    def offers(self) -> AsyncOffersResourceWithStreamingResponse:
        return AsyncOffersResourceWithStreamingResponse(self._lending.offers)
