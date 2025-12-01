# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import (
    FinancialGoal,
    GoalListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestGoals:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_create(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_method_create_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
            contributing_accounts=[{}],
            generate_ai_plan=True,
            initial_contribution=1000,
            risk_tolerance="conservative",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_raw_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.goals.with_raw_response.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_streaming_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.goals.with_streaming_response.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(FinancialGoal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.retrieve(
            "goal_retirement_2050",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_raw_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.goals.with_raw_response.retrieve(
            "goal_retirement_2050",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_streaming_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.goals.with_streaming_response.retrieve(
            "goal_retirement_2050",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(FinancialGoal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_update(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.update(
            goal_id="goal_retirement_2050",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_method_update_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.update(
            goal_id="goal_retirement_2050",
            contributing_accounts=[{}],
            generate_ai_plan=True,
            name="Revised Retirement Fund Goal",
            risk_tolerance="conservative",
            status="paused",
            target_amount=1200000,
            target_date="2029-12-31",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_raw_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.goals.with_raw_response.update(
            goal_id="goal_retirement_2050",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    def test_streaming_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.goals.with_streaming_response.update(
            goal_id="goal_retirement_2050",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(FinancialGoal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.list()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.list(
            limit={},
            offset={},
        )
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.goals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.goals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert_matches_type(GoalListResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        goal = client.goals.delete(
            "goal_retirement_2050",
        )
        assert goal is None

    @parametrize
    def test_raw_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.goals.with_raw_response.delete(
            "goal_retirement_2050",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = response.parse()
        assert goal is None

    @parametrize
    def test_streaming_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.goals.with_streaming_response.delete(
            "goal_retirement_2050",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = response.parse()
            assert goal is None

        assert cast(Any, response.is_closed) is True


class TestAsyncGoals:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
            contributing_accounts=[{}],
            generate_ai_plan=True,
            initial_contribution=1000,
            risk_tolerance="conservative",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.goals.with_raw_response.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.goals.with_streaming_response.create(
            name="Dream Vacation Fund",
            target_amount=15000,
            target_date="2026-06-30",
            type="large_purchase",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(FinancialGoal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.retrieve(
            "goal_retirement_2050",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.goals.with_raw_response.retrieve(
            "goal_retirement_2050",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.goals.with_streaming_response.retrieve(
            "goal_retirement_2050",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(FinancialGoal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.update(
            goal_id="goal_retirement_2050",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.update(
            goal_id="goal_retirement_2050",
            contributing_accounts=[{}],
            generate_ai_plan=True,
            name="Revised Retirement Fund Goal",
            risk_tolerance="conservative",
            status="paused",
            target_amount=1200000,
            target_date="2029-12-31",
        )
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.goals.with_raw_response.update(
            goal_id="goal_retirement_2050",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(FinancialGoal, goal, path=["response"])

    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.goals.with_streaming_response.update(
            goal_id="goal_retirement_2050",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(FinancialGoal, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.list()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.list(
            limit={},
            offset={},
        )
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.goals.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert_matches_type(GoalListResponse, goal, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.goals.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert_matches_type(GoalListResponse, goal, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        goal = await async_client.goals.delete(
            "goal_retirement_2050",
        )
        assert goal is None

    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.goals.with_raw_response.delete(
            "goal_retirement_2050",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        goal = await response.parse()
        assert goal is None

    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.goals.with_streaming_response.delete(
            "goal_retirement_2050",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            goal = await response.parse()
            assert goal is None

        assert cast(Any, response.is_closed) is True
