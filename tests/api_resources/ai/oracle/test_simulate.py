# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.ai.oracle import (
    SimulationResponse,
    AdvancedSimulationResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestSimulate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_advanced(self, client: JamesBurvelOcallaghanIii) -> None:
        simulate = client.ai.oracle.simulate.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                }
            ],
        )
        assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_advanced_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        simulate = client.ai.oracle.simulate.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                            "start_month": 1,
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                            "start_month": 1,
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                    "duration_years": 10,
                    "sensitivity_analysis_params": [
                        {
                            "max": 0.07,
                            "min": 0.03,
                            "param_name": "marketRecoveryRate",
                            "step": 0.01,
                        }
                    ],
                }
            ],
            duration_years=10,
            initial_state={
                "monthly_income_override": 8000,
                "net_worth_override": 500000,
            },
            sensitivity_analysis_params=[
                {
                    "max": 0.07,
                    "min": 0.03,
                    "param_name": "marketRecoveryRate",
                    "step": 0.01,
                }
            ],
        )
        assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_advanced(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.oracle.simulate.with_raw_response.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = response.parse()
        assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_advanced(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.oracle.simulate.with_streaming_response.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = response.parse()
            assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_standard(self, client: JamesBurvelOcallaghanIii) -> None:
        simulate = client.ai.oracle.simulate.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
        )
        assert_matches_type(SimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_run_standard_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        simulate = client.ai.oracle.simulate.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
            parameters={
                "durationYears": "bar",
                "monthlyInvestmentAmount": "bar",
                "riskTolerance": "bar",
            },
        )
        assert_matches_type(SimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_run_standard(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.oracle.simulate.with_raw_response.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = response.parse()
        assert_matches_type(SimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_run_standard(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.oracle.simulate.with_streaming_response.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = response.parse()
            assert_matches_type(SimulationResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncSimulate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_advanced(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        simulate = await async_client.ai.oracle.simulate.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                }
            ],
        )
        assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_advanced_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        simulate = await async_client.ai.oracle.simulate.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                            "start_month": 1,
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                            "start_month": 1,
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                    "duration_years": 10,
                    "sensitivity_analysis_params": [
                        {
                            "max": 0.07,
                            "min": 0.03,
                            "param_name": "marketRecoveryRate",
                            "step": 0.01,
                        }
                    ],
                }
            ],
            duration_years=10,
            initial_state={
                "monthly_income_override": 8000,
                "net_worth_override": 500000,
            },
            sensitivity_analysis_params=[
                {
                    "max": 0.07,
                    "min": 0.03,
                    "param_name": "marketRecoveryRate",
                    "step": 0.01,
                }
            ],
        )
        assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_advanced(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.oracle.simulate.with_raw_response.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                }
            ],
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = await response.parse()
        assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_advanced(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.oracle.simulate.with_streaming_response.run_advanced(
            prompt="Evaluate the long-term impact of a sudden job loss combined with a variable market downturn, analyzing worst-case and best-case recovery scenarios over a decade.",
            scenarios=[
                {
                    "events": [
                        {
                            "details": {
                                "durationMonths": "bar",
                                "severanceAmount": "bar",
                                "unemploymentBenefits": "bar",
                            },
                            "type": "job_loss",
                        },
                        {
                            "details": {
                                "impactPercentage": "bar",
                                "recoveryYears": "bar",
                            },
                            "type": "market_downturn",
                        },
                    ],
                    "name": "Job Loss & Mild Market Recovery",
                }
            ],
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = await response.parse()
            assert_matches_type(AdvancedSimulationResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_standard(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        simulate = await async_client.ai.oracle.simulate.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
        )
        assert_matches_type(SimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_run_standard_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        simulate = await async_client.ai.oracle.simulate.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
            parameters={
                "durationYears": "bar",
                "monthlyInvestmentAmount": "bar",
                "riskTolerance": "bar",
            },
        )
        assert_matches_type(SimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_run_standard(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.oracle.simulate.with_raw_response.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        simulate = await response.parse()
        assert_matches_type(SimulationResponse, simulate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_run_standard(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.oracle.simulate.with_streaming_response.run_standard(
            prompt="What if I invest an additional $1,000 per month into my aggressive growth portfolio for the next 5 years?",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            simulate = await response.parse()
            assert_matches_type(SimulationResponse, simulate, path=["response"])

        assert cast(Any, response.is_closed) is True
