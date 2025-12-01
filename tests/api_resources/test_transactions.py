# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import (
    Transaction,
    PaginatedTransactions,
    TransactionDisputeResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.retrieve(
            "txn_quantum-2024-07-21-A7B8C9",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.with_raw_response.retrieve(
            "txn_quantum-2024-07-21-A7B8C9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.with_streaming_response.retrieve(
            "txn_quantum-2024-07-21-A7B8C9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.list()
        assert_matches_type(PaginatedTransactions, transaction, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.list(
            category="Groceries",
            end_date="2024-12-31",
            limit={},
            max_amount=100,
            min_amount=20,
            offset={},
            search_query="Starbucks",
            start_date="2024-01-01",
            type="expense",
        )
        assert_matches_type(PaginatedTransactions, transaction, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(PaginatedTransactions, transaction, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(PaginatedTransactions, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_categorize(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_method_categorize_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
            apply_to_future=True,
            notes="Bulk purchase for party",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_categorize(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.with_raw_response.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_streaming_response_categorize(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.with_streaming_response.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_dispute(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
        )
        assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

    @parametrize
    def test_method_dispute_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
            supporting_documents=["https://demobank.com/uploads/flight_ticket.png"],
        )
        assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

    @parametrize
    def test_raw_response_dispute(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.with_raw_response.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

    @parametrize
    def test_streaming_response_dispute(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.with_streaming_response.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update_notes(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.transactions.update_notes(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            notes="This was a special coffee for a client meeting.",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_raw_response_update_notes(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.with_raw_response.update_notes(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            notes="This was a special coffee for a client meeting.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    def test_streaming_response_update_notes(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.with_streaming_response.update_notes(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            notes="This was a special coffee for a client meeting.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.retrieve(
            "txn_quantum-2024-07-21-A7B8C9",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.with_raw_response.retrieve(
            "txn_quantum-2024-07-21-A7B8C9",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.with_streaming_response.retrieve(
            "txn_quantum-2024-07-21-A7B8C9",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.list()
        assert_matches_type(PaginatedTransactions, transaction, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.list(
            category="Groceries",
            end_date="2024-12-31",
            limit={},
            max_amount=100,
            min_amount=20,
            offset={},
            search_query="Starbucks",
            start_date="2024-01-01",
            type="expense",
        )
        assert_matches_type(PaginatedTransactions, transaction, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(PaginatedTransactions, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(PaginatedTransactions, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_categorize(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_method_categorize_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
            apply_to_future=True,
            notes="Bulk purchase for party",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_categorize(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.with_raw_response.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_categorize(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.with_streaming_response.categorize(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            category="Home > Groceries",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_dispute(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
        )
        assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

    @parametrize
    async def test_method_dispute_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
            supporting_documents=["https://demobank.com/uploads/flight_ticket.png"],
        )
        assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

    @parametrize
    async def test_raw_response_dispute(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.with_raw_response.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_dispute(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.with_streaming_response.dispute(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            details="I did not authorize this purchase. My card may have been compromised and I was traveling internationally on this date.",
            reason="unauthorized",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionDisputeResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update_notes(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.transactions.update_notes(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            notes="This was a special coffee for a client meeting.",
        )
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_raw_response_update_notes(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.with_raw_response.update_notes(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            notes="This was a special coffee for a client meeting.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(Transaction, transaction, path=["response"])

    @parametrize
    async def test_streaming_response_update_notes(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.with_streaming_response.update_notes(
            transaction_id="txn_quantum-2024-07-21-A7B8C9",
            notes="This was a special coffee for a client meeting.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(Transaction, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
