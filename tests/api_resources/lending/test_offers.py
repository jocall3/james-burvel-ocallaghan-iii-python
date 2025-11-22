# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.lending import OfferListPreApprovedResponse

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOffers:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list_pre_approved(self, client: JamesBurvelOcallaghanIii) -> None:
        offer = client.lending.offers.list_pre_approved()
        assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

    @parametrize
    def test_method_list_pre_approved_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        offer = client.lending.offers.list_pre_approved(
            limit=1,
            offset=0,
        )
        assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

    @parametrize
    def test_raw_response_list_pre_approved(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.lending.offers.with_raw_response.list_pre_approved()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offer = response.parse()
        assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

    @parametrize
    def test_streaming_response_list_pre_approved(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.lending.offers.with_streaming_response.list_pre_approved() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offer = response.parse()
            assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncOffers:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list_pre_approved(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        offer = await async_client.lending.offers.list_pre_approved()
        assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

    @parametrize
    async def test_method_list_pre_approved_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        offer = await async_client.lending.offers.list_pre_approved(
            limit=1,
            offset=0,
        )
        assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

    @parametrize
    async def test_raw_response_list_pre_approved(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.lending.offers.with_raw_response.list_pre_approved()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        offer = await response.parse()
        assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

    @parametrize
    async def test_streaming_response_list_pre_approved(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.lending.offers.with_streaming_response.list_pre_approved() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            offer = await response.parse()
            assert_matches_type(OfferListPreApprovedResponse, offer, path=["response"])

        assert cast(Any, response.is_closed) is True
