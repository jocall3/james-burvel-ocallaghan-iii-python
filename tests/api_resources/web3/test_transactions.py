# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.web3 import (
    TransactionInitiateTransferResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestTransactions:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_transfer(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.web3.transactions.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
        )
        assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_transfer_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        transaction = client.web3.transactions.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
            gas_limit=21000,
            gas_price_gwei=50,
            memo="Payment for services",
        )
        assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate_transfer(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.web3.transactions.with_raw_response.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = response.parse()
        assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate_transfer(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.web3.transactions.with_streaming_response.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = response.parse()
            assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncTransactions:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_transfer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.web3.transactions.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
        )
        assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_transfer_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        transaction = await async_client.web3.transactions.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
            gas_limit=21000,
            gas_price_gwei=50,
            memo="Payment for services",
        )
        assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate_transfer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.web3.transactions.with_raw_response.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        transaction = await response.parse()
        assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate_transfer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.web3.transactions.with_streaming_response.initiate_transfer(
            amount=0.1,
            asset_symbol="ETH",
            blockchain_network="Ethereum",
            recipient_address="0xdef4567890abcdef1234567890abcdef1234567890",
            source_wallet_id="wallet_conn_eth_0xabc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            transaction = await response.parse()
            assert_matches_type(TransactionInitiateTransferResponse, transaction, path=["response"])

        assert cast(Any, response.is_closed) is True
