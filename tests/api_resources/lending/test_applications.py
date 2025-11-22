# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.lending import LoanApplicationStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestApplications:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        application = client.lending.applications.retrieve(
            "loan_app_creditflow-123",
        )
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.lending.applications.with_raw_response.retrieve(
            "loan_app_creditflow-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.lending.applications.with_streaming_response.retrieve(
            "loan_app_creditflow-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(LoanApplicationStatus, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            client.lending.applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        application = client.lending.applications.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
        )
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        application = client.lending.applications.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
            additional_notes="Funds needed to replace a broken HVAC system.",
            co_applicant={
                "email": "jane.doe@example.com",
                "income": 75000,
                "name": "Jane Doe",
            },
        )
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.lending.applications.with_raw_response.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = response.parse()
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.lending.applications.with_streaming_response.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = response.parse()
            assert_matches_type(LoanApplicationStatus, application, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncApplications:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        application = await async_client.lending.applications.retrieve(
            "loan_app_creditflow-123",
        )
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.lending.applications.with_raw_response.retrieve(
            "loan_app_creditflow-123",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.lending.applications.with_streaming_response.retrieve(
            "loan_app_creditflow-123",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(LoanApplicationStatus, application, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `application_id` but received ''"):
            await async_client.lending.applications.with_raw_response.retrieve(
                "",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        application = await async_client.lending.applications.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
        )
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        application = await async_client.lending.applications.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
            additional_notes="Funds needed to replace a broken HVAC system.",
            co_applicant={
                "email": "jane.doe@example.com",
                "income": 75000,
                "name": "Jane Doe",
            },
        )
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.lending.applications.with_raw_response.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        application = await response.parse()
        assert_matches_type(LoanApplicationStatus, application, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.lending.applications.with_streaming_response.submit(
            loan_amount=10000,
            loan_purpose="home_improvement",
            repayment_term_months=36,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            application = await response.parse()
            assert_matches_type(LoanApplicationStatus, application, path=["response"])

        assert cast(Any, response.is_closed) is True
