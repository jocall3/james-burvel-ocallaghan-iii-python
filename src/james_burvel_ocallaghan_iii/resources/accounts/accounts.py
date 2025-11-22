# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...types import account_link_new_institution_params, account_retrieve_account_statements_params
from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    to_custom_raw_response_wrapper,
    async_to_streamed_response_wrapper,
    to_custom_streamed_response_wrapper,
    async_to_custom_raw_response_wrapper,
    async_to_custom_streamed_response_wrapper,
)
from .transactions import (
    TransactionsResource,
    AsyncTransactionsResource,
    TransactionsResourceWithRawResponse,
    AsyncTransactionsResourceWithRawResponse,
    TransactionsResourceWithStreamingResponse,
    AsyncTransactionsResourceWithStreamingResponse,
)
from ..._base_client import make_request_options
from .overdraft_settings import (
    OverdraftSettingsResource,
    AsyncOverdraftSettingsResource,
    OverdraftSettingsResourceWithRawResponse,
    AsyncOverdraftSettingsResourceWithRawResponse,
    OverdraftSettingsResourceWithStreamingResponse,
    AsyncOverdraftSettingsResourceWithStreamingResponse,
)
from ...types.account_link_new_institution_response import AccountLinkNewInstitutionResponse
from ...types.account_list_linked_accounts_response import AccountListLinkedAccountsResponse
from ...types.account_retrieve_account_details_response import AccountRetrieveAccountDetailsResponse

__all__ = ["AccountsResource", "AsyncAccountsResource"]


