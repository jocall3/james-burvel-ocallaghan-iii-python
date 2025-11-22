# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.transactions import recurring_create_params
from ...types.transactions.recurring_transaction import RecurringTransaction
from ...types.transactions.recurring_list_response import RecurringListResponse

__all__ = ["RecurringResource", "AsyncRecurringResource"]


class RecurringResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> RecurringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return RecurringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> RecurringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return RecurringResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        amount: float,
        category: str,
        currency: str,
        description: str,
        frequency: Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"],
        start_date: Union[str, date],
        linked_account_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecurringTransaction:
        """
        Defines a new recurring transaction pattern for future tracking and budgeting.

        Args:
          amount: The expected amount of the recurring transaction.

          category: Category of the recurring transaction.

          currency: The currency of the transaction (ISO 4217 code).

          description: Description for the new recurring transaction.

          frequency: How often the transaction is expected to occur.

          start_date: The date the first recurring transaction is expected.

          linked_account_id: Optional: The account from which this recurring transaction will be paid or
              received.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/transactions/recurring",
            body=maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "currency": currency,
                    "description": description,
                    "frequency": frequency,
                    "start_date": start_date,
                    "linked_account_id": linked_account_id,
                },
                recurring_create_params.RecurringCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurringTransaction,
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
    ) -> RecurringListResponse:
        """
        Retrieves a list of all detected or user-defined recurring transactions, useful
        for budget tracking and subscription management.
        """
        return self._get(
            "/transactions/recurring",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurringListResponse,
        )


class AsyncRecurringResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncRecurringResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncRecurringResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncRecurringResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncRecurringResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        amount: float,
        category: str,
        currency: str,
        description: str,
        frequency: Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"],
        start_date: Union[str, date],
        linked_account_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> RecurringTransaction:
        """
        Defines a new recurring transaction pattern for future tracking and budgeting.

        Args:
          amount: The expected amount of the recurring transaction.

          category: Category of the recurring transaction.

          currency: The currency of the transaction (ISO 4217 code).

          description: Description for the new recurring transaction.

          frequency: How often the transaction is expected to occur.

          start_date: The date the first recurring transaction is expected.

          linked_account_id: Optional: The account from which this recurring transaction will be paid or
              received.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/transactions/recurring",
            body=await async_maybe_transform(
                {
                    "amount": amount,
                    "category": category,
                    "currency": currency,
                    "description": description,
                    "frequency": frequency,
                    "start_date": start_date,
                    "linked_account_id": linked_account_id,
                },
                recurring_create_params.RecurringCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurringTransaction,
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
    ) -> RecurringListResponse:
        """
        Retrieves a list of all detected or user-defined recurring transactions, useful
        for budget tracking and subscription management.
        """
        return await self._get(
            "/transactions/recurring",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=RecurringListResponse,
        )


class RecurringResourceWithRawResponse:
    def __init__(self, recurring: RecurringResource) -> None:
        self._recurring = recurring

        self.create = to_raw_response_wrapper(
            recurring.create,
        )
        self.list = to_raw_response_wrapper(
            recurring.list,
        )


class AsyncRecurringResourceWithRawResponse:
    def __init__(self, recurring: AsyncRecurringResource) -> None:
        self._recurring = recurring

        self.create = async_to_raw_response_wrapper(
            recurring.create,
        )
        self.list = async_to_raw_response_wrapper(
            recurring.list,
        )


class RecurringResourceWithStreamingResponse:
    def __init__(self, recurring: RecurringResource) -> None:
        self._recurring = recurring

        self.create = to_streamed_response_wrapper(
            recurring.create,
        )
        self.list = to_streamed_response_wrapper(
            recurring.list,
        )


class AsyncRecurringResourceWithStreamingResponse:
    def __init__(self, recurring: AsyncRecurringResource) -> None:
        self._recurring = recurring

        self.create = async_to_streamed_response_wrapper(
            recurring.create,
        )
        self.list = async_to_streamed_response_wrapper(
            recurring.list,
        )
