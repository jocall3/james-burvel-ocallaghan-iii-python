# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.marketplace import (
    ProductListResponse,
    ProductClaimOfferResponse,
    ProductSimulatePurchaseResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestProducts:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        product = client.marketplace.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        product = client.marketplace.products.list(
            category="Smart Home Devices",
            limit=2,
            offset=0,
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.marketplace.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.marketplace.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_claim_offer(self, client: JamesBurvelOcallaghanIii) -> None:
        product = client.marketplace.products.claim_offer(
            product_id="prod_smart_thermostat_001",
        )
        assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_claim_offer_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        product = client.marketplace.products.claim_offer(
            product_id="prod_smart_thermostat_001",
            redemption_channel="in_app",
        )
        assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_claim_offer(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.marketplace.products.with_raw_response.claim_offer(
            product_id="prod_smart_thermostat_001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_claim_offer(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.marketplace.products.with_streaming_response.claim_offer(
            product_id="prod_smart_thermostat_001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_claim_offer(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.marketplace.products.with_raw_response.claim_offer(
                product_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_simulate_purchase(self, client: JamesBurvelOcallaghanIii) -> None:
        product = client.marketplace.products.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
        )
        assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_simulate_purchase_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        product = client.marketplace.products.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
            target_account_id="acc_chase_checking_4567",
        )
        assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_simulate_purchase(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.marketplace.products.with_raw_response.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = response.parse()
        assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_simulate_purchase(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.marketplace.products.with_streaming_response.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = response.parse()
            assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_simulate_purchase(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            client.marketplace.products.with_raw_response.simulate_purchase(
                product_id="",
                purchase_option="financed_12_months",
            )


class TestAsyncProducts:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        product = await async_client.marketplace.products.list()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        product = await async_client.marketplace.products.list(
            category="Smart Home Devices",
            limit=2,
            offset=0,
        )
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.marketplace.products.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductListResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.marketplace.products.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductListResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_claim_offer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        product = await async_client.marketplace.products.claim_offer(
            product_id="prod_smart_thermostat_001",
        )
        assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_claim_offer_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        product = await async_client.marketplace.products.claim_offer(
            product_id="prod_smart_thermostat_001",
            redemption_channel="in_app",
        )
        assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_claim_offer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.marketplace.products.with_raw_response.claim_offer(
            product_id="prod_smart_thermostat_001",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_claim_offer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.marketplace.products.with_streaming_response.claim_offer(
            product_id="prod_smart_thermostat_001",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductClaimOfferResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_claim_offer(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.marketplace.products.with_raw_response.claim_offer(
                product_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_simulate_purchase(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        product = await async_client.marketplace.products.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
        )
        assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_simulate_purchase_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        product = await async_client.marketplace.products.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
            target_account_id="acc_chase_checking_4567",
        )
        assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_simulate_purchase(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.marketplace.products.with_raw_response.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        product = await response.parse()
        assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_simulate_purchase(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.marketplace.products.with_streaming_response.simulate_purchase(
            product_id="prod_smart_thermostat_001",
            purchase_option="financed_12_months",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            product = await response.parse()
            assert_matches_type(ProductSimulatePurchaseResponse, product, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_simulate_purchase(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `product_id` but received ''"):
            await async_client.marketplace.products.with_raw_response.simulate_purchase(
                product_id="",
                purchase_option="financed_12_months",
            )
