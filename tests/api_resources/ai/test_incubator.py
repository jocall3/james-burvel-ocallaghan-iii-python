# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.ai import IncubatorListPitchesResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestIncubator:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pitches(self, client: JamesBurvelOcallaghanIii) -> None:
        incubator = client.ai.incubator.list_pitches()
        assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_pitches_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        incubator = client.ai.incubator.list_pitches(
            limit=2,
            offset=0,
            status="feedback_required",
        )
        assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_pitches(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.incubator.with_raw_response.list_pitches()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = response.parse()
        assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_pitches(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.incubator.with_streaming_response.list_pitches() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = response.parse()
            assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncIncubator:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pitches(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        incubator = await async_client.ai.incubator.list_pitches()
        assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_pitches_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        incubator = await async_client.ai.incubator.list_pitches(
            limit=2,
            offset=0,
            status="feedback_required",
        )
        assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_pitches(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.incubator.with_raw_response.list_pitches()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        incubator = await response.parse()
        assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_pitches(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.incubator.with_streaming_response.list_pitches() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            incubator = await response.parse()
            assert_matches_type(IncubatorListPitchesResponse, incubator, path=["response"])

        assert cast(Any, response.is_closed) is True
