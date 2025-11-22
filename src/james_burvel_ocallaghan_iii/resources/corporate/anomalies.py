# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
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
from ...types.corporate import anomaly_list_params, anomaly_update_status_params
from ...types.corporate.financial_anomaly import FinancialAnomaly
from ...types.corporate.anomaly_list_response import AnomalyListResponse

__all__ = ["AnomaliesResource", "AsyncAnomaliesResource"]


class AnomaliesResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AnomaliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AnomaliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AnomaliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AnomaliesResourceWithStreamingResponse(self)

    def list(
        self,
        *,
        end_date: Union[str, date] | Omit = omit,
        entity_type: Literal["PaymentOrder", "Transaction", "Counterparty", "CorporateCard", "Invoice"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        severity: Literal["Low", "Medium", "High", "Critical"] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        status: Literal["New", "Under Review", "Escalated", "Dismissed", "Resolved"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnomalyListResponse:
        """
        Retrieves a comprehensive list of AI-detected financial anomalies across
        transactions, payments, and corporate cards that require immediate review and
        potential action to mitigate risk and ensure compliance.

        Args:
          end_date: Filter results up to this date (inclusive, YYYY-MM-DD).

          entity_type: Filter anomalies by the type of financial entity they are related to.

          limit: Maximum number of items to return.

          offset: Number of items to skip before starting to collect the result set.

          severity: Filter anomalies by their AI-assessed severity level.

          start_date: Filter results from this date (inclusive, YYYY-MM-DD).

          status: Filter anomalies by their current review status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/corporate/anomalies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "end_date": end_date,
                        "entity_type": entity_type,
                        "limit": limit,
                        "offset": offset,
                        "severity": severity,
                        "start_date": start_date,
                        "status": status,
                    },
                    anomaly_list_params.AnomalyListParams,
                ),
            ),
            cast_to=AnomalyListResponse,
        )

    def update_status(
        self,
        anomaly_id: str,
        *,
        status: Literal["Dismissed", "Resolved", "Under Review", "Escalated"],
        resolution_notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialAnomaly:
        """
        Updates the review status of a specific financial anomaly, allowing compliance
        officers to mark it as dismissed, resolved, or escalate for further
        investigation after thorough AI-assisted and human review.

        Args:
          status: The new status for the financial anomaly.

          resolution_notes: Optional notes regarding the resolution or dismissal of the anomaly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not anomaly_id:
            raise ValueError(f"Expected a non-empty value for `anomaly_id` but received {anomaly_id!r}")
        return self._put(
            f"/corporate/anomalies/{anomaly_id}/status",
            body=maybe_transform(
                {
                    "status": status,
                    "resolution_notes": resolution_notes,
                },
                anomaly_update_status_params.AnomalyUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAnomaly,
        )


class AsyncAnomaliesResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncAnomaliesResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncAnomaliesResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncAnomaliesResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncAnomaliesResourceWithStreamingResponse(self)

    async def list(
        self,
        *,
        end_date: Union[str, date] | Omit = omit,
        entity_type: Literal["PaymentOrder", "Transaction", "Counterparty", "CorporateCard", "Invoice"] | Omit = omit,
        limit: int | Omit = omit,
        offset: int | Omit = omit,
        severity: Literal["Low", "Medium", "High", "Critical"] | Omit = omit,
        start_date: Union[str, date] | Omit = omit,
        status: Literal["New", "Under Review", "Escalated", "Dismissed", "Resolved"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AnomalyListResponse:
        """
        Retrieves a comprehensive list of AI-detected financial anomalies across
        transactions, payments, and corporate cards that require immediate review and
        potential action to mitigate risk and ensure compliance.

        Args:
          end_date: Filter results up to this date (inclusive, YYYY-MM-DD).

          entity_type: Filter anomalies by the type of financial entity they are related to.

          limit: Maximum number of items to return.

          offset: Number of items to skip before starting to collect the result set.

          severity: Filter anomalies by their AI-assessed severity level.

          start_date: Filter results from this date (inclusive, YYYY-MM-DD).

          status: Filter anomalies by their current review status.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/corporate/anomalies",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "end_date": end_date,
                        "entity_type": entity_type,
                        "limit": limit,
                        "offset": offset,
                        "severity": severity,
                        "start_date": start_date,
                        "status": status,
                    },
                    anomaly_list_params.AnomalyListParams,
                ),
            ),
            cast_to=AnomalyListResponse,
        )

    async def update_status(
        self,
        anomaly_id: str,
        *,
        status: Literal["Dismissed", "Resolved", "Under Review", "Escalated"],
        resolution_notes: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> FinancialAnomaly:
        """
        Updates the review status of a specific financial anomaly, allowing compliance
        officers to mark it as dismissed, resolved, or escalate for further
        investigation after thorough AI-assisted and human review.

        Args:
          status: The new status for the financial anomaly.

          resolution_notes: Optional notes regarding the resolution or dismissal of the anomaly.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not anomaly_id:
            raise ValueError(f"Expected a non-empty value for `anomaly_id` but received {anomaly_id!r}")
        return await self._put(
            f"/corporate/anomalies/{anomaly_id}/status",
            body=await async_maybe_transform(
                {
                    "status": status,
                    "resolution_notes": resolution_notes,
                },
                anomaly_update_status_params.AnomalyUpdateStatusParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=FinancialAnomaly,
        )


class AnomaliesResourceWithRawResponse:
    def __init__(self, anomalies: AnomaliesResource) -> None:
        self._anomalies = anomalies

        self.list = to_raw_response_wrapper(
            anomalies.list,
        )
        self.update_status = to_raw_response_wrapper(
            anomalies.update_status,
        )


class AsyncAnomaliesResourceWithRawResponse:
    def __init__(self, anomalies: AsyncAnomaliesResource) -> None:
        self._anomalies = anomalies

        self.list = async_to_raw_response_wrapper(
            anomalies.list,
        )
        self.update_status = async_to_raw_response_wrapper(
            anomalies.update_status,
        )


class AnomaliesResourceWithStreamingResponse:
    def __init__(self, anomalies: AnomaliesResource) -> None:
        self._anomalies = anomalies

        self.list = to_streamed_response_wrapper(
            anomalies.list,
        )
        self.update_status = to_streamed_response_wrapper(
            anomalies.update_status,
        )


class AsyncAnomaliesResourceWithStreamingResponse:
    def __init__(self, anomalies: AsyncAnomaliesResource) -> None:
        self._anomalies = anomalies

        self.list = async_to_streamed_response_wrapper(
            anomalies.list,
        )
        self.update_status = async_to_streamed_response_wrapper(
            anomalies.update_status,
        )
