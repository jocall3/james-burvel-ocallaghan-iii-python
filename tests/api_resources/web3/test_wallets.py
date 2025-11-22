# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.web3 import (
    WalletListResponse,
    CryptoWalletConnection,
    WalletRetrieveBalancesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWallets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        wallet = client.web3.wallets.list()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        wallet = client.web3.wallets.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.web3.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.web3.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletListResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect(self, client: JamesBurvelOcallaghanIii) -> None:
        wallet = client.web3.wallets.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
        )
        assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_connect_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        wallet = client.web3.wallets.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
            request_write_access=True,
        )
        assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_connect(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.web3.wallets.with_raw_response.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_connect(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.web3.wallets.with_streaming_response.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_balances(self, client: JamesBurvelOcallaghanIii) -> None:
        wallet = client.web3.wallets.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
        )
        assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_balances_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        wallet = client.web3.wallets.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
            limit=1,
            offset=0,
        )
        assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_balances(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.web3.wallets.with_raw_response.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = response.parse()
        assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_balances(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.web3.wallets.with_streaming_response.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = response.parse()
            assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_balances(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            client.web3.wallets.with_raw_response.retrieve_balances(
                wallet_id="",
            )


class TestAsyncWallets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        wallet = await async_client.web3.wallets.list()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        wallet = await async_client.web3.wallets.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.web3.wallets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletListResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.web3.wallets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletListResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        wallet = await async_client.web3.wallets.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
        )
        assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_connect_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        wallet = await async_client.web3.wallets.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
            request_write_access=True,
        )
        assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_connect(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.web3.wallets.with_raw_response.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_connect(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.web3.wallets.with_streaming_response.connect(
            blockchain_network="Ethereum",
            signed_message="0xabcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890abcdef1234567890",
            wallet_address="0x123abc456def7890...",
            wallet_provider="MetaMask",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(CryptoWalletConnection, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_balances(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        wallet = await async_client.web3.wallets.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
        )
        assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_balances_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        wallet = await async_client.web3.wallets.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
            limit=1,
            offset=0,
        )
        assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_balances(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.web3.wallets.with_raw_response.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        wallet = await response.parse()
        assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_balances(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.web3.wallets.with_streaming_response.retrieve_balances(
            wallet_id="wallet_conn_eth_0xabc123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            wallet = await response.parse()
            assert_matches_type(WalletRetrieveBalancesResponse, wallet, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_balances(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `wallet_id` but received ''"):
            await async_client.web3.wallets.with_raw_response.retrieve_balances(
                wallet_id="",
            )
