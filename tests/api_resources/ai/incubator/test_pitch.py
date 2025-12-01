# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.ai.incubator import (
    QuantumWeaverState,
    PitchRetrieveDetailsResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestPitch:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_details(self, client: JamesBurvelOcallaghanIii) -> None:
        pitch = client.ai.incubator.pitch.retrieve_details(
            "pitch_qw_synergychain-xyz",
        )
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    def test_raw_response_retrieve_details(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.incubator.pitch.with_raw_response.retrieve_details(
            "pitch_qw_synergychain-xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_details(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.incubator.pitch.with_streaming_response.retrieve_details(
            "pitch_qw_synergychain-xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        pitch = client.ai.incubator.pitch.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={},
            founding_team=[{}, {}],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    def test_method_submit_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        pitch = client.ai.incubator.pitch.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={
                "profitability_estimate": "Achieve profitability within 18 months.",
                "projection_years": 3,
                "revenue_forecast": [500000, 2000000, 6000000],
                "seed_round_amount": 2500000,
                "valuation_pre_money": 10000000,
            },
            founding_team=[
                {
                    "experience": "15+ years in AI/ML, PhD in Quantum Computing, ex-Google Brain",
                    "name": "Dr. Eleanor Vance",
                    "role": "CEO & Lead AI Scientist",
                },
                {
                    "experience": "20+ years in Fintech, ex-Goldman Sachs",
                    "name": "Marcus Thorne",
                    "role": "COO & Finance Expert",
                },
            ],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    def test_raw_response_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.incubator.pitch.with_raw_response.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={},
            founding_team=[{}, {}],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    def test_streaming_response_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.incubator.pitch.with_streaming_response.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={},
            founding_team=[{}, {}],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert_matches_type(QuantumWeaverState, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_submit_feedback(self, client: JamesBurvelOcallaghanIii) -> None:
        pitch = client.ai.incubator.pitch.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    def test_method_submit_feedback_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        pitch = client.ai.incubator.pitch.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
            answers=[
                {
                    "answer": "Our mitigation strategy includes dedicated R&D and new hires with specific expertise.",
                    "question_id": "q_qa-team-001",
                },
                {
                    "answer": "Our CAC projections are based on pilot program results showing $500 per enterprise client with a conversion rate of 10% from trials.",
                    "question_id": "q_qa-market-002",
                },
            ],
            feedback="Regarding the technical challenges, our team has allocated 3 months for R&D on quantum-resistant cryptography, mitigating the risk. We've also brought in Dr. Elena Petrova, a leading expert in secure multi-party computation.",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    def test_raw_response_submit_feedback(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.ai.incubator.pitch.with_raw_response.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = response.parse()
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    def test_streaming_response_submit_feedback(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.ai.incubator.pitch.with_streaming_response.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = response.parse()
            assert_matches_type(QuantumWeaverState, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncPitch:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        pitch = await async_client.ai.incubator.pitch.retrieve_details(
            "pitch_qw_synergychain-xyz",
        )
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.retrieve_details(
            "pitch_qw_synergychain-xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_details(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.retrieve_details(
            "pitch_qw_synergychain-xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert_matches_type(PitchRetrieveDetailsResponse, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        pitch = await async_client.ai.incubator.pitch.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={},
            founding_team=[{}, {}],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        pitch = await async_client.ai.incubator.pitch.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={
                "profitability_estimate": "Achieve profitability within 18 months.",
                "projection_years": 3,
                "revenue_forecast": [500000, 2000000, 6000000],
                "seed_round_amount": 2500000,
                "valuation_pre_money": 10000000,
            },
            founding_team=[
                {
                    "experience": "15+ years in AI/ML, PhD in Quantum Computing, ex-Google Brain",
                    "name": "Dr. Eleanor Vance",
                    "role": "CEO & Lead AI Scientist",
                },
                {
                    "experience": "20+ years in Fintech, ex-Goldman Sachs",
                    "name": "Marcus Thorne",
                    "role": "COO & Finance Expert",
                },
            ],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={},
            founding_team=[{}, {}],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.submit(
            business_plan="Quantum-AI powered financial advisor platform leveraging neural networks for predictive analytics and hyper-personalized advice...",
            financial_projections={},
            founding_team=[{}, {}],
            market_opportunity="The booming digital finance market coupled with demand for truly personalized, AI-driven financial guidance presents a multi-billion dollar opportunity. Our unique quantum-AI approach provides unparalleled accuracy and foresight.",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert_matches_type(QuantumWeaverState, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_submit_feedback(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        pitch = await async_client.ai.incubator.pitch.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    async def test_method_submit_feedback_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        pitch = await async_client.ai.incubator.pitch.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
            answers=[
                {
                    "answer": "Our mitigation strategy includes dedicated R&D and new hires with specific expertise.",
                    "question_id": "q_qa-team-001",
                },
                {
                    "answer": "Our CAC projections are based on pilot program results showing $500 per enterprise client with a conversion rate of 10% from trials.",
                    "question_id": "q_qa-market-002",
                },
            ],
            feedback="Regarding the technical challenges, our team has allocated 3 months for R&D on quantum-resistant cryptography, mitigating the risk. We've also brought in Dr. Elena Petrova, a leading expert in secure multi-party computation.",
        )
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    async def test_raw_response_submit_feedback(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.ai.incubator.pitch.with_raw_response.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        pitch = await response.parse()
        assert_matches_type(QuantumWeaverState, pitch, path=["response"])

    @parametrize
    async def test_streaming_response_submit_feedback(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.ai.incubator.pitch.with_streaming_response.submit_feedback(
            pitch_id="pitch_qw_synergychain-xyz",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            pitch = await response.parse()
            assert_matches_type(QuantumWeaverState, pitch, path=["response"])

        assert cast(Any, response.is_closed) is True
