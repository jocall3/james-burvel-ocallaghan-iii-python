# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii._utils import parse_date
from james_burvel_ocallaghan_iii.types.transactions import (
    RecurringTransaction,
    RecurringListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestRecurring:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: JamesBurvelOcallaghanIii) -> None:
        recurring = client.transactions.recurring.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
        )
        assert_matches_type(RecurringTransaction, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        recurring = client.transactions.recurring.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
            linked_account_id="acc_chase_checking_4567",
        )
        assert_matches_type(RecurringTransaction, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.recurring.with_raw_response.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurring = response.parse()
        assert_matches_type(RecurringTransaction, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.recurring.with_streaming_response.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurring = response.parse()
            assert_matches_type(RecurringTransaction, recurring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        recurring = client.transactions.recurring.list()
        assert_matches_type(RecurringListResponse, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.transactions.recurring.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurring = response.parse()
        assert_matches_type(RecurringListResponse, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.transactions.recurring.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurring = response.parse()
            assert_matches_type(RecurringListResponse, recurring, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncRecurring:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        recurring = await async_client.transactions.recurring.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
        )
        assert_matches_type(RecurringTransaction, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        recurring = await async_client.transactions.recurring.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
            linked_account_id="acc_chase_checking_4567",
        )
        assert_matches_type(RecurringTransaction, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.recurring.with_raw_response.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurring = await response.parse()
        assert_matches_type(RecurringTransaction, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.recurring.with_streaming_response.create(
            amount=55.5,
            category="Health & Fitness",
            currency="USD",
            description="New Gym Membership",
            frequency="monthly",
            start_date=parse_date("2024-09-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurring = await response.parse()
            assert_matches_type(RecurringTransaction, recurring, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        recurring = await async_client.transactions.recurring.list()
        assert_matches_type(RecurringListResponse, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.transactions.recurring.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        recurring = await response.parse()
        assert_matches_type(RecurringListResponse, recurring, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.transactions.recurring.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            recurring = await response.parse()
            assert_matches_type(RecurringListResponse, recurring, path=["response"])

        assert cast(Any, response.is_closed) is True
