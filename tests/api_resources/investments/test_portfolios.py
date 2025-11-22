# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.investments import (
    InvestmentPortfolio,
    PortfolioListResponse,
    PortfolioRebalanceResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPortfolios:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
            ai_auto_allocate=True,
            linked_account_id="acc_chase_checking_4567",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.investments.portfolios.with_raw_response.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.investments.portfolios.with_streaming_response.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.retrieve(
            "portfolio_equity_growth",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.investments.portfolios.with_raw_response.retrieve(
            "portfolio_equity_growth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.investments.portfolios.with_streaming_response.retrieve(
            "portfolio_equity_growth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            client.investments.portfolios.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.update(
            portfolio_id="portfolio_equity_growth",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.update(
            portfolio_id="portfolio_equity_growth",
            ai_rebalancing_frequency="quarterly",
            name="Refined Growth Portfolio",
            risk_tolerance="medium",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.investments.portfolios.with_raw_response.update(
            portfolio_id="portfolio_equity_growth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.investments.portfolios.with_streaming_response.update(
            portfolio_id="portfolio_equity_growth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            client.investments.portfolios.with_raw_response.update(
                portfolio_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.list()
        assert_matches_type(PortfolioListResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.investments.portfolios.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(PortfolioListResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.investments.portfolios.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(PortfolioListResponse, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rebalance(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
        )
        assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_rebalance_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        portfolio = client.investments.portfolios.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
            confirmation_required=True,
            dry_run=True,
        )
        assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_rebalance(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.investments.portfolios.with_raw_response.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = response.parse()
        assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_rebalance(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.investments.portfolios.with_streaming_response.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = response.parse()
            assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_rebalance(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            client.investments.portfolios.with_raw_response.rebalance(
                portfolio_id="",
                target_risk_tolerance="medium",
            )


class TestAsyncPortfolios:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
            ai_auto_allocate=True,
            linked_account_id="acc_chase_checking_4567",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.investments.portfolios.with_raw_response.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.investments.portfolios.with_streaming_response.create(
            currency="USD",
            initial_investment=10000,
            name="My First Growth Portfolio",
            risk_tolerance="medium",
            type="diversified",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.retrieve(
            "portfolio_equity_growth",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.investments.portfolios.with_raw_response.retrieve(
            "portfolio_equity_growth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.investments.portfolios.with_streaming_response.retrieve(
            "portfolio_equity_growth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            await async_client.investments.portfolios.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.update(
            portfolio_id="portfolio_equity_growth",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.update(
            portfolio_id="portfolio_equity_growth",
            ai_rebalancing_frequency="quarterly",
            name="Refined Growth Portfolio",
            risk_tolerance="medium",
        )
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.investments.portfolios.with_raw_response.update(
            portfolio_id="portfolio_equity_growth",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.investments.portfolios.with_streaming_response.update(
            portfolio_id="portfolio_equity_growth",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(InvestmentPortfolio, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            await async_client.investments.portfolios.with_raw_response.update(
                portfolio_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.list()
        assert_matches_type(PortfolioListResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.investments.portfolios.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(PortfolioListResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.investments.portfolios.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(PortfolioListResponse, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rebalance(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
        )
        assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_rebalance_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        portfolio = await async_client.investments.portfolios.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
            confirmation_required=True,
            dry_run=True,
        )
        assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_rebalance(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.investments.portfolios.with_raw_response.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        portfolio = await response.parse()
        assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_rebalance(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.investments.portfolios.with_streaming_response.rebalance(
            portfolio_id="portfolio_equity_growth",
            target_risk_tolerance="medium",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            portfolio = await response.parse()
            assert_matches_type(PortfolioRebalanceResponse, portfolio, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_rebalance(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `portfolio_id` but received ''"):
            await async_client.investments.portfolios.with_raw_response.rebalance(
                portfolio_id="",
                target_risk_tolerance="medium",
            )
