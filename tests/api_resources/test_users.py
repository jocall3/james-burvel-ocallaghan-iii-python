# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import User, UserLoginResponse
from james_burvel_ocallaghan_iii._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestUsers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_login(self, client: JamesBurvelOcallaghanIii) -> None:
        user = client.users.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
        )
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    def test_method_login_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        user = client.users.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
            mfa_code="123456",
        )
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    def test_raw_response_login(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.with_raw_response.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    def test_streaming_response_login(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.with_streaming_response.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(UserLoginResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: JamesBurvelOcallaghanIii) -> None:
        user = client.users.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        user = client.users.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
            address={
                "city": "Anytown",
                "country": "USA",
                "state": "CA",
                "street": "123 Main St",
                "zip": "90210",
            },
            date_of_birth=parse_date("1990-05-10"),
            phone="+1-555-987-6543",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.with_raw_response.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.with_streaming_response.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncUsers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_login(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        user = await async_client.users.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
        )
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    async def test_method_login_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        user = await async_client.users.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
            mfa_code="123456",
        )
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    async def test_raw_response_login(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.with_raw_response.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(UserLoginResponse, user, path=["response"])

    @parametrize
    async def test_streaming_response_login(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.with_streaming_response.login(
            email="quantum.visionary@demobank.com",
            password="YourSecurePassword123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(UserLoginResponse, user, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        user = await async_client.users.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        user = await async_client.users.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
            address={
                "city": "Anytown",
                "country": "USA",
                "state": "CA",
                "street": "123 Main St",
                "zip": "90210",
            },
            date_of_birth=parse_date("1990-05-10"),
            phone="+1-555-987-6543",
        )
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.with_raw_response.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        user = await response.parse()
        assert_matches_type(User, user, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.with_streaming_response.register(
            email="alice.w@example.com",
            name="Alice Wonderland",
            password="SecureP@ssw0rd2024!",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            user = await response.parse()
            assert_matches_type(User, user, path=["response"])

        assert cast(Any, response.is_closed) is True
