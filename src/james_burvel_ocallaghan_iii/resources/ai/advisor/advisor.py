# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import httpx

from .chat import (
    ChatResource,
    AsyncChatResource,
    ChatResourceWithRawResponse,
    AsyncChatResourceWithRawResponse,
    ChatResourceWithStreamingResponse,
    AsyncChatResourceWithStreamingResponse,
)
from ...._types import Body, Query, Headers, NotGiven, not_given
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.advisor_list_tools_response import AdvisorListToolsResponse

__all__ = ["AdvisorResource", "AsyncAdvisorResource"]


class AdvisorResource(SyncAPIResource):
    @cached_property
    def chat(self) -> ChatResource:
        return ChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AdvisorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AdvisorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AdvisorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AdvisorResourceWithStreamingResponse(self)

    def list_tools(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvisorListToolsResponse:
        """
        Retrieves a dynamic manifest of all integrated AI tools that Quantum can invoke
        and execute, providing details on their capabilities, parameters, and access
        requirements.
        """
        return self._get(
            "/ai/advisor/tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvisorListToolsResponse,
        )


class AsyncAdvisorResource(AsyncAPIResource):
    @cached_property
    def chat(self) -> AsyncChatResource:
        return AsyncChatResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAdvisorResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAdvisorResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAdvisorResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncAdvisorResourceWithStreamingResponse(self)

    async def list_tools(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvisorListToolsResponse:
        """
        Retrieves a dynamic manifest of all integrated AI tools that Quantum can invoke
        and execute, providing details on their capabilities, parameters, and access
        requirements.
        """
        return await self._get(
            "/ai/advisor/tools",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvisorListToolsResponse,
        )


class AdvisorResourceWithRawResponse:
    def __init__(self, advisor: AdvisorResource) -> None:
        self._advisor = advisor

        self.list_tools = to_raw_response_wrapper(
            advisor.list_tools,
        )

    @cached_property
    def chat(self) -> ChatResourceWithRawResponse:
        return ChatResourceWithRawResponse(self._advisor.chat)


class AsyncAdvisorResourceWithRawResponse:
    def __init__(self, advisor: AsyncAdvisorResource) -> None:
        self._advisor = advisor

        self.list_tools = async_to_raw_response_wrapper(
            advisor.list_tools,
        )

    @cached_property
    def chat(self) -> AsyncChatResourceWithRawResponse:
        return AsyncChatResourceWithRawResponse(self._advisor.chat)


class AdvisorResourceWithStreamingResponse:
    def __init__(self, advisor: AdvisorResource) -> None:
        self._advisor = advisor

        self.list_tools = to_streamed_response_wrapper(
            advisor.list_tools,
        )

    @cached_property
    def chat(self) -> ChatResourceWithStreamingResponse:
        return ChatResourceWithStreamingResponse(self._advisor.chat)


class AsyncAdvisorResourceWithStreamingResponse:
    def __init__(self, advisor: AsyncAdvisorResource) -> None:
        self._advisor = advisor

        self.list_tools = async_to_streamed_response_wrapper(
            advisor.list_tools,
        )

    @cached_property
    def chat(self) -> AsyncChatResourceWithStreamingResponse:
        return AsyncChatResourceWithStreamingResponse(self._advisor.chat)
