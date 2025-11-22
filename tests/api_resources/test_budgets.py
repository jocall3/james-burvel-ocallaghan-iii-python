# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import Budget, BudgetListResponse
from james_burvel_ocallaghan_iii._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBudgets:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
            ai_auto_populate=True,
            alert_threshold=75,
            categories=[
                {
                    "allocated": 1500,
                    "name": "Rent",
                },
                {
                    "allocated": 400,
                    "name": "Groceries",
                },
            ],
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.budgets.with_raw_response.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.budgets.with_streaming_response.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(Budget, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.retrieve(
            "budget_monthly_aug",
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.budgets.with_raw_response.retrieve(
            "budget_monthly_aug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.budgets.with_streaming_response.retrieve(
            "budget_monthly_aug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(Budget, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.update(
            budget_id="budget_monthly_aug",
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.update(
            budget_id="budget_monthly_aug",
            alert_threshold=85,
            categories=[
                {
                    "allocated": 1600,
                    "name": "Rent",
                }
            ],
            end_date=parse_date("2024-09-30"),
            name="September Household Budget",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            status="active",
            total_amount=3200,
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.budgets.with_raw_response.update(
            budget_id="budget_monthly_aug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.budgets.with_streaming_response.update(
            budget_id="budget_monthly_aug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(Budget, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.update(
                budget_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.list()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.budgets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.budgets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert_matches_type(BudgetListResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        budget = client.budgets.delete(
            "budget_monthly_aug",
        )
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.budgets.with_raw_response.delete(
            "budget_monthly_aug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = response.parse()
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.budgets.with_streaming_response.delete(
            "budget_monthly_aug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = response.parse()
            assert budget is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_delete(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            client.budgets.with_raw_response.delete(
                "",
            )


class TestAsyncBudgets:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
            ai_auto_populate=True,
            alert_threshold=75,
            categories=[
                {
                    "allocated": 1500,
                    "name": "Rent",
                },
                {
                    "allocated": 400,
                    "name": "Groceries",
                },
            ],
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.budgets.with_raw_response.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.budgets.with_streaming_response.create(
            end_date=parse_date("2024-09-30"),
            name="September Living Expenses",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            total_amount=2800,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(Budget, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.retrieve(
            "budget_monthly_aug",
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.budgets.with_raw_response.retrieve(
            "budget_monthly_aug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.budgets.with_streaming_response.retrieve(
            "budget_monthly_aug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(Budget, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.update(
            budget_id="budget_monthly_aug",
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.update(
            budget_id="budget_monthly_aug",
            alert_threshold=85,
            categories=[
                {
                    "allocated": 1600,
                    "name": "Rent",
                }
            ],
            end_date=parse_date("2024-09-30"),
            name="September Household Budget",
            period="monthly",
            start_date=parse_date("2024-09-01"),
            status="active",
            total_amount=3200,
        )
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.budgets.with_raw_response.update(
            budget_id="budget_monthly_aug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(Budget, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.budgets.with_streaming_response.update(
            budget_id="budget_monthly_aug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(Budget, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.update(
                budget_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.list()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.budgets.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert_matches_type(BudgetListResponse, budget, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.budgets.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert_matches_type(BudgetListResponse, budget, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        budget = await async_client.budgets.delete(
            "budget_monthly_aug",
        )
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.budgets.with_raw_response.delete(
            "budget_monthly_aug",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        budget = await response.parse()
        assert budget is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.budgets.with_streaming_response.delete(
            "budget_monthly_aug",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            budget = await response.parse()
            assert budget is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_delete(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `budget_id` but received ''"):
            await async_client.budgets.with_raw_response.delete(
                "",
            )
