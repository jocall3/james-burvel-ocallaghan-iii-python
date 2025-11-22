# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.investments import AssetSearchResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAssets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search(self, client: JamesBurvelOcallaghanIii) -> None:
        asset = client.investments.assets.search(
            query="Tesla",
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_search_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        asset = client.investments.assets.search(
            query="Tesla",
            min_esg_score=7,
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_search(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.investments.assets.with_raw_response.search(
            query="Tesla",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = response.parse()
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_search(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.investments.assets.with_streaming_response.search(
            query="Tesla",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = response.parse()
            assert_matches_type(AssetSearchResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncAssets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        asset = await async_client.investments.assets.search(
            query="Tesla",
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_search_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        asset = await async_client.investments.assets.search(
            query="Tesla",
            min_esg_score=7,
        )
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_search(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.investments.assets.with_raw_response.search(
            query="Tesla",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        asset = await response.parse()
        assert_matches_type(AssetSearchResponse, asset, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_search(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.investments.assets.with_streaming_response.search(
            query="Tesla",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            asset = await response.parse()
            assert_matches_type(AssetSearchResponse, asset, path=["response"])

        assert cast(Any, response.is_closed) is True
