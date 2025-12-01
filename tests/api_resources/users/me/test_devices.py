# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.users.me import (
    Device,
    DeviceListResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestDevices:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @parametrize
    def test_method_list(self, client: JamesBurvelOcallaghanIii) -> None:
        device = client.users.me.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    def test_method_list_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        device = client.users.me.devices.list(
            limit={},
            offset={},
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    def test_raw_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    def test_streaming_response_list(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_deregister(self, client: JamesBurvelOcallaghanIii) -> None:
        device = client.users.me.devices.deregister(
            "dev_mobile_ios_aabbcc",
        )
        assert device is None

    @parametrize
    def test_raw_response_deregister(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.devices.with_raw_response.deregister(
            "dev_mobile_ios_aabbcc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert device is None

    @parametrize
    def test_streaming_response_deregister(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.devices.with_streaming_response.deregister(
            "dev_mobile_ios_aabbcc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    def test_method_register(self, client: JamesBurvelOcallaghanIii) -> None:
        device = client.users.me.devices.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
        )
        assert_matches_type(Device, device, path=["response"])

    @parametrize
    def test_method_register_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        device = client.users.me.devices.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
            biometric_signature="base64encoded_android_biometric_proof",
            device_name="Alex's Work Phone",
            push_token="ExponentPushToken[yzzzyzzzyzzzyzzz]",
        )
        assert_matches_type(Device, device, path=["response"])

    @parametrize
    def test_raw_response_register(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.devices.with_raw_response.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = response.parse()
        assert_matches_type(Device, device, path=["response"])

    @parametrize
    def test_streaming_response_register(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.devices.with_streaming_response.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncDevices:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @parametrize
    async def test_method_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        device = await async_client.users.me.devices.list()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    async def test_method_list_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        device = await async_client.users.me.devices.list(
            limit={},
            offset={},
        )
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    async def test_raw_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.devices.with_raw_response.list()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(DeviceListResponse, device, path=["response"])

    @parametrize
    async def test_streaming_response_list(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.devices.with_streaming_response.list() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(DeviceListResponse, device, path=["response"])

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_deregister(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        device = await async_client.users.me.devices.deregister(
            "dev_mobile_ios_aabbcc",
        )
        assert device is None

    @parametrize
    async def test_raw_response_deregister(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.devices.with_raw_response.deregister(
            "dev_mobile_ios_aabbcc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert device is None

    @parametrize
    async def test_streaming_response_deregister(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.devices.with_streaming_response.deregister(
            "dev_mobile_ios_aabbcc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert device is None

        assert cast(Any, response.is_closed) is True

    @parametrize
    async def test_method_register(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        device = await async_client.users.me.devices.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
        )
        assert_matches_type(Device, device, path=["response"])

    @parametrize
    async def test_method_register_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        device = await async_client.users.me.devices.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
            biometric_signature="base64encoded_android_biometric_proof",
            device_name="Alex's Work Phone",
            push_token="ExponentPushToken[yzzzyzzzyzzzyzzz]",
        )
        assert_matches_type(Device, device, path=["response"])

    @parametrize
    async def test_raw_response_register(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.devices.with_raw_response.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        device = await response.parse()
        assert_matches_type(Device, device, path=["response"])

    @parametrize
    async def test_streaming_response_register(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.devices.with_streaming_response.register(
            device_type="mobile",
            model="Samsung Galaxy S24 Ultra",
            os="Android 14",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            device = await response.parse()
            assert_matches_type(Device, device, path=["response"])

        assert cast(Any, response.is_closed) is True
