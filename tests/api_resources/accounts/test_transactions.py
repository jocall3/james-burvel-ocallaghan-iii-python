# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.accounts import (
    TransactionListPendingTransactionsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_pending_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.accounts.transactions.list_pending_transactions(
            account_id="acc_chase_checking_4567",
        )
        assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

    @parametrize
    def test_method_list_pending_transactions_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.accounts.transactions.list_pending_transactions(
            account_id="acc_chase_checking_4567",
            limit={},
            offset={},
        )
        assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_list_pending_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.transactions.with_raw_response.list_pending_transactions(
            account_id="acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_list_pending_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.transactions.with_streaming_response.list_pending_transactions(
            account_id="acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_pending_transactions(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.accounts.transactions.list_pending_transactions(
            account_id="acc_chase_checking_4567",
        )
        assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

    @parametrize
    async def test_method_list_pending_transactions_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        transaction = await async_client.accounts.transactions.list_pending_transactions(
            account_id="acc_chase_checking_4567",
            limit={},
            offset={},
        )
        assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_list_pending_transactions(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.transactions.with_raw_response.list_pending_transactions(
            account_id="acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list_pending_transactions(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        async with async_client.accounts.transactions.with_streaming_response.list_pending_transactions(
            account_id="acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionListPendingTransactionsResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
