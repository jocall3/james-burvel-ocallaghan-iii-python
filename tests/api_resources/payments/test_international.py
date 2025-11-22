# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.payments import InternationalPaymentStatus

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestInternational:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate(self, client: JamesBurvelOcallaghanIii) -> None:
        international = client.payments.international.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
        )
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_initiate_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        international = client.payments.international.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
                "account_number": "accountNumber",
                "iban": "DE89370400440532013000",
                "routing_number": "routingNumber",
                "swift_bic": "DEUTDEFF",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
            fx_rate_lock=True,
            fx_rate_provider="proprietary_ai",
            reference="reference",
        )
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_initiate(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.payments.international.with_raw_response.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_initiate(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.payments.international.with_streaming_response.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert_matches_type(InternationalPaymentStatus, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        international = client.payments.international.retrieve_status(
            "int_pmt_xyz7890",
        )
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.payments.international.with_raw_response.retrieve_status(
            "int_pmt_xyz7890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = response.parse()
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.payments.international.with_streaming_response.retrieve_status(
            "int_pmt_xyz7890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = response.parse()
            assert_matches_type(InternationalPaymentStatus, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_retrieve_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            client.payments.international.with_raw_response.retrieve_status(
                "",
            )


class TestAsyncInternational:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        international = await async_client.payments.international.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
        )
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_initiate_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        international = await async_client.payments.international.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
                "account_number": "accountNumber",
                "iban": "DE89370400440532013000",
                "routing_number": "routingNumber",
                "swift_bic": "DEUTDEFF",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
            fx_rate_lock=True,
            fx_rate_provider="proprietary_ai",
            reference="reference",
        )
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_initiate(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.payments.international.with_raw_response.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_initiate(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.payments.international.with_streaming_response.initiate(
            amount=5000,
            beneficiary={
                "address": "Hauptstrasse 1, 10115 Berlin, Germany",
                "bank_name": "Deutsche Bank",
                "name": "Maria Schmidt",
            },
            purpose="Vendor payment for Q2 services.",
            source_account_id="acc_chase_checking_4567",
            source_currency="USD",
            target_currency="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert_matches_type(InternationalPaymentStatus, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        international = await async_client.payments.international.retrieve_status(
            "int_pmt_xyz7890",
        )
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.payments.international.with_raw_response.retrieve_status(
            "int_pmt_xyz7890",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        international = await response.parse()
        assert_matches_type(InternationalPaymentStatus, international, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.payments.international.with_streaming_response.retrieve_status(
            "int_pmt_xyz7890",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            international = await response.parse()
            assert_matches_type(InternationalPaymentStatus, international, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_retrieve_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `payment_id` but received ''"):
            await async_client.payments.international.with_raw_response.retrieve_status(
                "",
            )
