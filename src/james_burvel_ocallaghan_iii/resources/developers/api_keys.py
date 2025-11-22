# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional

import httpx

from ..._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.developers import api_key_create_params
from ...types.developers.api_key import APIKey
from ...types.developers.api_key_list_response import APIKeyListResponse

__all__ = ["APIKeysResource", "AsyncAPIKeysResource"]


class APIKeysResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> APIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return APIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> APIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return APIKeysResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        scopes: SequenceNotStr[str],
        expires_in_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Generates a new API key for the developer application with specified scopes and
        an optional expiration.

        Args:
          name: A descriptive name for the new API key.

          scopes: A list of OAuth2 scopes to grant to this API key.

          expires_in_days: Optional: Number of days until the API key expires. If omitted, the key does not
              expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/developers/api-keys",
            body=maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "expires_in_days": expires_in_days,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """Retrieves a list of API keys issued to the authenticated developer application."""
        return self._get(
            "/developers/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyListResponse,
        )

    def revoke(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revokes an existing API key, disabling its access immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/developers/api-keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncAPIKeysResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAPIKeysResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAPIKeysResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAPIKeysResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncAPIKeysResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        scopes: SequenceNotStr[str],
        expires_in_days: Optional[int] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKey:
        """
        Generates a new API key for the developer application with specified scopes and
        an optional expiration.

        Args:
          name: A descriptive name for the new API key.

          scopes: A list of OAuth2 scopes to grant to this API key.

          expires_in_days: Optional: Number of days until the API key expires. If omitted, the key does not
              expire.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/developers/api-keys",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "scopes": scopes,
                    "expires_in_days": expires_in_days,
                },
                api_key_create_params.APIKeyCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKey,
        )

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> APIKeyListResponse:
        """Retrieves a list of API keys issued to the authenticated developer application."""
        return await self._get(
            "/developers/api-keys",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=APIKeyListResponse,
        )

    async def revoke(
        self,
        key_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Revokes an existing API key, disabling its access immediately.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not key_id:
            raise ValueError(f"Expected a non-empty value for `key_id` but received {key_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/developers/api-keys/{key_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class APIKeysResourceWithRawResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_raw_response_wrapper(
            api_keys.create,
        )
        self.list = to_raw_response_wrapper(
            api_keys.list,
        )
        self.revoke = to_raw_response_wrapper(
            api_keys.revoke,
        )


class AsyncAPIKeysResourceWithRawResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_raw_response_wrapper(
            api_keys.create,
        )
        self.list = async_to_raw_response_wrapper(
            api_keys.list,
        )
        self.revoke = async_to_raw_response_wrapper(
            api_keys.revoke,
        )


class APIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: APIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = to_streamed_response_wrapper(
            api_keys.create,
        )
        self.list = to_streamed_response_wrapper(
            api_keys.list,
        )
        self.revoke = to_streamed_response_wrapper(
            api_keys.revoke,
        )


class AsyncAPIKeysResourceWithStreamingResponse:
    def __init__(self, api_keys: AsyncAPIKeysResource) -> None:
        self._api_keys = api_keys

        self.create = async_to_streamed_response_wrapper(
            api_keys.create,
        )
        self.list = async_to_streamed_response_wrapper(
            api_keys.list,
        )
        self.revoke = async_to_streamed_response_wrapper(
            api_keys.revoke,
        )
