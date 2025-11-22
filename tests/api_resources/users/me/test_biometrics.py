# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

import os
from typing import Any, cast

import pytest

from tests.utils import assert_matches_type
from james_burvel_ocallaghan_iii import JamesBurvelOcallaghanIii, AsyncJamesBurvelOcallaghanIii
from james_burvel_ocallaghan_iii.types.users.me import (
    BiometricStatus,
    BiometricVerifyResponse,
)

base_url = os.environ.get("TEST_API_BASE_URL", "http://127.0.0.1:4010")


class TestBiometrics:
    parametrize = pytest.mark.parametrize("client", [False, True], indirect=True, ids=["loose", "strict"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_deregister(self, client: JamesBurvelOcallaghanIii) -> None:
        biometric = client.users.me.biometrics.deregister()
        assert biometric is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_deregister(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.biometrics.with_raw_response.deregister()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = response.parse()
        assert biometric is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_deregister(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.biometrics.with_streaming_response.deregister() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = response.parse()
            assert biometric is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enroll(self, client: JamesBurvelOcallaghanIii) -> None:
        biometric = client.users.me.biometrics.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
        )
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_enroll_with_all_params(self, client: JamesBurvelOcallaghanIii) -> None:
        biometric = client.users.me.biometrics.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
            device_name="My Primary iPhone",
        )
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_enroll(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.biometrics.with_raw_response.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = response.parse()
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_enroll(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.biometrics.with_streaming_response.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = response.parse()
            assert_matches_type(BiometricStatus, biometric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_status(self, client: JamesBurvelOcallaghanIii) -> None:
        biometric = client.users.me.biometrics.status()
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_status(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.biometrics.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = response.parse()
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_status(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.biometrics.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = response.parse()
            assert_matches_type(BiometricStatus, biometric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_method_verify(self, client: JamesBurvelOcallaghanIii) -> None:
        biometric = client.users.me.biometrics.verify(
            biometric_signature="base64encoded_one_time_fingerprint_proof",
            biometric_type="fingerprint",
            device_id="dev_mobile_android_ddeeff",
        )
        assert_matches_type(BiometricVerifyResponse, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_raw_response_verify(self, client: JamesBurvelOcallaghanIii) -> None:
        response = client.users.me.biometrics.with_raw_response.verify(
            biometric_signature="base64encoded_one_time_fingerprint_proof",
            biometric_type="fingerprint",
            device_id="dev_mobile_android_ddeeff",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = response.parse()
        assert_matches_type(BiometricVerifyResponse, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    def test_streaming_response_verify(self, client: JamesBurvelOcallaghanIii) -> None:
        with client.users.me.biometrics.with_streaming_response.verify(
            biometric_signature="base64encoded_one_time_fingerprint_proof",
            biometric_type="fingerprint",
            device_id="dev_mobile_android_ddeeff",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = response.parse()
            assert_matches_type(BiometricVerifyResponse, biometric, path=["response"])

        assert cast(Any, response.is_closed) is True


class TestAsyncBiometrics:
    parametrize = pytest.mark.parametrize(
        "async_client", [False, True, {"http_client": "aiohttp"}], indirect=True, ids=["loose", "strict", "aiohttp"]
    )

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_deregister(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        biometric = await async_client.users.me.biometrics.deregister()
        assert biometric is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_deregister(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.biometrics.with_raw_response.deregister()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = await response.parse()
        assert biometric is None

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_deregister(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.biometrics.with_streaming_response.deregister() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = await response.parse()
            assert biometric is None

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enroll(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        biometric = await async_client.users.me.biometrics.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
        )
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_enroll_with_all_params(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        biometric = await async_client.users.me.biometrics.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
            device_name="My Primary iPhone",
        )
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_enroll(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.biometrics.with_raw_response.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = await response.parse()
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_enroll(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.biometrics.with_streaming_response.enroll(
            biometric_signature="base64encoded_facial_template_for_enrollment",
            biometric_type="facial_recognition",
            device_id="dev_mobile_ios_aabbcc",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = await response.parse()
            assert_matches_type(BiometricStatus, biometric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        biometric = await async_client.users.me.biometrics.status()
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.biometrics.with_raw_response.status()

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = await response.parse()
        assert_matches_type(BiometricStatus, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_status(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.biometrics.with_streaming_response.status() as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = await response.parse()
            assert_matches_type(BiometricStatus, biometric, path=["response"])

        assert cast(Any, response.is_closed) is True

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_method_verify(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        biometric = await async_client.users.me.biometrics.verify(
            biometric_signature="base64encoded_one_time_fingerprint_proof",
            biometric_type="fingerprint",
            device_id="dev_mobile_android_ddeeff",
        )
        assert_matches_type(BiometricVerifyResponse, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_raw_response_verify(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        response = await async_client.users.me.biometrics.with_raw_response.verify(
            biometric_signature="base64encoded_one_time_fingerprint_proof",
            biometric_type="fingerprint",
            device_id="dev_mobile_android_ddeeff",
        )

        assert response.is_closed is True
        assert response.http_request.headers.get("X-Stainless-Lang") == "python"
        biometric = await response.parse()
        assert_matches_type(BiometricVerifyResponse, biometric, path=["response"])

    @pytest.mark.skip(reason="Prism tests are disabled")
    @parametrize
    async def test_streaming_response_verify(self, async_client: AsyncJamesBurvelOcallaghanIii) -> None:
        async with async_client.users.me.biometrics.with_streaming_response.verify(
            biometric_signature="base64encoded_one_time_fingerprint_proof",
            biometric_type="fingerprint",
            device_id="dev_mobile_android_ddeeff",
        ) as response:
            assert not response.is_closed
            assert response.http_request.headers.get("X-Stainless-Lang") == "python"

            biometric = await response.parse()
            assert_matches_type(BiometricVerifyResponse, biometric, path=["response"])

        assert cast(Any, response.is_closed) is True
