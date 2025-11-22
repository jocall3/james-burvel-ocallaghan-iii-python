# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NoneType, NotGiven, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.users.me import device_register_params
from ....types.users.me.device import Device
from ....types.users.me.device_list_response import DeviceListResponse

__all__ = ["DevicesResource", "AsyncDevicesResource"]


class DevicesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> DevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return DevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> DevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return DevicesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceListResponse:
        """
        Retrieves a list of all devices linked to the user's account, including mobile
        phones, tablets, and desktops, indicating their last active status and security
        posture.
        """
        return self._get(
            "/users/me/devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceListResponse,
        )

    def deregister(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a specific device from the user's linked devices, revoking its access
        and requiring re-registration for future use. Useful for lost or compromised
        devices.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return self._delete(
            f"/users/me/devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    def register(
        self,
        *,
        device_type: Literal["mobile", "desktop", "tablet", "smart_watch"],
        model: str,
        os: str,
        biometric_signature: Optional[str] | Omit = omit,
        device_name: Optional[str] | Omit = omit,
        push_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Registers a new device for secure access and multi-factor authentication,
        associating it with the user's profile. This typically initiates a biometric or
        MFA enrollment flow.

        Args:
          device_type: Type of device being registered.

          model: Model of the device.

          os: Operating system and version of the device.

          biometric_signature: Base64 encoded biometric signature for initial enrollment (if applicable).

          device_name: User-defined name for the device.

          push_token: Push notification token for the device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/users/me/devices",
            body=maybe_transform(
                {
                    "device_type": device_type,
                    "model": model,
                    "os": os,
                    "biometric_signature": biometric_signature,
                    "device_name": device_name,
                    "push_token": push_token,
                },
                device_register_params.DeviceRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )


class AsyncDevicesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncDevicesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncDevicesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncDevicesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/stainless-sdks/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncDevicesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> DeviceListResponse:
        """
        Retrieves a list of all devices linked to the user's account, including mobile
        phones, tablets, and desktops, indicating their last active status and security
        posture.
        """
        return await self._get(
            "/users/me/devices",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=DeviceListResponse,
        )

    async def deregister(
        self,
        device_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> None:
        """
        Removes a specific device from the user's linked devices, revoking its access
        and requiring re-registration for future use. Useful for lost or compromised
        devices.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not device_id:
            raise ValueError(f"Expected a non-empty value for `device_id` but received {device_id!r}")
        extra_headers = {"Accept": "*/*", **(extra_headers or {})}
        return await self._delete(
            f"/users/me/devices/{device_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=NoneType,
        )

    async def register(
        self,
        *,
        device_type: Literal["mobile", "desktop", "tablet", "smart_watch"],
        model: str,
        os: str,
        biometric_signature: Optional[str] | Omit = omit,
        device_name: Optional[str] | Omit = omit,
        push_token: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> Device:
        """
        Registers a new device for secure access and multi-factor authentication,
        associating it with the user's profile. This typically initiates a biometric or
        MFA enrollment flow.

        Args:
          device_type: Type of device being registered.

          model: Model of the device.

          os: Operating system and version of the device.

          biometric_signature: Base64 encoded biometric signature for initial enrollment (if applicable).

          device_name: User-defined name for the device.

          push_token: Push notification token for the device.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/users/me/devices",
            body=await async_maybe_transform(
                {
                    "device_type": device_type,
                    "model": model,
                    "os": os,
                    "biometric_signature": biometric_signature,
                    "device_name": device_name,
                    "push_token": push_token,
                },
                device_register_params.DeviceRegisterParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=Device,
        )


class DevicesResourceWithRawResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_raw_response_wrapper(
            devices.list,
        )
        self.deregister = to_raw_response_wrapper(
            devices.deregister,
        )
        self.register = to_raw_response_wrapper(
            devices.register,
        )


class AsyncDevicesResourceWithRawResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_raw_response_wrapper(
            devices.list,
        )
        self.deregister = async_to_raw_response_wrapper(
            devices.deregister,
        )
        self.register = async_to_raw_response_wrapper(
            devices.register,
        )


class DevicesResourceWithStreamingResponse:
    def __init__(self, devices: DevicesResource) -> None:
        self._devices = devices

        self.list = to_streamed_response_wrapper(
            devices.list,
        )
        self.deregister = to_streamed_response_wrapper(
            devices.deregister,
        )
        self.register = to_streamed_response_wrapper(
            devices.register,
        )


class AsyncDevicesResourceWithStreamingResponse:
    def __init__(self, devices: AsyncDevicesResource) -> None:
        self._devices = devices

        self.list = async_to_streamed_response_wrapper(
            devices.list,
        )
        self.deregister = async_to_streamed_response_wrapper(
            devices.deregister,
        )
        self.register = async_to_streamed_response_wrapper(
            devices.register,
        )
