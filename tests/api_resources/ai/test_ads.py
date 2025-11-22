# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.ai import VideoOperationStatus, AdListGeneratedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestAds:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_generated(self, client: JamesBurvelOcallaghanIii) -> None:
        ad = client.ai.ads.list_generated()
        assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_generated_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        ad = client.ai.ads.list_generated(
            limit=10,
            offset=0,
            status="done",
        )
        assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_generated(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.ads.with_raw_response.list_generated()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_generated(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.ads.with_streaming_response.list_generated() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        ad = client.ai.ads.retrieve_status(
            "op-video-gen-12345-abcde",
        )
        assert_matches_type(VideoOperationStatus, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.ads.with_raw_response.retrieve_status(
            "op-video-gen-12345-abcde",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = response.parse()
        assert_matches_type(VideoOperationStatus, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.ads.with_streaming_response.retrieve_status(
            "op-video-gen-12345-abcde",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = response.parse()
            assert_matches_type(VideoOperationStatus, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            client.ai.ads.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncAds:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_generated(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        ad = await async_client.ai.ads.list_generated()
        assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_generated_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        ad = await async_client.ai.ads.list_generated(
            limit=10,
            offset=0,
            status="done",
        )
        assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_generated(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.ads.with_raw_response.list_generated()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_generated(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.ads.with_streaming_response.list_generated() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(AdListGeneratedResponse, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        ad = await async_client.ai.ads.retrieve_status(
            "op-video-gen-12345-abcde",
        )
        assert_matches_type(VideoOperationStatus, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.ads.with_raw_response.retrieve_status(
            "op-video-gen-12345-abcde",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        ad = await response.parse()
        assert_matches_type(VideoOperationStatus, ad, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.ads.with_streaming_response.retrieve_status(
            "op-video-gen-12345-abcde",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            ad = await response.parse()
            assert_matches_type(VideoOperationStatus, ad, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `operation_id` but received ''"):
            await async_client.ai.ads.with_raw_response.retrieve_status(
                "",
            )
