# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .kyc import (
    KYCResource,
    AsyncKYCResource,
    KYCResourceWithRawResponse,
    AsyncKYCResourceWithRawResponse,
    KYCResourceWithStreamingResponse,
    AsyncKYCResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["IdentityResource", "AsyncIdentityResource"]


class IdentityResource(SyncAPIResource):
    @cached_property
    def kyc(self) -> KYCResource:
        return KYCResource(self._client)

    @cached_property
    def with_raw_response(self) -> IdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return IdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> IdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return IdentityResourceWithStreamingResponse(self)


class AsyncIdentityResource(AsyncAPIResource):
    @cached_property
    def kyc(self) -> AsyncKYCResource:
        return AsyncKYCResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncIdentityResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncIdentityResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncIdentityResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncIdentityResourceWithStreamingResponse(self)


class IdentityResourceWithRawResponse:
    def __init__(self, identity: IdentityResource) -> None:
        self._identity = identity

    @cached_property
    def kyc(self) -> KYCResourceWithRawResponse:
        return KYCResourceWithRawResponse(self._identity.kyc)


class AsyncIdentityResourceWithRawResponse:
    def __init__(self, identity: AsyncIdentityResource) -> None:
        self._identity = identity

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithRawResponse:
        return AsyncKYCResourceWithRawResponse(self._identity.kyc)


class IdentityResourceWithStreamingResponse:
    def __init__(self, identity: IdentityResource) -> None:
        self._identity = identity

    @cached_property
    def kyc(self) -> KYCResourceWithStreamingResponse:
        return KYCResourceWithStreamingResponse(self._identity.kyc)


class AsyncIdentityResourceWithStreamingResponse:
    def __init__(self, identity: AsyncIdentityResource) -> None:
        self._identity = identity

    @cached_property
    def kyc(self) -> AsyncKYCResourceWithStreamingResponse:
        return AsyncKYCResourceWithStreamingResponse(self._identity.kyc)
