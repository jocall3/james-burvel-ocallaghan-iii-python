# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import List, Union, Optional
from datetime import date
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
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
from ....types.corporate.compliance import audit_request_params
from ....types.corporate.compliance.audit_request_response import AuditRequestResponse
from ....types.corporate.compliance.audit_retrieve_report_response import AuditRetrieveReportResponse

__all__ = ["AuditsResource", "AsyncAuditsResource"]


class AuditsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AuditsResourceWithStreamingResponse(self)

    def request(
        self,
        *,
        audit_scope: Literal[
            "all_transactions", "corporate_cards", "international_payments", "user_onboarding", "specific_accounts"
        ],
        end_date: Union[str, date],
        regulatory_frameworks: List[Literal["AML", "KYC", "PCI-DSS", "GDPR", "CCPA", "SOX"]],
        start_date: Union[str, date],
        specific_account_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRequestResponse:
        """
        Initiates an AI-powered compliance audit for a specific period or scope,
        generating a comprehensive report detailing adherence to regulatory frameworks,
        internal policies, and flagging potential risks.

        Args:
          audit_scope: The scope of the compliance audit.

          end_date: End date for the audit period (inclusive).

          regulatory_frameworks: List of regulatory frameworks to audit against.

          start_date: Start date for the audit period (inclusive).

          specific_account_ids: Optional: List of specific account IDs to include if `auditScope` is
              'specific_accounts'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/corporate/compliance/audits",
            body=maybe_transform(
                {
                    "audit_scope": audit_scope,
                    "end_date": end_date,
                    "regulatory_frameworks": regulatory_frameworks,
                    "start_date": start_date,
                    "specific_account_ids": specific_account_ids,
                },
                audit_request_params.AuditRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRequestResponse,
        )

    def retrieve_report(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRetrieveReportResponse:
        """
        Retrieves the full report generated by an AI-driven compliance audit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        return self._get(
            f"/corporate/compliance/audits/{audit_id}/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRetrieveReportResponse,
        )


class AsyncAuditsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAuditsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAuditsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAuditsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncAuditsResourceWithStreamingResponse(self)

    async def request(
        self,
        *,
        audit_scope: Literal[
            "all_transactions", "corporate_cards", "international_payments", "user_onboarding", "specific_accounts"
        ],
        end_date: Union[str, date],
        regulatory_frameworks: List[Literal["AML", "KYC", "PCI-DSS", "GDPR", "CCPA", "SOX"]],
        start_date: Union[str, date],
        specific_account_ids: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRequestResponse:
        """
        Initiates an AI-powered compliance audit for a specific period or scope,
        generating a comprehensive report detailing adherence to regulatory frameworks,
        internal policies, and flagging potential risks.

        Args:
          audit_scope: The scope of the compliance audit.

          end_date: End date for the audit period (inclusive).

          regulatory_frameworks: List of regulatory frameworks to audit against.

          start_date: Start date for the audit period (inclusive).

          specific_account_ids: Optional: List of specific account IDs to include if `auditScope` is
              'specific_accounts'.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/corporate/compliance/audits",
            body=await async_maybe_transform(
                {
                    "audit_scope": audit_scope,
                    "end_date": end_date,
                    "regulatory_frameworks": regulatory_frameworks,
                    "start_date": start_date,
                    "specific_account_ids": specific_account_ids,
                },
                audit_request_params.AuditRequestParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRequestResponse,
        )

    async def retrieve_report(
        self,
        audit_id: str,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AuditRetrieveReportResponse:
        """
        Retrieves the full report generated by an AI-driven compliance audit.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not audit_id:
            raise ValueError(f"Expected a non-empty value for `audit_id` but received {audit_id!r}")
        return await self._get(
            f"/corporate/compliance/audits/{audit_id}/report",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AuditRetrieveReportResponse,
        )


class AuditsResourceWithRawResponse:
    def __init__(self, audits: AuditsResource) -> None:
        self._audits = audits

        self.request = to_raw_response_wrapper(
            audits.request,
        )
        self.retrieve_report = to_raw_response_wrapper(
            audits.retrieve_report,
        )


class AsyncAuditsResourceWithRawResponse:
    def __init__(self, audits: AsyncAuditsResource) -> None:
        self._audits = audits

        self.request = async_to_raw_response_wrapper(
            audits.request,
        )
        self.retrieve_report = async_to_raw_response_wrapper(
            audits.retrieve_report,
        )


class AuditsResourceWithStreamingResponse:
    def __init__(self, audits: AuditsResource) -> None:
        self._audits = audits

        self.request = to_streamed_response_wrapper(
            audits.request,
        )
        self.retrieve_report = to_streamed_response_wrapper(
            audits.retrieve_report,
        )


class AsyncAuditsResourceWithStreamingResponse:
    def __init__(self, audits: AsyncAuditsResource) -> None:
        self._audits = audits

        self.request = async_to_streamed_response_wrapper(
            audits.request,
        )
        self.retrieve_report = async_to_streamed_response_wrapper(
            audits.retrieve_report,
        )
