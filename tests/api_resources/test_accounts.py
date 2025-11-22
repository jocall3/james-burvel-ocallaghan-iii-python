# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import httpx
import pytest
from respx import MockRouter

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import (
    AccountLinkNewInstitutionResponse,
    AccountListLinkedAccountsResponse,
    AccountRetrieveAccountDetailsResponse,
)
from james_burvel_ocallaghan_iii._response import (
    BinaryAPIResponse,
    AsyncBinaryAPIResponse,
    StreamedBinaryAPIResponse,
    AsyncStreamedBinaryAPIResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAccounts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_link_new_institution(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_link_new_institution_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
            provider="plaid",
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_linked_accounts(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.list_linked_accounts()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_linked_accounts(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.with_raw_response.list_linked_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_linked_accounts(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.with_streaming_response.list_linked_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = response.parse()
            assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_account_details(self, client: JamesBurvelOcallaghanIii) -> None:
        account = client.accounts.retrieve_account_details(
            "acc_chase_checking_4567",
        )
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_account_details(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.with_raw_response.retrieve_account_details(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = response.parse()
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_account_details(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve_account_details(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_account_statements(self, client: JamesBurvelOcallaghanIii, respx_mock: MockRouter) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        account = client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )
        assert account.is_closed
        assert account.json() == {"foo": "bar"}
        assert cast(Any, account.is_closed) is True
        assert isinstance(account, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_method_retrieve_account_statements_with_all_params(
        self, client: JamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        account = client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
            format="pdf",
        )
        assert account.is_closed
        assert account.json() == {"foo": "bar"}
        assert cast(Any, account.is_closed) is True
        assert isinstance(account, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_raw_response_retrieve_account_statements(
        self, client: JamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        account = client.accounts.with_raw_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )

        assert account.is_closed is True
        assert account.http_request.headers.get("X-Stainless-Lang") == "python"
        assert account.json() == {"foo": "bar"}
        assert isinstance(account, BinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_streaming_response_retrieve_account_statements(
        self, client: JamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        with client.accounts.with_streaming_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        ) as account:
            assert not account.is_closed
            assert account.http_request.headers.get("X-Stainless-Lang") == "python"

            assert account.json() == {"foo": "bar"}
            assert cast(Any, account.is_closed) is True
            assert isinstance(account, StreamedBinaryAPIResponse)

        assert cast(Any, account.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    def test_path_params_retrieve_account_statements(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.with_raw_response.retrieve_account_statements(
                account_id="",
                month=7,
                year=2024,
            )


class TestAsyncAccounts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_link_new_institution(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_link_new_institution_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        account = await async_client.accounts.link_new_institution(
            country_code="US",
            institution_name="Bank of America",
            provider="plaid",
        )
        assert_matches_type(AccountLinkNewInstitutionResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_linked_accounts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.list_linked_accounts()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_linked_accounts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.with_raw_response.list_linked_accounts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_linked_accounts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.accounts.with_streaming_response.list_linked_accounts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            account = await response.parse()
            assert_matches_type(AccountListLinkedAccountsResponse, account, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_account_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        account = await async_client.accounts.retrieve_account_details(
            "acc_chase_checking_4567",
        )
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_account_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.with_raw_response.retrieve_account_details(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        account = await response.parse()
        assert_matches_type(AccountRetrieveAccountDetailsResponse, account, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
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

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_account_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve_account_details(
                "",
            )

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_account_statements(
        self, async_client: AsyncJamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        account = await async_client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )
        assert account.is_closed
        assert await account.json() == {"foo": "bar"}
        assert cast(Any, account.is_closed) is True
        assert isinstance(account, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_method_retrieve_account_statements_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        account = await async_client.accounts.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
            format="pdf",
        )
        assert account.is_closed
        assert await account.json() == {"foo": "bar"}
        assert cast(Any, account.is_closed) is True
        assert isinstance(account, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_raw_response_retrieve_account_statements(
        self, async_client: AsyncJamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )

        account = await async_client.accounts.with_raw_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        )

        assert account.is_closed is True
        assert account.http_request.headers.get("X-Stainless-Lang") == "python"
        assert await account.json() == {"foo": "bar"}
        assert isinstance(account, AsyncBinaryAPIResponse)

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_streaming_response_retrieve_account_statements(
        self, async_client: AsyncJamesBurvelOcallaghanIii, respx_mock: MockRouter
    ) -> None:
        respx_mock.get("/accounts/acc_chase_checking_4567/statements").mock(
            return_value=httpx.Response(200, json={"foo": "bar"})
        )
        async with async_client.accounts.with_streaming_response.retrieve_account_statements(
            account_id="acc_chase_checking_4567",
            month=7,
            year=2024,
        ) as account:
            assert not account.is_closed
            assert account.http_request.headers.get("X-Stainless-Lang") == "python"

            assert await account.json() == {"foo": "bar"}
            assert cast(Any, account.is_closed) is True
            assert isinstance(account, AsyncStreamedBinaryAPIResponse)

        assert cast(Any, account.is_closed) is True

    @parametrize
    @pytest.mark.respx(base_url=base_url)
    async def test_path_params_retrieve_account_statements(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.with_raw_response.retrieve_account_statements(
                account_id="",
                month=7,
                year=2024,
            )
