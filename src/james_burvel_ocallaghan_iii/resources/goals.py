# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import goal_list_params, goal_create_params, goal_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, SequenceNotStr, omit, not_given
from .._utils import maybe_transform, async_maybe_transform
from .._compat import cached_property
from .._resource import SyncAPIResource, AsyncAPIResource
from .._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from .._base_client import make_request_options
from ..types.financial_goal import FinancialGoal
from ..types.goal_list_response import GoalListResponse

__all__ = ["GoalsResource", "AsyncGoalsResource"]


class GoalsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GoalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return GoalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GoalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return GoalsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        name: str,
        target_amount: float,
        target_date: Union[str, date],
        type: Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "other"],
        contributing_accounts: Optional[SequenceNotStr[str]] | Omit = omit,
        generate_ai_plan: bool | Omit = omit,
        initial_contribution: float | Omit = omit,
        risk_tolerance: Optional[Literal["conservative", "moderate", "aggressive"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGoal:
        """
        Creates a new long-term financial goal, with optional AI plan generation.

        Args:
          name: Name of the new financial goal.

          target_amount: The target monetary amount for the goal.

          target_date: The target completion date for the goal.

          type: Type of financial goal.

          contributing_accounts: Optional: List of account IDs initially contributing to this goal.

          generate_ai_plan: If true, AI will automatically generate a strategic plan for the goal.

          initial_contribution: Optional: Initial amount to contribute to the goal.

          risk_tolerance: Desired risk tolerance for investments related to this goal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/goals",
            body=maybe_transform(
                {
                    "name": name,
                    "target_amount": target_amount,
                    "target_date": target_date,
                    "type": type,
                    "contributing_accounts": contributing_accounts,
                    "generate_ai_plan": generate_ai_plan,
                    "initial_contribution": initial_contribution,
                    "risk_tolerance": risk_tolerance,
                },
                goal_create_params.GoalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGoal,
        )

    def retrieve(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGoal:
        """
        Retrieves detailed information for a specific financial goal, including current
        progress, AI strategic plan, and related insights.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return self._get(
            f"/goals/{goal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGoal,
        )

    def update(
        self,
        goal_id: str,
        *,
        contributing_accounts: Optional[SequenceNotStr[str]] | Omit = omit,
        generate_ai_plan: bool | Omit = omit,
        name: str | Omit = omit,
        risk_tolerance: Optional[Literal["conservative", "moderate", "aggressive"]] | Omit = omit,
        status: Literal["on_track", "behind_schedule", "ahead_of_schedule", "completed", "paused", "cancelled"]
        | Omit = omit,
        target_amount: float | Omit = omit,
        target_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGoal:
        """
        Updates the parameters of an existing financial goal, such as target amount,
        date, or contributing accounts. This may trigger an AI plan recalculation.

        Args:
          contributing_accounts: Updated list of account IDs contributing to this goal.

          generate_ai_plan: If true, AI will recalculate and update the strategic plan for the goal.

          name: Updated name of the financial goal.

          risk_tolerance: Updated risk tolerance for investments related to this goal.

          status: Updated status of the goal's progress.

          target_amount: The updated target monetary amount for the goal.

          target_date: The updated target completion date for the goal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return self._put(
            f"/goals/{goal_id}",
            body=maybe_transform(
                {
                    "contributing_accounts": contributing_accounts,
                    "generate_ai_plan": generate_ai_plan,
                    "name": name,
                    "risk_tolerance": risk_tolerance,
                    "status": status,
                    "target_amount": target_amount,
                    "target_date": target_date,
                },
                goal_update_params.GoalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGoal,
        )

    def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalListResponse:
        """
        Retrieves a list of all financial goals defined by the user, including their
        progress and associated AI plans.

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/goals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    goal_list_params.GoalListParams,
                ),
            ),
            cast_to=GoalListResponse,
        )

    def delete(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific financial goal from the user's profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/goals/{goal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncGoalsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGoalsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGoalsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGoalsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncGoalsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        name: str,
        target_amount: float,
        target_date: Union[str, date],
        type: Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "other"],
        contributing_accounts: Optional[SequenceNotStr[str]] | Omit = omit,
        generate_ai_plan: bool | Omit = omit,
        initial_contribution: float | Omit = omit,
        risk_tolerance: Optional[Literal["conservative", "moderate", "aggressive"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGoal:
        """
        Creates a new long-term financial goal, with optional AI plan generation.

        Args:
          name: Name of the new financial goal.

          target_amount: The target monetary amount for the goal.

          target_date: The target completion date for the goal.

          type: Type of financial goal.

          contributing_accounts: Optional: List of account IDs initially contributing to this goal.

          generate_ai_plan: If true, AI will automatically generate a strategic plan for the goal.

          initial_contribution: Optional: Initial amount to contribute to the goal.

          risk_tolerance: Desired risk tolerance for investments related to this goal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/goals",
            body=await async_maybe_transform(
                {
                    "name": name,
                    "target_amount": target_amount,
                    "target_date": target_date,
                    "type": type,
                    "contributing_accounts": contributing_accounts,
                    "generate_ai_plan": generate_ai_plan,
                    "initial_contribution": initial_contribution,
                    "risk_tolerance": risk_tolerance,
                },
                goal_create_params.GoalCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGoal,
        )

    async def retrieve(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGoal:
        """
        Retrieves detailed information for a specific financial goal, including current
        progress, AI strategic plan, and related insights.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return await self._get(
            f"/goals/{goal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGoal,
        )

    async def update(
        self,
        goal_id: str,
        *,
        contributing_accounts: Optional[SequenceNotStr[str]] | Omit = omit,
        generate_ai_plan: bool | Omit = omit,
        name: str | Omit = omit,
        risk_tolerance: Optional[Literal["conservative", "moderate", "aggressive"]] | Omit = omit,
        status: Literal["on_track", "behind_schedule", "ahead_of_schedule", "completed", "paused", "cancelled"]
        | Omit = omit,
        target_amount: float | Omit = omit,
        target_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialGoal:
        """
        Updates the parameters of an existing financial goal, such as target amount,
        date, or contributing accounts. This may trigger an AI plan recalculation.

        Args:
          contributing_accounts: Updated list of account IDs contributing to this goal.

          generate_ai_plan: If true, AI will recalculate and update the strategic plan for the goal.

          name: Updated name of the financial goal.

          risk_tolerance: Updated risk tolerance for investments related to this goal.

          status: Updated status of the goal's progress.

          target_amount: The updated target monetary amount for the goal.

          target_date: The updated target completion date for the goal.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        return await self._put(
            f"/goals/{goal_id}",
            body=await async_maybe_transform(
                {
                    "contributing_accounts": contributing_accounts,
                    "generate_ai_plan": generate_ai_plan,
                    "name": name,
                    "risk_tolerance": risk_tolerance,
                    "status": status,
                    "target_amount": target_amount,
                    "target_date": target_date,
                },
                goal_update_params.GoalUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialGoal,
        )

    async def list(
        self,
        *,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GoalListResponse:
        """
        Retrieves a list of all financial goals defined by the user, including their
        progress and associated AI plans.

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/goals",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    goal_list_params.GoalListParams,
                ),
            ),
            cast_to=GoalListResponse,
        )

    async def delete(
        self,
        goal_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific financial goal from the user's profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not goal_id:
            raise ValueError(f"Expected a non-empty value for `goal_id` but received {goal_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/goals/{goal_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class GoalsResourceWithRawResponse:
    def __init__(self, goals: GoalsResource) -> None:
        self._goals = goals

        self.create = to_raw_response_wrapper(
            goals.create,
        )
        self.retrieve = to_raw_response_wrapper(
            goals.retrieve,
        )
        self.update = to_raw_response_wrapper(
            goals.update,
        )
        self.list = to_raw_response_wrapper(
            goals.list,
        )
        self.delete = to_raw_response_wrapper(
            goals.delete,
        )


class AsyncGoalsResourceWithRawResponse:
    def __init__(self, goals: AsyncGoalsResource) -> None:
        self._goals = goals

        self.create = async_to_raw_response_wrapper(
            goals.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            goals.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            goals.update,
        )
        self.list = async_to_raw_response_wrapper(
            goals.list,
        )
        self.delete = async_to_raw_response_wrapper(
            goals.delete,
        )


class GoalsResourceWithStreamingResponse:
    def __init__(self, goals: GoalsResource) -> None:
        self._goals = goals

        self.create = to_streamed_response_wrapper(
            goals.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            goals.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            goals.update,
        )
        self.list = to_streamed_response_wrapper(
            goals.list,
        )
        self.delete = to_streamed_response_wrapper(
            goals.delete,
        )


class AsyncGoalsResourceWithStreamingResponse:
    def __init__(self, goals: AsyncGoalsResource) -> None:
        self._goals = goals

        self.create = async_to_streamed_response_wrapper(
            goals.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            goals.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            goals.update,
        )
        self.list = async_to_streamed_response_wrapper(
            goals.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            goals.delete,
        )
