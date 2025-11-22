# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.ai.ads import (
    GenerateAdvancedResponse,
    GenerateStandardResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGenerate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_advanced(self, client: JamesBurvelOcallaghanIii) -> None:
        generate = client.ai.ads.generate.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )
        assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_advanced_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        generate = client.ai.ads.generate.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
            audience_target="corporate",
            background_music="upbeat_corporate",
            brand_assets=["https://demobank.com/assets/corporate_logo.png"],
            brand_colors=["#0000FF", "#FFD700"],
            call_to_action={
                "display_time_seconds": 5,
                "text": "Learn more at DemoBank.com/business",
                "url": "https://demobank.com/business",
            },
            keywords=["financial freedom", "AI banking", "startup success"],
            subtitles_enabled=True,
            voiceover_style="male_professional",
            voiceover_text=": Your business, powered by intelligent finance.",
        )
        assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_advanced(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.ads.generate.with_raw_response.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_advanced(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.ads.generate.with_streaming_response.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_standard(self, client: JamesBurvelOcallaghanIii) -> None:
        generate = client.ai.ads.generate.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )
        assert_matches_type(GenerateStandardResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_standard_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        generate = client.ai.ads.generate.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
            brand_colors=["#0000FF", "#FFD700"],
            keywords=["financial freedom", "AI banking", "startup success"],
        )
        assert_matches_type(GenerateStandardResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_standard(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.ads.generate.with_raw_response.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = response.parse()
        assert_matches_type(GenerateStandardResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_standard(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.ads.generate.with_streaming_response.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = response.parse()
            assert_matches_type(GenerateStandardResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncGenerate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_advanced(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        generate = await async_client.ai.ads.generate.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )
        assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_advanced_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        generate = await async_client.ai.ads.generate.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
            audience_target="corporate",
            background_music="upbeat_corporate",
            brand_assets=["https://demobank.com/assets/corporate_logo.png"],
            brand_colors=["#0000FF", "#FFD700"],
            call_to_action={
                "display_time_seconds": 5,
                "text": "Learn more at DemoBank.com/business",
                "url": "https://demobank.com/business",
            },
            keywords=["financial freedom", "AI banking", "startup success"],
            subtitles_enabled=True,
            voiceover_style="male_professional",
            voiceover_text=": Your business, powered by intelligent finance.",
        )
        assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_advanced(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.ads.generate.with_raw_response.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_advanced(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.ads.generate.with_streaming_response.advanced(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateAdvancedResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_standard(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        generate = await async_client.ai.ads.generate.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )
        assert_matches_type(GenerateStandardResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_standard_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        generate = await async_client.ai.ads.generate.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
            brand_colors=["#0000FF", "#FFD700"],
            keywords=["financial freedom", "AI banking", "startup success"],
        )
        assert_matches_type(GenerateStandardResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_standard(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.ads.generate.with_raw_response.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        generate = await response.parse()
        assert_matches_type(GenerateStandardResponse, generate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_standard(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.ads.generate.with_streaming_response.standard(
            aspect_ratio="16:9",
            length_seconds=15,
            prompt="A captivating ad featuring a young entrepreneur using 's AI tools to grow their startup. Focus on innovation and ease of use.",
            style="Cinematic",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            generate = await response.parse()
            assert_matches_type(GenerateStandardResponse, generate, path=["response"])

        assert cast(Any, response.is_closed) is True
