# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.users.me import preference_update_params
from ....types.users.me.user_preferences import UserPreferences

__all__ = ["PreferencesResource", "AsyncPreferencesResource"]


class PreferencesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return PreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return PreferencesResourceWithStreamingResponse(self)

    def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserPreferences:
        """
        Retrieves the user's deep personalization preferences, including AI
        customization settings, notification channel priorities, thematic choices, and
        data sharing consents.
        """
        return self._get(
            "/users/me/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPreferences,
        )

    def update(
        self,
        *,
        ai_interaction_mode: Literal["proactive", "balanced", "on_demand"] | Omit = omit,
        data_sharing_consent: object | Omit = omit,
        notification_channels: preference_update_params.NotificationChannels | Omit = omit,
        preferred_language: object | Omit = omit,
        theme: object | Omit = omit,
        transaction_grouping: Literal["category", "merchant", "date", "account"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserPreferences:
        """
        Updates the user's deep personalization preferences, allowing dynamic control
        over AI behavior, notification delivery, thematic choices, and data privacy
        settings.

        Args:
          ai_interaction_mode: How the user prefers to interact with AI (proactive advice, balanced, or only on
              demand).

          data_sharing_consent: Consent status for sharing anonymized data for AI improvement and personalized
              offers.

          notification_channels: Preferred channels for receiving notifications.

          preferred_language: Preferred language for the user interface.

          theme: Preferred UI theme (e.g., Light-Default, Dark-Quantum).

          transaction_grouping: Default grouping preference for transaction lists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            "/users/me/preferences",
            body=maybe_transform(
                {
                    "ai_interaction_mode": ai_interaction_mode,
                    "data_sharing_consent": data_sharing_consent,
                    "notification_channels": notification_channels,
                    "preferred_language": preferred_language,
                    "theme": theme,
                    "transaction_grouping": transaction_grouping,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPreferences,
        )


class AsyncPreferencesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPreferencesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPreferencesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPreferencesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncPreferencesResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserPreferences:
        """
        Retrieves the user's deep personalization preferences, including AI
        customization settings, notification channel priorities, thematic choices, and
        data sharing consents.
        """
        return await self._get(
            "/users/me/preferences",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPreferences,
        )

    async def update(
        self,
        *,
        ai_interaction_mode: Literal["proactive", "balanced", "on_demand"] | Omit = omit,
        data_sharing_consent: object | Omit = omit,
        notification_channels: preference_update_params.NotificationChannels | Omit = omit,
        preferred_language: object | Omit = omit,
        theme: object | Omit = omit,
        transaction_grouping: Literal["category", "merchant", "date", "account"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> UserPreferences:
        """
        Updates the user's deep personalization preferences, allowing dynamic control
        over AI behavior, notification delivery, thematic choices, and data privacy
        settings.

        Args:
          ai_interaction_mode: How the user prefers to interact with AI (proactive advice, balanced, or only on
              demand).

          data_sharing_consent: Consent status for sharing anonymized data for AI improvement and personalized
              offers.

          notification_channels: Preferred channels for receiving notifications.

          preferred_language: Preferred language for the user interface.

          theme: Preferred UI theme (e.g., Light-Default, Dark-Quantum).

          transaction_grouping: Default grouping preference for transaction lists.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            "/users/me/preferences",
            body=await async_maybe_transform(
                {
                    "ai_interaction_mode": ai_interaction_mode,
                    "data_sharing_consent": data_sharing_consent,
                    "notification_channels": notification_channels,
                    "preferred_language": preferred_language,
                    "theme": theme,
                    "transaction_grouping": transaction_grouping,
                },
                preference_update_params.PreferenceUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=UserPreferences,
        )


class PreferencesResourceWithRawResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_raw_response_wrapper(
            preferences.update,
        )


class AsyncPreferencesResourceWithRawResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_raw_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            preferences.update,
        )


class PreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: PreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            preferences.update,
        )


class AsyncPreferencesResourceWithStreamingResponse:
    def __init__(self, preferences: AsyncPreferencesResource) -> None:
        self._preferences = preferences

        self.retrieve = async_to_streamed_response_wrapper(
            preferences.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            preferences.update,
        )
