# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.accounts import OverdraftSettings

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestOverdraftSettings:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_retrieve_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        overdraft_setting = client.accounts.overdraft_settings.retrieve_settings(
            "acc_chase_checking_4567",
        )
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    def test_raw_response_retrieve_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.overdraft_settings.with_raw_response.retrieve_settings(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft_setting = response.parse()
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    def test_streaming_response_retrieve_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.overdraft_settings.with_streaming_response.retrieve_settings(
            "acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft_setting = response.parse()
            assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_retrieve_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.overdraft_settings.with_raw_response.retrieve_settings(
                "",
            )

    @parametrize
    def test_method_update_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        overdraft_setting = client.accounts.overdraft_settings.update_settings(
            account_id="acc_chase_checking_4567",
        )
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    def test_method_update_settings_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        overdraft_setting = client.accounts.overdraft_settings.update_settings(
            account_id="acc_chase_checking_4567",
            enabled=False,
            fee_preference="decline_if_over_limit",
            linked_savings_account_id="acc_new_savings_5678",
            link_to_savings=False,
            protection_limit=750,
        )
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    def test_raw_response_update_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.accounts.overdraft_settings.with_raw_response.update_settings(
            account_id="acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft_setting = response.parse()
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    def test_streaming_response_update_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.accounts.overdraft_settings.with_streaming_response.update_settings(
            account_id="acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft_setting = response.parse()
            assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_path_params_update_settings(self, client: JamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            client.accounts.overdraft_settings.with_raw_response.update_settings(
                account_id="",
            )


class TestAsyncOverdraftSettings:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_retrieve_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        overdraft_setting = await async_client.accounts.overdraft_settings.retrieve_settings(
            "acc_chase_checking_4567",
        )
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    async def test_raw_response_retrieve_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.overdraft_settings.with_raw_response.retrieve_settings(
            "acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft_setting = await response.parse()
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    async def test_streaming_response_retrieve_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.accounts.overdraft_settings.with_streaming_response.retrieve_settings(
            "acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft_setting = await response.parse()
            assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_retrieve_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.overdraft_settings.with_raw_response.retrieve_settings(
                "",
            )

    @parametrize
    async def test_method_update_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        overdraft_setting = await async_client.accounts.overdraft_settings.update_settings(
            account_id="acc_chase_checking_4567",
        )
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    async def test_method_update_settings_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        overdraft_setting = await async_client.accounts.overdraft_settings.update_settings(
            account_id="acc_chase_checking_4567",
            enabled=False,
            fee_preference="decline_if_over_limit",
            linked_savings_account_id="acc_new_savings_5678",
            link_to_savings=False,
            protection_limit=750,
        )
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    async def test_raw_response_update_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.accounts.overdraft_settings.with_raw_response.update_settings(
            account_id="acc_chase_checking_4567",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        overdraft_setting = await response.parse()
        assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

    @parametrize
    async def test_streaming_response_update_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.accounts.overdraft_settings.with_streaming_response.update_settings(
            account_id="acc_chase_checking_4567",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            overdraft_setting = await response.parse()
            assert_matches_type(OverdraftSettings, overdraft_setting, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_path_params_update_settings(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        with pytest.raises(ValueError, match=r"Expected a non-empty value for `account_id` but received ''"):
            await async_client.accounts.overdraft_settings.with_raw_response.update_settings(
                account_id="",
            )
