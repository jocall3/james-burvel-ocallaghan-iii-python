# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import Web3RetrieveNFTsResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestWeb3:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_nfts(self, client: JamesBurvelOcallaghanIii) -> None:
        web3 = client.web3.retrieve_nfts()
        assert_matches_type(Web3RetrieveNFTsResponse, web3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_nfts(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.web3.with_raw_response.retrieve_nfts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web3 = response.parse()
        assert_matches_type(Web3RetrieveNFTsResponse, web3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_nfts(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.web3.with_streaming_response.retrieve_nfts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web3 = response.parse()
            assert_matches_type(Web3RetrieveNFTsResponse, web3, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncWeb3:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_nfts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        web3 = await async_client.web3.retrieve_nfts()
        assert_matches_type(Web3RetrieveNFTsResponse, web3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_nfts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.web3.with_raw_response.retrieve_nfts()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        web3 = await response.parse()
        assert_matches_type(Web3RetrieveNFTsResponse, web3, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_nfts(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.web3.with_streaming_response.retrieve_nfts() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            web3 = await response.parse()
            assert_matches_type(Web3RetrieveNFTsResponse, web3, path=["response"])

        assert cast(Any, response.is_closed) is True
