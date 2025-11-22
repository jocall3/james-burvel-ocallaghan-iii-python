# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..types import budget_create_params, budget_update_params
from .._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
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
from ..types.budget import Budget
from ..types.budget_list_response import BudgetListResponse

__all__ = ["BudgetsResource", "AsyncBudgetsResource"]


class BudgetsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> BudgetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return BudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> BudgetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return BudgetsResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        end_date: Union[str, date],
        name: str,
        period: Literal["weekly", "monthly", "quarterly", "annually", "custom"],
        start_date: Union[str, date],
        total_amount: float,
        ai_auto_populate: bool | Omit = omit,
        alert_threshold: Optional[int] | Omit = omit,
        categories: Optional[Iterable[budget_create_params.Category]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Budget:
        """
        Creates a new financial budget for the user, with optional AI auto-population of
        categories and amounts.

        Args:
          end_date: The end date of the budget period.

          name: Name of the new budget.

          period: The recurrence period of the budget.

          start_date: The start date of the budget period.

          total_amount: The total amount allocated for the budget.

          ai_auto_populate: If true, AI will automatically suggest and populate budget categories and
              amounts based on historical spending.

          alert_threshold: Percentage of budget spent at which an alert should be triggered.

          categories: Optional: Initial breakdown of the budget by categories. If omitted and
              `aiAutoPopulate` is true, AI will generate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/budgets",
            body=maybe_transform(
                {
                    "end_date": end_date,
                    "name": name,
                    "period": period,
                    "start_date": start_date,
                    "total_amount": total_amount,
                    "ai_auto_populate": ai_auto_populate,
                    "alert_threshold": alert_threshold,
                    "categories": categories,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
        )

    def retrieve(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Budget:
        """
        Retrieves detailed information for a specific budget, including current
        spending, remaining amounts, and AI recommendations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return self._get(
            f"/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
        )

    def update(
        self,
        budget_id: str,
        *,
        alert_threshold: Optional[int] | Omit = omit,
        categories: Iterable[budget_update_params.Category] | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        name: str | Omit = omit,
        period: Literal["weekly", "monthly", "quarterly", "annually", "custom"] | Omit = omit,
        reset_spent_amounts: bool | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        status: Literal["active", "completed", "archived", "overspent"] | Omit = omit,
        total_amount: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Budget:
        """
        Updates the parameters of an existing budget, such as total amount, dates, or
        categories.

        Args:
          alert_threshold: Updated percentage for budget alert threshold.

          categories: Updated breakdown of the budget by categories. Existing categories will be
              updated, new ones added.

          end_date: Updated end date of the budget period.

          name: Updated name of the budget.

          period: Updated recurrence period of the budget.

          reset_spent_amounts: If true, resets `spentAmount` for all categories and total to 0. Useful for
              starting a new cycle of a recurring budget.

          start_date: Updated start date of the budget period.

          status: Updated status of the budget.

          total_amount: Updated total allocated budget amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return self._put(
            f"/budgets/{budget_id}",
            body=maybe_transform(
                {
                    "alert_threshold": alert_threshold,
                    "categories": categories,
                    "end_date": end_date,
                    "name": name,
                    "period": period,
                    "reset_spent_amounts": reset_spent_amounts,
                    "start_date": start_date,
                    "status": status,
                    "total_amount": total_amount,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
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
    ) -> BudgetListResponse:
        """
        Retrieves a list of all active and historical budgets for the authenticated
        user.
        """
        return self._get(
            "/budgets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetListResponse,
        )

    def delete(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific budget from the user's profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class AsyncBudgetsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncBudgetsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncBudgetsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncBudgetsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncBudgetsResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        end_date: Union[str, date],
        name: str,
        period: Literal["weekly", "monthly", "quarterly", "annually", "custom"],
        start_date: Union[str, date],
        total_amount: float,
        ai_auto_populate: bool | Omit = omit,
        alert_threshold: Optional[int] | Omit = omit,
        categories: Optional[Iterable[budget_create_params.Category]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Budget:
        """
        Creates a new financial budget for the user, with optional AI auto-population of
        categories and amounts.

        Args:
          end_date: The end date of the budget period.

          name: Name of the new budget.

          period: The recurrence period of the budget.

          start_date: The start date of the budget period.

          total_amount: The total amount allocated for the budget.

          ai_auto_populate: If true, AI will automatically suggest and populate budget categories and
              amounts based on historical spending.

          alert_threshold: Percentage of budget spent at which an alert should be triggered.

          categories: Optional: Initial breakdown of the budget by categories. If omitted and
              `aiAutoPopulate` is true, AI will generate.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/budgets",
            body=await async_maybe_transform(
                {
                    "end_date": end_date,
                    "name": name,
                    "period": period,
                    "start_date": start_date,
                    "total_amount": total_amount,
                    "ai_auto_populate": ai_auto_populate,
                    "alert_threshold": alert_threshold,
                    "categories": categories,
                },
                budget_create_params.BudgetCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
        )

    async def retrieve(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Budget:
        """
        Retrieves detailed information for a specific budget, including current
        spending, remaining amounts, and AI recommendations.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return await self._get(
            f"/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
        )

    async def update(
        self,
        budget_id: str,
        *,
        alert_threshold: Optional[int] | Omit = omit,
        categories: Iterable[budget_update_params.Category] | Omit = omit,
        end_date: Union[str, date] | Omit = omit,
        name: str | Omit = omit,
        period: Literal["weekly", "monthly", "quarterly", "annually", "custom"] | Omit = omit,
        reset_spent_amounts: bool | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        status: Literal["active", "completed", "archived", "overspent"] | Omit = omit,
        total_amount: float | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Budget:
        """
        Updates the parameters of an existing budget, such as total amount, dates, or
        categories.

        Args:
          alert_threshold: Updated percentage for budget alert threshold.

          categories: Updated breakdown of the budget by categories. Existing categories will be
              updated, new ones added.

          end_date: Updated end date of the budget period.

          name: Updated name of the budget.

          period: Updated recurrence period of the budget.

          reset_spent_amounts: If true, resets `spentAmount` for all categories and total to 0. Useful for
              starting a new cycle of a recurring budget.

          start_date: Updated start date of the budget period.

          status: Updated status of the budget.

          total_amount: Updated total allocated budget amount.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        return await self._put(
            f"/budgets/{budget_id}",
            body=await async_maybe_transform(
                {
                    "alert_threshold": alert_threshold,
                    "categories": categories,
                    "end_date": end_date,
                    "name": name,
                    "period": period,
                    "reset_spent_amounts": reset_spent_amounts,
                    "start_date": start_date,
                    "status": status,
                    "total_amount": total_amount,
                },
                budget_update_params.BudgetUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Budget,
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
    ) -> BudgetListResponse:
        """
        Retrieves a list of all active and historical budgets for the authenticated
        user.
        """
        return await self._get(
            "/budgets",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=BudgetListResponse,
        )

    async def delete(
        self,
        budget_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Deletes a specific budget from the user's profile.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not budget_id:
            raise ValueError(f"Expected a non-empty value for `budget_id` but received {budget_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/budgets/{budget_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )


class BudgetsResourceWithRawResponse:
    def __init__(self, budgets: BudgetsResource) -> None:
        self._budgets = budgets

        self.create = to_raw_response_wrapper(
            budgets.create,
        )
        self.retrieve = to_raw_response_wrapper(
            budgets.retrieve,
        )
        self.update = to_raw_response_wrapper(
            budgets.update,
        )
        self.list = to_raw_response_wrapper(
            budgets.list,
        )
        self.delete = to_raw_response_wrapper(
            budgets.delete,
        )


class AsyncBudgetsResourceWithRawResponse:
    def __init__(self, budgets: AsyncBudgetsResource) -> None:
        self._budgets = budgets

        self.create = async_to_raw_response_wrapper(
            budgets.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            budgets.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            budgets.update,
        )
        self.list = async_to_raw_response_wrapper(
            budgets.list,
        )
        self.delete = async_to_raw_response_wrapper(
            budgets.delete,
        )


class BudgetsResourceWithStreamingResponse:
    def __init__(self, budgets: BudgetsResource) -> None:
        self._budgets = budgets

        self.create = to_streamed_response_wrapper(
            budgets.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            budgets.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            budgets.update,
        )
        self.list = to_streamed_response_wrapper(
            budgets.list,
        )
        self.delete = to_streamed_response_wrapper(
            budgets.delete,
        )


class AsyncBudgetsResourceWithStreamingResponse:
    def __init__(self, budgets: AsyncBudgetsResource) -> None:
        self._budgets = budgets

        self.create = async_to_streamed_response_wrapper(
            budgets.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            budgets.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            budgets.update,
        )
        self.list = async_to_streamed_response_wrapper(
            budgets.list,
        )
        self.delete = async_to_streamed_response_wrapper(
            budgets.delete,
        )
