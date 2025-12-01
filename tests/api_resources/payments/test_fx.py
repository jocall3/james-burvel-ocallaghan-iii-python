# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.payments import (
    FxConvertResponse,
    FxRetrieveRatesResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestFx:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_convert(self, client: JamesBurvelOcallaghanIii) -> None:
        fx = client.payments.fx.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
        )
        assert_matches_type(FxConvertResponse, fx, path=["response"])

    @parametrize
    def test_method_convert_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        fx = client.payments.fx.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
            fx_rate_lock=True,
            target_account_id="acc_euro_savings_9876",
        )
        assert_matches_type(FxConvertResponse, fx, path=["response"])

    @parametrize
    def test_raw_response_convert(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.payments.fx.with_raw_response.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fx = response.parse()
        assert_matches_type(FxConvertResponse, fx, path=["response"])

    @parametrize
    def test_streaming_response_convert(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.payments.fx.with_streaming_response.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fx = response.parse()
            assert_matches_type(FxConvertResponse, fx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_retrieve_rates(self, client: JamesBurvelOcallaghanIii) -> None:
        fx = client.payments.fx.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
        )
        assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

    @parametrize
    def test_method_retrieve_rates_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        fx = client.payments.fx.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
            forecast_days=7,
        )
        assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

    @parametrize
    def test_raw_response_retrieve_rates(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.payments.fx.with_raw_response.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fx = response.parse()
        assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_rates(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.payments.fx.with_streaming_response.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fx = response.parse()
            assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncFx:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_convert(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        fx = await async_client.payments.fx.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
        )
        assert_matches_type(FxConvertResponse, fx, path=["response"])

    @parametrize
    async def test_method_convert_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        fx = await async_client.payments.fx.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
            fx_rate_lock=True,
            target_account_id="acc_euro_savings_9876",
        )
        assert_matches_type(FxConvertResponse, fx, path=["response"])

    @parametrize
    async def test_raw_response_convert(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.payments.fx.with_raw_response.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fx = await response.parse()
        assert_matches_type(FxConvertResponse, fx, path=["response"])

    @parametrize
    async def test_streaming_response_convert(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.payments.fx.with_streaming_response.convert(
            source_account_id="acc_chase_checking_4567",
            source_amount=1000,
            source_currency="USD",
            target_currency="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fx = await response.parse()
            assert_matches_type(FxConvertResponse, fx, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_retrieve_rates(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        fx = await async_client.payments.fx.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
        )
        assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

    @parametrize
    async def test_method_retrieve_rates_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        fx = await async_client.payments.fx.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
            forecast_days=7,
        )
        assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_rates(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.payments.fx.with_raw_response.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        fx = await response.parse()
        assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_rates(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.payments.fx.with_streaming_response.retrieve_rates(
            base_currency="USD",
            target_currency="EUR",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            fx = await response.parse()
            assert_matches_type(FxRetrieveRatesResponse, fx, path=["response"])

        assert cast(Any, response.is_closed) is True
