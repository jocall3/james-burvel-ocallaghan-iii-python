# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import (
    CorporatePerformSanctionScreeningResponse,
)
from james_burvel_ocallaghan_iii._utils import parse_date

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCorporate:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_perform_sanction_screening(self, client: JamesBurvelOcallaghanIii) -> None:
        corporate = client.corporate.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
        )
        assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_perform_sanction_screening_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        corporate = client.corporate.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
            address={
                "city": "Quantumville",
                "country": "USA",
                "state": "CA",
                "street": "100 Innovation Drive",
                "zip": "90210",
            },
            date_of_birth=parse_date("1970-01-01"),
            identification_number="identificationNumber",
        )
        assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_perform_sanction_screening(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.with_raw_response.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        corporate = response.parse()
        assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_perform_sanction_screening(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.with_streaming_response.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            corporate = response.parse()
            assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncCorporate:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_perform_sanction_screening(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        corporate = await async_client.corporate.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
        )
        assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_perform_sanction_screening_with_all_params(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        corporate = await async_client.corporate.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
            address={
                "city": "Quantumville",
                "country": "USA",
                "state": "CA",
                "street": "100 Innovation Drive",
                "zip": "90210",
            },
            date_of_birth=parse_date("1970-01-01"),
            identification_number="identificationNumber",
        )
        assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_perform_sanction_screening(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.with_raw_response.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        corporate = await response.parse()
        assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_perform_sanction_screening(
        self, async_client: AsyncJamesBurvelOcallaghanIii
    ) -> None:
        async with async_client.corporate.with_streaming_response.perform_sanction_screening(
            country="US",
            entity_type="individual",
            name="John Doe",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            corporate = await response.parse()
            assert_matches_type(CorporatePerformSanctionScreeningResponse, corporate, path=["response"])

        assert cast(Any, response.is_closed) is True
