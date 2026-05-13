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
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return ApplicationsResource(self._client)

    @cached_property
    def offers(self) -> OffersResource:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return OffersResource(self._client)

    @cached_property
    def with_raw_response(self) -> LendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return LendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> LendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return LendingResourceWithStreamingResponse(self)


class AsyncLendingResource(AsyncAPIResource):
    @cached_property
    def applications(self) -> AsyncApplicationsResource:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return AsyncApplicationsResource(self._client)

    @cached_property
    def offers(self) -> AsyncOffersResource:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return AsyncOffersResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncLendingResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncLendingResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncLendingResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncLendingResourceWithStreamingResponse(self)


class LendingResourceWithRawResponse:
    def __init__(self, lending: LendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> ApplicationsResourceWithRawResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return ApplicationsResourceWithRawResponse(self._lending.applications)

    @cached_property
    def offers(self) -> OffersResourceWithRawResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return OffersResourceWithRawResponse(self._lending.offers)


class AsyncLendingResourceWithRawResponse:
    def __init__(self, lending: AsyncLendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return AsyncApplicationsResourceWithRawResponse(self._lending.applications)

    @cached_property
    def offers(self) -> AsyncOffersResourceWithRawResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return AsyncOffersResourceWithRawResponse(self._lending.offers)


class LendingResourceWithStreamingResponse:
    def __init__(self, lending: LendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> ApplicationsResourceWithStreamingResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return ApplicationsResourceWithStreamingResponse(self._lending.applications)

    @cached_property
    def offers(self) -> OffersResourceWithStreamingResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return OffersResourceWithStreamingResponse(self._lending.offers)


class AsyncLendingResourceWithStreamingResponse:
    def __init__(self, lending: AsyncLendingResource) -> None:
        self._lending = lending

    @cached_property
    def applications(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return AsyncApplicationsResourceWithStreamingResponse(self._lending.applications)

    @cached_property
    def offers(self) -> AsyncOffersResourceWithStreamingResponse:
        """
        Comprehensive access to credit scores, detailed history, AI-generated improvement plans, and personalized lending offers with instant underwriting.
        """
        return AsyncOffersResourceWithStreamingResponse(self._lending.offers)
