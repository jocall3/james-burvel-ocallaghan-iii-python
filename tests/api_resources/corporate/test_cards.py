# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types import PaginatedTransactions
from james_burvel_ocallaghan_iii._utils import parse_date
from james_burvel_ocallaghan_iii.types.corporate import (
    CorporateCard,
    CardListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestCards:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.list()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_virtual(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.create_virtual(
            controls={},
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_create_virtual_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.create_virtual(
            controls={
                "atm_withdrawals": False,
                "contactless_payments": False,
                "daily_limit": 500,
                "international_transactions": False,
                "merchant_category_restrictions": ["Advertising"],
                "monthly_limit": 1000,
                "online_transactions": True,
                "single_transaction_limit": 200,
                "vendor_restrictions": ["Facebook Ads", "Google Ads"],
            },
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
            associated_employee_id="emp_marketing_01",
            spending_policy_id="policy_marketing_fixed",
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_create_virtual(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.cards.with_raw_response.create_virtual(
            controls={},
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_create_virtual(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.cards.with_streaming_response.create_virtual(
            controls={},
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CorporateCard, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_freeze(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.freeze(
            card_id="corp_card_xyz987654",
            freeze=True,
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_freeze(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.cards.with_raw_response.freeze(
            card_id="corp_card_xyz987654",
            freeze=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_freeze(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.cards.with_streaming_response.freeze(
            card_id="corp_card_xyz987654",
            freeze=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CorporateCard, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_freeze(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.corporate.cards.with_raw_response.freeze(
                card_id="",
                freeze=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.list_transactions(
            card_id="corp_card_xyz987654",
        )
        assert_matches_type(PaginatedTransactions, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_list_transactions_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.list_transactions(
            card_id="corp_card_xyz987654",
            end_date=parse_date("2024-12-31"),
            limit=1,
            offset=0,
            start_date=parse_date("2024-01-01"),
        )
        assert_matches_type(PaginatedTransactions, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_list_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.cards.with_raw_response.list_transactions(
            card_id="corp_card_xyz987654",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(PaginatedTransactions, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_list_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.cards.with_streaming_response.list_transactions(
            card_id="corp_card_xyz987654",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(PaginatedTransactions, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_list_transactions(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.corporate.cards.with_raw_response.list_transactions(
                card_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_controls(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.update_controls(
            card_id="corp_card_xyz987654",
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_update_controls_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        card = client.corporate.cards.update_controls(
            card_id="corp_card_xyz987654",
            atm_withdrawals=True,
            contactless_payments=True,
            daily_limit=750,
            international_transactions=True,
            merchant_category_restrictions=["Software Subscriptions", "Conferences"],
            monthly_limit=3000,
            online_transactions=True,
            single_transaction_limit=1000,
            vendor_restrictions=["Amazon", "Uber"],
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_update_controls(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.corporate.cards.with_raw_response.update_controls(
            card_id="corp_card_xyz987654",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = response.parse()
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_update_controls(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.corporate.cards.with_streaming_response.update_controls(
            card_id="corp_card_xyz987654",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = response.parse()
            assert_matches_type(CorporateCard, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_path_params_update_controls(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            client.corporate.cards.with_raw_response.update_controls(
                card_id="",
            )


class TestAsyncCards:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.list()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.list(
            limit=1,
            offset=0,
        )
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.cards.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CardListResponse, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.cards.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CardListResponse, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_virtual(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.create_virtual(
            controls={},
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_create_virtual_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.create_virtual(
            controls={
                "atm_withdrawals": False,
                "contactless_payments": False,
                "daily_limit": 500,
                "international_transactions": False,
                "merchant_category_restrictions": ["Advertising"],
                "monthly_limit": 1000,
                "online_transactions": True,
                "single_transaction_limit": 200,
                "vendor_restrictions": ["Facebook Ads", "Google Ads"],
            },
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
            associated_employee_id="emp_marketing_01",
            spending_policy_id="policy_marketing_fixed",
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_create_virtual(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.cards.with_raw_response.create_virtual(
            controls={},
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_create_virtual(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.cards.with_streaming_response.create_virtual(
            controls={},
            expiration_date=parse_date("2025-12-31"),
            holder_name="Marketing Campaign Q4",
            purpose="Online advertising for Q4 campaigns",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CorporateCard, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_freeze(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.freeze(
            card_id="corp_card_xyz987654",
            freeze=True,
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_freeze(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.cards.with_raw_response.freeze(
            card_id="corp_card_xyz987654",
            freeze=True,
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_freeze(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.cards.with_streaming_response.freeze(
            card_id="corp_card_xyz987654",
            freeze=True,
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CorporateCard, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_freeze(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.corporate.cards.with_raw_response.freeze(
                card_id="",
                freeze=True,
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_transactions(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.list_transactions(
            card_id="corp_card_xyz987654",
        )
        assert_matches_type(PaginatedTransactions, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_list_transactions_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.list_transactions(
            card_id="corp_card_xyz987654",
            end_date=parse_date("2024-12-31"),
            limit=1,
            offset=0,
            start_date=parse_date("2024-01-01"),
        )
        assert_matches_type(PaginatedTransactions, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_list_transactions(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.cards.with_raw_response.list_transactions(
            card_id="corp_card_xyz987654",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(PaginatedTransactions, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_list_transactions(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.cards.with_streaming_response.list_transactions(
            card_id="corp_card_xyz987654",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(PaginatedTransactions, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_list_transactions(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.corporate.cards.with_raw_response.list_transactions(
                card_id="",
            )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_controls(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.update_controls(
            card_id="corp_card_xyz987654",
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_update_controls_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        card = await async_client.corporate.cards.update_controls(
            card_id="corp_card_xyz987654",
            atm_withdrawals=True,
            contactless_payments=True,
            daily_limit=750,
            international_transactions=True,
            merchant_category_restrictions=["Software Subscriptions", "Conferences"],
            monthly_limit=3000,
            online_transactions=True,
            single_transaction_limit=1000,
            vendor_restrictions=["Amazon", "Uber"],
        )
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_update_controls(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.corporate.cards.with_raw_response.update_controls(
            card_id="corp_card_xyz987654",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        card = await response.parse()
        assert_matches_type(CorporateCard, card, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_update_controls(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.corporate.cards.with_streaming_response.update_controls(
            card_id="corp_card_xyz987654",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            card = await response.parse()
            assert_matches_type(CorporateCard, card, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_path_params_update_controls(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `card_id` but received ''"):
            await async_client.corporate.cards.with_raw_response.update_controls(
                card_id="",
            )
