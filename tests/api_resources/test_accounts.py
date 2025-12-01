# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import (
    AccountLinkNewInstitutionResponse,
    AccountListLinkedAccountsResponse,
    AccountRetrieveAccountDetailsResponse,
    AccountRetrieveAccountStatementsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_link_new_institution(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @parametrize
    def test_method_link_new_institution_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
            provider_identifier={},
            redirect_uri={},
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @parametrize
    def test_raw_response_link_new_institution(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.with_raw_response.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_link_new_institution(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.with_streaming_response.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list_linked_accounts(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.list_linked_accounts()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @parametrize
    def test_method_list_linked_accounts_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.list_linked_accounts(
            limit={},
            offset={},
        )
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @parametrize
    def test_raw_response_list_linked_accounts(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.with_raw_response.list_linked_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_list_linked_accounts(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.with_streaming_response.list_linked_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_account_details(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.retrieve_account_details(
            "acc_chase_checking_4567",
        )
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve_account_details(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.with_raw_response.retrieve_account_details(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_account_details(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.with_streaming_response.retrieve_account_details(
            "acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_account_statements(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )
        assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

    @parametrize
    def test_method_retrieve_account_statements_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
            format="pdf",
        )
        assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

    @parametrize
    def test_raw_response_retrieve_account_statements(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.with_raw_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_account_statements(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.with_streaming_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_link_new_institution(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @parametrize
    async def test_method_link_new_institution_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        account = await async_client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
            provider_identifier={},
            redirect_uri={},
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_link_new_institution(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.with_raw_response.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_link_new_institution(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.accounts.with_streaming_response.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list_linked_accounts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.list_linked_accounts()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @parametrize
    async def test_method_list_linked_accounts_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        account = await async_client.accounts.list_linked_accounts(
            limit={},
            offset={},
        )
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_list_linked_accounts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.with_raw_response.list_linked_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_list_linked_accounts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.accounts.with_streaming_response.list_linked_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_account_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.retrieve_account_details(
            "acc_chase_checking_4567",
        )
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_account_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_account_details(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_account_details(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_account_details(
            "acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_account_statements(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )
        assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

    @parametrize
    async def test_method_retrieve_account_statements_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        account = await async_client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
            format="pdf",
        )
        assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_account_statements(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_account_statements(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        async with async_client.accounts.with_streaming_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountRetrieveAccountStatementsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True
