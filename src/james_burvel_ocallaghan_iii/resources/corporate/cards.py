# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ...types.corporate import (
    card_freeze_params,
    card_create_virtual_params,
    card_update_controls_params,
    card_list_transactions_params,
)
from ...types.paginated_transactions import PaginatedTransactions
from ...types.corporate.corporate_card import CorporateCard
from ...types.corporate.card_list_response import CardListResponse
from ...types.corporate.corporate_card_controls_param import CorporateCardControlsParam

__all__ = ["CardsResource", "AsyncCardsResource"]


class CardsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> CardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return CardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> CardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return CardsResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Retrieves a comprehensive list of all physical and virtual corporate cards
        associated with the user's organization, including their status, assigned
        holder, and current spending controls.
        """
        return self._get(
            "/corporate/cards",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardListResponse,
        )

    def create_virtual(
        self,
        *,
        controls: CorporateCardControlsParam,
        expiration_date: Union[str, date],
        holder_name: str,
        purpose: str,
        associated_employee_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CorporateCard:
        """
        Creates and issues a new virtual corporate card with specified spending limits,
        merchant restrictions, and expiration dates, ideal for secure online purchases
        and temporary projects.

        Args:
          controls: Specific spending controls for this virtual card.

          expiration_date: Expiration date for the virtual card.

          holder_name: Name for the virtual card holder or its purpose.

          purpose: Brief description of the virtual card's intended use.

          associated_employee_id: Optional: Employee ID to associate with this virtual card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/cards/virtual",
            body=maybe_transform(
                {
                    "controls": controls,
                    "expiration_date": expiration_date,
                    "holder_name": holder_name,
                    "purpose": purpose,
                    "associated_employee_id": associated_employee_id,
                },
                card_create_virtual_params.CardCreateVirtualParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorporateCard,
        )

    def freeze(
        self,
        card_id: str,
        *,
        freeze: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CorporateCard:
        """
        Immediately changes the frozen status of a corporate card, preventing or
        allowing transactions in real-time, critical for security and expense
        management.

        Args:
          freeze: Set to `true` to freeze the card, `false` to unfreeze.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._post(
            f"/corporate/cards/{card_id}/freeze",
            body=maybe_transform({"freeze": freeze}, card_freeze_params.CardFreezeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorporateCard,
        )

    def list_transactions(
        self,
        card_id: str,
        *,
        end_date: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTransactions:
        """
        Retrieves a paginated list of transactions made with a specific corporate card,
        including AI categorization and compliance flags.

        Args:
          end_date: Filter results up to this date (inclusive, YYYY-MM-DD).

          limit: Maximum number of items to return.

          offset: Number of items to skip before starting to collect the result set.

          start_date: Filter results from this date (inclusive, YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._get(
            f"/corporate/cards/{card_id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "start_date": start_date,
                    },
                    card_list_transactions_params.CardListTransactionsParams,
                ),
            ),
            cast_to=PaginatedTransactions,
        )

    def update_controls(
        self,
        card_id: str,
        *,
        atm_withdrawals: bool | Omit = omit,
        contactless_payments: bool | Omit = omit,
        daily_limit: Optional[float] | Omit = omit,
        international_transactions: bool | Omit = omit,
        merchant_category_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        monthly_limit: Optional[float] | Omit = omit,
        online_transactions: bool | Omit = omit,
        single_transaction_limit: Optional[float] | Omit = omit,
        vendor_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CorporateCard:
        """
        Updates the sophisticated spending controls, limits, and policy overrides for a
        specific corporate card, enabling real-time adjustments for security and budget
        adherence.

        Args:
          atm_withdrawals: Allow ATM withdrawals.

          contactless_payments: Allow contactless payments.

          daily_limit: Maximum spending limit per day.

          international_transactions: Allow international transactions.

          merchant_category_restrictions: List of allowed or disallowed merchant categories.

          monthly_limit: Maximum spending limit per month.

          online_transactions: Allow online transactions.

          single_transaction_limit: Maximum amount for a single transaction.

          vendor_restrictions: List of specific allowed or disallowed vendors/merchants.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return self._put(
            f"/corporate/cards/{card_id}/controls",
            body=maybe_transform(
                {
                    "atm_withdrawals": atm_withdrawals,
                    "contactless_payments": contactless_payments,
                    "daily_limit": daily_limit,
                    "international_transactions": international_transactions,
                    "merchant_category_restrictions": merchant_category_restrictions,
                    "monthly_limit": monthly_limit,
                    "online_transactions": online_transactions,
                    "single_transaction_limit": single_transaction_limit,
                    "vendor_restrictions": vendor_restrictions,
                },
                card_update_controls_params.CardUpdateControlsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorporateCard,
        )


class AsyncCardsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncCardsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncCardsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncCardsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncCardsResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CardListResponse:
        """
        Retrieves a comprehensive list of all physical and virtual corporate cards
        associated with the user's organization, including their status, assigned
        holder, and current spending controls.
        """
        return await self._get(
            "/corporate/cards",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CardListResponse,
        )

    async def create_virtual(
        self,
        *,
        controls: CorporateCardControlsParam,
        expiration_date: Union[str, date],
        holder_name: str,
        purpose: str,
        associated_employee_id: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CorporateCard:
        """
        Creates and issues a new virtual corporate card with specified spending limits,
        merchant restrictions, and expiration dates, ideal for secure online purchases
        and temporary projects.

        Args:
          controls: Specific spending controls for this virtual card.

          expiration_date: Expiration date for the virtual card.

          holder_name: Name for the virtual card holder or its purpose.

          purpose: Brief description of the virtual card's intended use.

          associated_employee_id: Optional: Employee ID to associate with this virtual card.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/cards/virtual",
            body=await async_maybe_transform(
                {
                    "controls": controls,
                    "expiration_date": expiration_date,
                    "holder_name": holder_name,
                    "purpose": purpose,
                    "associated_employee_id": associated_employee_id,
                },
                card_create_virtual_params.CardCreateVirtualParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorporateCard,
        )

    async def freeze(
        self,
        card_id: str,
        *,
        freeze: bool,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CorporateCard:
        """
        Immediately changes the frozen status of a corporate card, preventing or
        allowing transactions in real-time, critical for security and expense
        management.

        Args:
          freeze: Set to `true` to freeze the card, `false` to unfreeze.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._post(
            f"/corporate/cards/{card_id}/freeze",
            body=await async_maybe_transform({"freeze": freeze}, card_freeze_params.CardFreezeParams),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorporateCard,
        )

    async def list_transactions(
        self,
        card_id: str,
        *,
        end_date: Union[str, date] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PaginatedTransactions:
        """
        Retrieves a paginated list of transactions made with a specific corporate card,
        including AI categorization and compliance flags.

        Args:
          end_date: Filter results up to this date (inclusive, YYYY-MM-DD).

          limit: Maximum number of items to return.

          offset: Number of items to skip before starting to collect the result set.

          start_date: Filter results from this date (inclusive, YYYY-MM-DD).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._get(
            f"/corporate/cards/{card_id}/transactions",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "limit": limit,
                        "offset": offset,
                        "start_date": start_date,
                    },
                    card_list_transactions_params.CardListTransactionsParams,
                ),
            ),
            cast_to=PaginatedTransactions,
        )

    async def update_controls(
        self,
        card_id: str,
        *,
        atm_withdrawals: bool | Omit = omit,
        contactless_payments: bool | Omit = omit,
        daily_limit: Optional[float] | Omit = omit,
        international_transactions: bool | Omit = omit,
        merchant_category_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        monthly_limit: Optional[float] | Omit = omit,
        online_transactions: bool | Omit = omit,
        single_transaction_limit: Optional[float] | Omit = omit,
        vendor_restrictions: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> CorporateCard:
        """
        Updates the sophisticated spending controls, limits, and policy overrides for a
        specific corporate card, enabling real-time adjustments for security and budget
        adherence.

        Args:
          atm_withdrawals: Allow ATM withdrawals.

          contactless_payments: Allow contactless payments.

          daily_limit: Maximum spending limit per day.

          international_transactions: Allow international transactions.

          merchant_category_restrictions: List of allowed or disallowed merchant categories.

          monthly_limit: Maximum spending limit per month.

          online_transactions: Allow online transactions.

          single_transaction_limit: Maximum amount for a single transaction.

          vendor_restrictions: List of specific allowed or disallowed vendors/merchants.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not card_id:
            raise ValueError(f"Expected a non-empty value for `card_id` but received {card_id!r}")
        return await self._put(
            f"/corporate/cards/{card_id}/controls",
            body=await async_maybe_transform(
                {
                    "atm_withdrawals": atm_withdrawals,
                    "contactless_payments": contactless_payments,
                    "daily_limit": daily_limit,
                    "international_transactions": international_transactions,
                    "merchant_category_restrictions": merchant_category_restrictions,
                    "monthly_limit": monthly_limit,
                    "online_transactions": online_transactions,
                    "single_transaction_limit": single_transaction_limit,
                    "vendor_restrictions": vendor_restrictions,
                },
                card_update_controls_params.CardUpdateControlsParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=CorporateCard,
        )


class CardsResourceWithRawResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.list = to_raw_response_wrapper(
            cards.list,
        )
        self.create_virtual = to_raw_response_wrapper(
            cards.create_virtual,
        )
        self.freeze = to_raw_response_wrapper(
            cards.freeze,
        )
        self.list_transactions = to_raw_response_wrapper(
            cards.list_transactions,
        )
        self.update_controls = to_raw_response_wrapper(
            cards.update_controls,
        )


class AsyncCardsResourceWithRawResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.list = async_to_raw_response_wrapper(
            cards.list,
        )
        self.create_virtual = async_to_raw_response_wrapper(
            cards.create_virtual,
        )
        self.freeze = async_to_raw_response_wrapper(
            cards.freeze,
        )
        self.list_transactions = async_to_raw_response_wrapper(
            cards.list_transactions,
        )
        self.update_controls = async_to_raw_response_wrapper(
            cards.update_controls,
        )


class CardsResourceWithStreamingResponse:
    def __init__(self, cards: CardsResource) -> None:
        self._cards = cards

        self.list = to_streamed_response_wrapper(
            cards.list,
        )
        self.create_virtual = to_streamed_response_wrapper(
            cards.create_virtual,
        )
        self.freeze = to_streamed_response_wrapper(
            cards.freeze,
        )
        self.list_transactions = to_streamed_response_wrapper(
            cards.list_transactions,
        )
        self.update_controls = to_streamed_response_wrapper(
            cards.update_controls,
        )


class AsyncCardsResourceWithStreamingResponse:
    def __init__(self, cards: AsyncCardsResource) -> None:
        self._cards = cards

        self.list = async_to_streamed_response_wrapper(
            cards.list,
        )
        self.create_virtual = async_to_streamed_response_wrapper(
            cards.create_virtual,
        )
        self.freeze = async_to_streamed_response_wrapper(
            cards.freeze,
        )
        self.list_transactions = async_to_streamed_response_wrapper(
            cards.list_transactions,
        )
        self.update_controls = async_to_streamed_response_wrapper(
            cards.update_controls,
        )
