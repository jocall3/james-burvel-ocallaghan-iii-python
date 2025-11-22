# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii._utils import parse_date
from james_burvel_ocallaghan_iii.types.identity import KYCStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestKYC:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        kyc = client.identity.kyc.retrieve_status()
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.identity.kyc.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.identity.kyc.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KYCStatus, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        kyc = client.identity.kyc.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
        )
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_submit_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        kyc = client.identity.kyc.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
            address_proof_image="U3RhaW5sZXNzIHJvY2tz",
            document_back_image="U3RhaW5sZXNzIHJvY2tz",
            live_selfie_image="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.identity.kyc.with_raw_response.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = response.parse()
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_submit(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.identity.kyc.with_streaming_response.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = response.parse()
            assert_matches_type(KYCStatus, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncKYC:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        kyc = await async_client.identity.kyc.retrieve_status()
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.identity.kyc.with_raw_response.retrieve_status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.identity.kyc.with_streaming_response.retrieve_status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KYCStatus, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        kyc = await async_client.identity.kyc.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
        )
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_submit_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        kyc = await async_client.identity.kyc.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
            address_proof_image="U3RhaW5sZXNzIHJvY2tz",
            document_back_image="U3RhaW5sZXNzIHJvY2tz",
            live_selfie_image="U3RhaW5sZXNzIHJvY2tz",
        )
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.identity.kyc.with_raw_response.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        kyc = await response.parse()
        assert_matches_type(KYCStatus, kyc, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_submit(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.identity.kyc.with_streaming_response.submit(
            country_of_issue="US",
            document_front_image="U3RhaW5sZXNzIHJvY2tz",
            document_number="ABC12345",
            document_type="drivers_license",
            expiration_date=parse_date("2030-01-01"),
            issue_date=parse_date("2020-01-01"),
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            kyc = await response.parse()
            assert_matches_type(KYCStatus, kyc, path=["response"])

        assert cast(Any, response.is_closed) is True