class AccountsResource(SyncAPIResource):
    @cached_property
    def transactions(self) -> TransactionsResource:
        return TransactionsResource(self._client)

    @cached_property
    def overdraft_settings(self) -> OverdraftSettingsResource:
        return OverdraftSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AccountsResourceWithStreamingResponse(self)

    def link_new_institution(
        self,
        *,
        country_code: str,
        institution_name: str,
        provider: Optional[Literal["plaid", "mx", "finicity", "other"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountLinkNewInstitutionResponse:
        """
        Begins the secure process of linking a new external financial institution (e.g.,
        another bank, investment platform) to the user's profile, typically involving a
        third-party tokenized flow.

        Args:
          country_code: ISO 3166-1 alpha-2 country code of the institution.

          institution_name: The name of the external financial institution to link.

          provider: Optional: Specific financial data aggregator to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/accounts/link",
            body=maybe_transform(
                {
                    "country_code": country_code,
                    "institution_name": institution_name,
                    "provider": provider,
                },
                account_link_new_institution_params.AccountLinkNewInstitutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountLinkNewInstitutionResponse,
        )

    def list_linked_accounts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListLinkedAccountsResponse:
        """
        Fetches a comprehensive, real-time list of all external financial accounts
        linked to the user's profile, including consolidated balances and institutional
        details.
        """
        return self._get(
            "/accounts/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListLinkedAccountsResponse,
        )

    def retrieve_account_details(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRetrieveAccountDetailsResponse:
        """
        Retrieves comprehensive analytics for a specific financial account, including
        historical balance trends, projected cash flow, and AI-driven insights into
        spending patterns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return self._get(
            f"/accounts/{account_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveAccountDetailsResponse,
        )

    def retrieve_account_statements(
        self,
        account_id: str,
        *,
        month: int,
        year: int,
        format: Literal["pdf", "csv"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> BinaryAPIResponse:
        """
        Fetches digital statements for a specific account, allowing filtering by date
        range and format.

        Args:
          month: Month for the statement (1-12).

          year: Year for the statement.

          format: Desired format for the statement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return self._get(
            f"/accounts/{account_id}/statements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "month": month,
                        "year": year,
                        "format": format,
                    },
                    account_retrieve_account_statements_params.AccountRetrieveAccountStatementsParams,
                ),
            ),
            cast_to=BinaryAPIResponse,
        )


class AsyncAccountsResource(AsyncAPIResource):
    @cached_property
    def transactions(self) -> AsyncTransactionsResource:
        return AsyncTransactionsResource(self._client)

    @cached_property
    def overdraft_settings(self) -> AsyncOverdraftSettingsResource:
        return AsyncOverdraftSettingsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncAccountsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAccountsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAccountsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncAccountsResourceWithStreamingResponse(self)

    async def link_new_institution(
        self,
        *,
        country_code: str,
        institution_name: str,
        provider: Optional[Literal["plaid", "mx", "finicity", "other"]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountLinkNewInstitutionResponse:
        """
        Begins the secure process of linking a new external financial institution (e.g.,
        another bank, investment platform) to the user's profile, typically involving a
        third-party tokenized flow.

        Args:
          country_code: ISO 3166-1 alpha-2 country code of the institution.

          institution_name: The name of the external financial institution to link.

          provider: Optional: Specific financial data aggregator to use.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/accounts/link",
            body=await async_maybe_transform(
                {
                    "country_code": country_code,
                    "institution_name": institution_name,
                    "provider": provider,
                },
                account_link_new_institution_params.AccountLinkNewInstitutionParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountLinkNewInstitutionResponse,
        )

    async def list_linked_accounts(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountListLinkedAccountsResponse:
        """
        Fetches a comprehensive, real-time list of all external financial accounts
        linked to the user's profile, including consolidated balances and institutional
        details.
        """
        return await self._get(
            "/accounts/me",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountListLinkedAccountsResponse,
        )

    async def retrieve_account_details(
        self,
        account_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AccountRetrieveAccountDetailsResponse:
        """
        Retrieves comprehensive analytics for a specific financial account, including
        historical balance trends, projected cash flow, and AI-driven insights into
        spending patterns.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        return await self._get(
            f"/accounts/{account_id}/details",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AccountRetrieveAccountDetailsResponse,
        )

    async def retrieve_account_statements(
        self,
        account_id: str,
        *,
        month: int,
        year: int,
        format: Literal["pdf", "csv"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AsyncBinaryAPIResponse:
        """
        Fetches digital statements for a specific account, allowing filtering by date
        range and format.

        Args:
          month: Month for the statement (1-12).

          year: Year for the statement.

          format: Desired format for the statement.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not account_id:
            raise ValueError(f"Expected a non-empty value for `account_id` but received {account_id!r}")
        extra_headers = {"Accept": "application/pdf", **(extra_headers or {})}
        return await self._get(
            f"/accounts/{account_id}/statements",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "month": month,
                        "year": year,
                        "format": format,
                    },
                    account_retrieve_account_statements_params.AccountRetrieveAccountStatementsParams,
                ),
            ),
            cast_to=AsyncBinaryAPIResponse,
        )


class AccountsResourceWithRawResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.link_new_institution = to_raw_response_wrapper(
            accounts.link_new_institution,
        )
        self.list_linked_accounts = to_raw_response_wrapper(
            accounts.list_linked_accounts,
        )
        self.retrieve_account_details = to_raw_response_wrapper(
            accounts.retrieve_account_details,
        )
        self.retrieve_account_statements = to_custom_raw_response_wrapper(
            accounts.retrieve_account_statements,
            BinaryAPIResponse,
        )

    @cached_property
    def transactions(self) -> TransactionsResourceWithRawResponse:
        return TransactionsResourceWithRawResponse(self._accounts.transactions)

    @cached_property
    def overdraft_settings(self) -> OverdraftSettingsResourceWithRawResponse:
        return OverdraftSettingsResourceWithRawResponse(self._accounts.overdraft_settings)


class AsyncAccountsResourceWithRawResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.link_new_institution = async_to_raw_response_wrapper(
            accounts.link_new_institution,
        )
        self.list_linked_accounts = async_to_raw_response_wrapper(
            accounts.list_linked_accounts,
        )
        self.retrieve_account_details = async_to_raw_response_wrapper(
            accounts.retrieve_account_details,
        )
        self.retrieve_account_statements = async_to_custom_raw_response_wrapper(
            accounts.retrieve_account_statements,
            AsyncBinaryAPIResponse,
        )

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithRawResponse:
        return AsyncTransactionsResourceWithRawResponse(self._accounts.transactions)

    @cached_property
    def overdraft_settings(self) -> AsyncOverdraftSettingsResourceWithRawResponse:
        return AsyncOverdraftSettingsResourceWithRawResponse(self._accounts.overdraft_settings)


class AccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AccountsResource) -> None:
        self._accounts = accounts

        self.link_new_institution = to_streamed_response_wrapper(
            accounts.link_new_institution,
        )
        self.list_linked_accounts = to_streamed_response_wrapper(
            accounts.list_linked_accounts,
        )
        self.retrieve_account_details = to_streamed_response_wrapper(
            accounts.retrieve_account_details,
        )
        self.retrieve_account_statements = to_custom_streamed_response_wrapper(
            accounts.retrieve_account_statements,
            StreamedBinaryAPIResponse,
        )

    @cached_property
    def transactions(self) -> TransactionsResourceWithStreamingResponse:
        return TransactionsResourceWithStreamingResponse(self._accounts.transactions)

    @cached_property
    def overdraft_settings(self) -> OverdraftSettingsResourceWithStreamingResponse:
        return OverdraftSettingsResourceWithStreamingResponse(self._accounts.overdraft_settings)


class AsyncAccountsResourceWithStreamingResponse:
    def __init__(self, accounts: AsyncAccountsResource) -> None:
        self._accounts = accounts

        self.link_new_institution = async_to_streamed_response_wrapper(
            accounts.link_new_institution,
        )
        self.list_linked_accounts = async_to_streamed_response_wrapper(
            accounts.list_linked_accounts,
        )
        self.retrieve_account_details = async_to_streamed_response_wrapper(
            accounts.retrieve_account_details,
        )
        self.retrieve_account_statements = async_to_custom_streamed_response_wrapper(
            accounts.retrieve_account_statements,
            AsyncStreamedBinaryAPIResponse,
        )

    @cached_property
    def transactions(self) -> AsyncTransactionsResourceWithStreamingResponse:
        return AsyncTransactionsResourceWithStreamingResponse(self._accounts.transactions)

    @cached_property
    def overdraft_settings(self) -> AsyncOverdraftSettingsResourceWithStreamingResponse:
        return AsyncOverdraftSettingsResourceWithStreamingResponse(self._accounts.overdraft_settings)
