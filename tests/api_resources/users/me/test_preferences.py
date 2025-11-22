# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.users.me import UserPreferences

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPreferences:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        preference = client.users.me.preferences.retrieve()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.preferences.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.preferences.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(UserPreferences, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: JamesBurvelOcallaghanIii) -> None:
        preference = client.users.me.preferences.update()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        preference = client.users.me.preferences.update(
            ai_interaction_mode="proactive",
            data_sharing_consent=True,
            notification_channels={
                "email": True,
                "in_app": True,
                "push": True,
                "sms": False,
            },
            preferred_language="en-US",
            theme="Dark-Quantum",
            transaction_grouping="category",
        )
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.preferences.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = response.parse()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.preferences.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = response.parse()
            assert_matches_type(UserPreferences, preference, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPreferences:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        preference = await async_client.users.me.preferences.retrieve()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.preferences.with_raw_response.retrieve()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.preferences.with_streaming_response.retrieve() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(UserPreferences, preference, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        preference = await async_client.users.me.preferences.update()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        preference = await async_client.users.me.preferences.update(
            ai_interaction_mode="proactive",
            data_sharing_consent=True,
            notification_channels={
                "email": True,
                "in_app": True,
                "push": True,
                "sms": False,
            },
            preferred_language="en-US",
            theme="Dark-Quantum",
            transaction_grouping="category",
        )
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.preferences.with_raw_response.update()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        preference = await response.parse()
        assert_matches_type(UserPreferences, preference, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.preferences.with_streaming_response.update() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            preference = await response.parse()
            assert_matches_type(UserPreferences, preference, path=["response"])

        assert cast(Any, response.is_closed) is True
