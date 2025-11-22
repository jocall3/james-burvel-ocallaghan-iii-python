# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .api_keys import (
    APIKeysResource,
    AsyncAPIKeysResource,
    APIKeysResourceWithRawResponse,
    AsyncAPIKeysResourceWithRawResponse,
    APIKeysResourceWithStreamingResponse,
    AsyncAPIKeysResourceWithStreamingResponse,
)
from .webhooks import (
    WebhooksResource,
    AsyncWebhooksResource,
    WebhooksResourceWithRawResponse,
    AsyncWebhooksResourceWithRawResponse,
    WebhooksResourceWithStreamingResponse,
    AsyncWebhooksResourceWithStreamingResponse,
)
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["DevelopersResource", "AsyncDevelopersResource"]


class DevelopersResource(SyncAPIResource):
    @cached_property
    def webhooks(self) -> WebhooksResource:
        return WebhooksResource(self._client)

    @cached_property
    def api_keys(self) -> APIKeysResource:
        return APIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> DevelopersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return DevelopersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevelopersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return DevelopersResourceWithStreamingResponse(self)


class AsyncDevelopersResource(AsyncAPIResource):
    @cached_property
    def webhooks(self) -> AsyncWebhooksResource:
        return AsyncWebhooksResource(self._client)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResource:
        return AsyncAPIKeysResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncDevelopersResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevelopersResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevelopersResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncDevelopersResourceWithStreamingResponse(self)


class DevelopersResourceWithRawResponse:
    def __init__(self, developers: DevelopersResource) -> None:
        self._developers = developers

    @cached_property
    def webhooks(self) -> WebhooksResourceWithRawResponse:
        return WebhooksResourceWithRawResponse(self._developers.webhooks)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithRawResponse:
        return APIKeysResourceWithRawResponse(self._developers.api_keys)


class AsyncDevelopersResourceWithRawResponse:
    def __init__(self, developers: AsyncDevelopersResource) -> None:
        self._developers = developers

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithRawResponse:
        return AsyncWebhooksResourceWithRawResponse(self._developers.webhooks)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithRawResponse:
        return AsyncAPIKeysResourceWithRawResponse(self._developers.api_keys)


class DevelopersResourceWithStreamingResponse:
    def __init__(self, developers: DevelopersResource) -> None:
        self._developers = developers

    @cached_property
    def webhooks(self) -> WebhooksResourceWithStreamingResponse:
        return WebhooksResourceWithStreamingResponse(self._developers.webhooks)

    @cached_property
    def api_keys(self) -> APIKeysResourceWithStreamingResponse:
        return APIKeysResourceWithStreamingResponse(self._developers.api_keys)


class AsyncDevelopersResourceWithStreamingResponse:
    def __init__(self, developers: AsyncDevelopersResource) -> None:
        self._developers = developers

    @cached_property
    def webhooks(self) -> AsyncWebhooksResourceWithStreamingResponse:
        return AsyncWebhooksResourceWithStreamingResponse(self._developers.webhooks)

    @cached_property
    def api_keys(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        return AsyncAPIKeysResourceWithStreamingResponse(self._developers.api_keys)
