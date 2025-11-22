# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, Base64FileInput, omit, not_given
from ..._utils import maybe_transform, async_maybe_transform
from ..._compat import cached_property
from ..._resource import SyncAPIResource, AsyncAPIResource
from ..._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ..._base_client import make_request_options
from ...types.identity import kyc_submit_params
from ...types.identity.kyc_status import KYCStatus

__all__ = ["KYCResource", "AsyncKYCResource"]


class KYCResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> KYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return KYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> KYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return KYCResourceWithStreamingResponse(self)

    def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatus:
        """
        Retrieves the current status of the user's Know Your Customer (KYC) verification
        process.
        """
        return self._get(
            "/identity/kyc/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatus,
        )

    def submit(
        self,
        *,
        country_of_issue: str,
        document_front_image: Union[str, Base64FileInput],
        document_number: str,
        document_type: Literal["drivers_license", "passport", "national_id", "utility_bill", "bank_statement"],
        expiration_date: Union[str, date],
        issue_date: Union[str, date],
        address_proof_image: Union[str, Base64FileInput, None] | Omit = omit,
        document_back_image: Union[str, Base64FileInput, None] | Omit = omit,
        live_selfie_image: Union[str, Base64FileInput, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatus:
        """
        Submits Know Your Customer (KYC) documentation, such as identity proofs and
        address verification, for AI-accelerated compliance and identity verification,
        crucial for higher service tiers and regulatory adherence.

        Args:
          country_of_issue: The country that issued the document (ISO 3166-1 alpha-2 code).

          document_front_image: Base64 encoded image of the front side of the document.

          document_number: The official document number.

          document_type: Type of KYC document being submitted.

          expiration_date: Date the document expires.

          issue_date: Date the document was issued.

          address_proof_image: Base64 encoded image of an address proof (e.g., utility bill).

          document_back_image: Base64 encoded image of the back side of the document (if applicable).

          live_selfie_image: Base64 encoded image of a live selfie for liveness detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/identity/kyc/submit",
            body=maybe_transform(
                {
                    "country_of_issue": country_of_issue,
                    "document_front_image": document_front_image,
                    "document_number": document_number,
                    "document_type": document_type,
                    "expiration_date": expiration_date,
                    "issue_date": issue_date,
                    "address_proof_image": address_proof_image,
                    "document_back_image": document_back_image,
                    "live_selfie_image": live_selfie_image,
                },
                kyc_submit_params.KYCSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatus,
        )


class AsyncKYCResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncKYCResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncKYCResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncKYCResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncKYCResourceWithStreamingResponse(self)

    async def retrieve_status(
        self,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatus:
        """
        Retrieves the current status of the user's Know Your Customer (KYC) verification
        process.
        """
        return await self._get(
            "/identity/kyc/status",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatus,
        )

    async def submit(
        self,
        *,
        country_of_issue: str,
        document_front_image: Union[str, Base64FileInput],
        document_number: str,
        document_type: Literal["drivers_license", "passport", "national_id", "utility_bill", "bank_statement"],
        expiration_date: Union[str, date],
        issue_date: Union[str, date],
        address_proof_image: Union[str, Base64FileInput, None] | Omit = omit,
        document_back_image: Union[str, Base64FileInput, None] | Omit = omit,
        live_selfie_image: Union[str, Base64FileInput, None] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> KYCStatus:
        """
        Submits Know Your Customer (KYC) documentation, such as identity proofs and
        address verification, for AI-accelerated compliance and identity verification,
        crucial for higher service tiers and regulatory adherence.

        Args:
          country_of_issue: The country that issued the document (ISO 3166-1 alpha-2 code).

          document_front_image: Base64 encoded image of the front side of the document.

          document_number: The official document number.

          document_type: Type of KYC document being submitted.

          expiration_date: Date the document expires.

          issue_date: Date the document was issued.

          address_proof_image: Base64 encoded image of an address proof (e.g., utility bill).

          document_back_image: Base64 encoded image of the back side of the document (if applicable).

          live_selfie_image: Base64 encoded image of a live selfie for liveness detection.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/identity/kyc/submit",
            body=await async_maybe_transform(
                {
                    "country_of_issue": country_of_issue,
                    "document_front_image": document_front_image,
                    "document_number": document_number,
                    "document_type": document_type,
                    "expiration_date": expiration_date,
                    "issue_date": issue_date,
                    "address_proof_image": address_proof_image,
                    "document_back_image": document_back_image,
                    "live_selfie_image": live_selfie_image,
                },
                kyc_submit_params.KYCSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=KYCStatus,
        )


class KYCResourceWithRawResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.retrieve_status = to_raw_response_wrapper(
            kyc.retrieve_status,
        )
        self.submit = to_raw_response_wrapper(
            kyc.submit,
        )


class AsyncKYCResourceWithRawResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.retrieve_status = async_to_raw_response_wrapper(
            kyc.retrieve_status,
        )
        self.submit = async_to_raw_response_wrapper(
            kyc.submit,
        )


class KYCResourceWithStreamingResponse:
    def __init__(self, kyc: KYCResource) -> None:
        self._kyc = kyc

        self.retrieve_status = to_streamed_response_wrapper(
            kyc.retrieve_status,
        )
        self.submit = to_streamed_response_wrapper(
            kyc.submit,
        )


class AsyncKYCResourceWithStreamingResponse:
    def __init__(self, kyc: AsyncKYCResource) -> None:
        self._kyc = kyc

        self.retrieve_status = async_to_streamed_response_wrapper(
            kyc.retrieve_status,
        )
        self.submit = async_to_streamed_response_wrapper(
            kyc.submit,
        )
