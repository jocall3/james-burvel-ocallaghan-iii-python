# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal

import httpx

from ..._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ...types.lending import application_submit_params
from ...types.lending.loan_application_status import LoanApplicationStatus

__all__ = ["ApplicationsResource", "AsyncApplicationsResource"]


class ApplicationsResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> ApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return ApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> ApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return ApplicationsResourceWithStreamingResponse(self)

    def retrieve(
        self,
        application_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoanApplicationStatus:
        """
        Retrieves the current status and detailed information for a submitted loan
        application, including AI underwriting outcomes, approved terms, and next steps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/lending/applications/{application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanApplicationStatus,
        )

    def submit(
        self,
        *,
        loan_amount: object,
        loan_purpose: Literal[
            "home_improvement", "debt_consolidation", "medical_expense", "education", "auto_purchase", "other"
        ],
        repayment_term_months: object,
        additional_notes: object | Omit = omit,
        co_applicant: application_submit_params.CoApplicant | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoanApplicationStatus:
        """
        Submits a new loan application, which is instantly processed and underwritten by
        our Quantum AI, providing rapid decisions and personalized loan offers based on
        real-time financial health data.

        Args:
          loan_amount: The desired loan amount.

          loan_purpose: The purpose of the loan.

          repayment_term_months: The desired repayment term in months.

          additional_notes: Optional notes or details for the application.

          co_applicant: Optional: Details of a co-applicant for the loan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/lending/applications",
            body=maybe_transform(
                {
                    "loan_amount": loan_amount,
                    "loan_purpose": loan_purpose,
                    "repayment_term_months": repayment_term_months,
                    "additional_notes": additional_notes,
                    "co_applicant": co_applicant,
                },
                application_submit_params.ApplicationSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanApplicationStatus,
        )


class AsyncApplicationsResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncApplicationsResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncApplicationsResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncApplicationsResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncApplicationsResourceWithStreamingResponse(self)

    async def retrieve(
        self,
        application_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoanApplicationStatus:
        """
        Retrieves the current status and detailed information for a submitted loan
        application, including AI underwriting outcomes, approved terms, and next steps.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/lending/applications/{application_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanApplicationStatus,
        )

    async def submit(
        self,
        *,
        loan_amount: object,
        loan_purpose: Literal[
            "home_improvement", "debt_consolidation", "medical_expense", "education", "auto_purchase", "other"
        ],
        repayment_term_months: object,
        additional_notes: object | Omit = omit,
        co_applicant: application_submit_params.CoApplicant | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> LoanApplicationStatus:
        """
        Submits a new loan application, which is instantly processed and underwritten by
        our Quantum AI, providing rapid decisions and personalized loan offers based on
        real-time financial health data.

        Args:
          loan_amount: The desired loan amount.

          loan_purpose: The purpose of the loan.

          repayment_term_months: The desired repayment term in months.

          additional_notes: Optional notes or details for the application.

          co_applicant: Optional: Details of a co-applicant for the loan.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/lending/applications",
            body=await async_maybe_transform(
                {
                    "loan_amount": loan_amount,
                    "loan_purpose": loan_purpose,
                    "repayment_term_months": repayment_term_months,
                    "additional_notes": additional_notes,
                    "co_applicant": co_applicant,
                },
                application_submit_params.ApplicationSubmitParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=LoanApplicationStatus,
        )


class ApplicationsResourceWithRawResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = to_raw_response_wrapper(
            applications.retrieve,
        )
        self.submit = to_raw_response_wrapper(
            applications.submit,
        )


class AsyncApplicationsResourceWithRawResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = async_to_raw_response_wrapper(
            applications.retrieve,
        )
        self.submit = async_to_raw_response_wrapper(
            applications.submit,
        )


class ApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: ApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = to_streamed_response_wrapper(
            applications.retrieve,
        )
        self.submit = to_streamed_response_wrapper(
            applications.submit,
        )


class AsyncApplicationsResourceWithStreamingResponse:
    def __init__(self, applications: AsyncApplicationsResource) -> None:
        self._applications = applications

        self.retrieve = async_to_streamed_response_wrapper(
            applications.retrieve,
        )
        self.submit = async_to_streamed_response_wrapper(
            applications.submit,
        )
