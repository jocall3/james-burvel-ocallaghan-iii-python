# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
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
from ...types.investments import (
    portfolio_list_params,
    portfolio_create_params,
    portfolio_update_params,
    portfolio_rebalance_params,
)
from ...types.investments.investment_portfolio import InvestmentPortfolio
from ...types.investments.portfolio_list_response import PortfolioListResponse
from ...types.investments.portfolio_rebalance_response import PortfolioRebalanceResponse

__all__ = ["PortfoliosResource", "AsyncPortfoliosResource"]


class PortfoliosResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> PortfoliosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return PortfoliosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> PortfoliosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return PortfoliosResourceWithStreamingResponse(self)

    def create(
        self,
        *,
        currency: object,
        initial_investment: object,
        name: object,
        risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"],
        type: Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"],
        ai_auto_allocate: object | Omit = omit,
        linked_account_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestmentPortfolio:
        """
        Creates a new investment portfolio, with options for initial asset allocation.

        Args:
          currency: ISO 4217 currency code of the portfolio.

          initial_investment: Initial amount to invest into the portfolio.

          name: Name for the new investment portfolio.

          risk_tolerance: Desired risk tolerance for this portfolio.

          type: General type or strategy of the portfolio.

          ai_auto_allocate: If true, AI will automatically allocate initial investment based on risk
              tolerance.

          linked_account_id: Optional: ID of a linked account to fund the initial investment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/investments/portfolios",
            body=maybe_transform(
                {
                    "currency": currency,
                    "initial_investment": initial_investment,
                    "name": name,
                    "risk_tolerance": risk_tolerance,
                    "type": type,
                    "ai_auto_allocate": ai_auto_allocate,
                    "linked_account_id": linked_account_id,
                },
                portfolio_create_params.PortfolioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    def retrieve(
        self,
        portfolio_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestmentPortfolio:
        """
        Retrieves detailed information for a specific investment portfolio, including
        holdings, performance, and AI insights.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            f"/investments/portfolios/{portfolio_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    def update(
        self,
        portfolio_id: object,
        *,
        ai_rebalancing_frequency: Optional[Literal["monthly", "quarterly", "semi_annually", "annually", "never"]]
        | Omit = omit,
        name: object | Omit = omit,
        risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestmentPortfolio:
        """
        Updates high-level details of an investment portfolio, such as name or risk
        tolerance.

        Args:
          ai_rebalancing_frequency: Updated frequency for AI-driven rebalancing.

          name: Updated name of the portfolio.

          risk_tolerance: Updated risk tolerance for this portfolio. May trigger rebalancing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._put(
            f"/investments/portfolios/{portfolio_id}",
            body=maybe_transform(
                {
                    "ai_rebalancing_frequency": ai_rebalancing_frequency,
                    "name": name,
                    "risk_tolerance": risk_tolerance,
                },
                portfolio_update_params.PortfolioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    def list(
        self,
        *,
        limit: object | Omit = omit,
        offset: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListResponse:
        """
        Retrieves a summary of all investment portfolios linked to the user's account.

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._get(
            "/investments/portfolios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    portfolio_list_params.PortfolioListParams,
                ),
            ),
            cast_to=PortfolioListResponse,
        )

    def rebalance(
        self,
        portfolio_id: object,
        *,
        target_risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"],
        confirmation_required: object | Omit = omit,
        dry_run: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioRebalanceResponse:
        """
        Triggers an AI-driven rebalancing process for a specific investment portfolio
        based on a target risk tolerance or strategy.

        Args:
          target_risk_tolerance: The desired risk tolerance for rebalancing the portfolio.

          confirmation_required: If true, user confirmation is required before executing actual trades after a
              dry run.

          dry_run: If true, only simulate the rebalance without executing trades. Returns proposed
              trades.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            f"/investments/portfolios/{portfolio_id}/rebalance",
            body=maybe_transform(
                {
                    "target_risk_tolerance": target_risk_tolerance,
                    "confirmation_required": confirmation_required,
                    "dry_run": dry_run,
                },
                portfolio_rebalance_params.PortfolioRebalanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioRebalanceResponse,
        )


class AsyncPortfoliosResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncPortfoliosResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncPortfoliosResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncPortfoliosResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncPortfoliosResourceWithStreamingResponse(self)

    async def create(
        self,
        *,
        currency: object,
        initial_investment: object,
        name: object,
        risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"],
        type: Literal["equities", "bonds", "diversified", "crypto", "retirement", "other"],
        ai_auto_allocate: object | Omit = omit,
        linked_account_id: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestmentPortfolio:
        """
        Creates a new investment portfolio, with options for initial asset allocation.

        Args:
          currency: ISO 4217 currency code of the portfolio.

          initial_investment: Initial amount to invest into the portfolio.

          name: Name for the new investment portfolio.

          risk_tolerance: Desired risk tolerance for this portfolio.

          type: General type or strategy of the portfolio.

          ai_auto_allocate: If true, AI will automatically allocate initial investment based on risk
              tolerance.

          linked_account_id: Optional: ID of a linked account to fund the initial investment.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/investments/portfolios",
            body=await async_maybe_transform(
                {
                    "currency": currency,
                    "initial_investment": initial_investment,
                    "name": name,
                    "risk_tolerance": risk_tolerance,
                    "type": type,
                    "ai_auto_allocate": ai_auto_allocate,
                    "linked_account_id": linked_account_id,
                },
                portfolio_create_params.PortfolioCreateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    async def retrieve(
        self,
        portfolio_id: object,
        *,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestmentPortfolio:
        """
        Retrieves detailed information for a specific investment portfolio, including
        holdings, performance, and AI insights.

        Args:
          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            f"/investments/portfolios/{portfolio_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    async def update(
        self,
        portfolio_id: object,
        *,
        ai_rebalancing_frequency: Optional[Literal["monthly", "quarterly", "semi_annually", "annually", "never"]]
        | Omit = omit,
        name: object | Omit = omit,
        risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> InvestmentPortfolio:
        """
        Updates high-level details of an investment portfolio, such as name or risk
        tolerance.

        Args:
          ai_rebalancing_frequency: Updated frequency for AI-driven rebalancing.

          name: Updated name of the portfolio.

          risk_tolerance: Updated risk tolerance for this portfolio. May trigger rebalancing.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._put(
            f"/investments/portfolios/{portfolio_id}",
            body=await async_maybe_transform(
                {
                    "ai_rebalancing_frequency": ai_rebalancing_frequency,
                    "name": name,
                    "risk_tolerance": risk_tolerance,
                },
                portfolio_update_params.PortfolioUpdateParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    async def list(
        self,
        *,
        limit: object | Omit = omit,
        offset: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListResponse:
        """
        Retrieves a summary of all investment portfolios linked to the user's account.

        Args:
          limit: Maximum number of items to return in a single page.

          offset: Number of items to skip before starting to collect the result set.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._get(
            "/investments/portfolios",
            options=make_request_options(
                extra_headers=extra_headers,
                extra_query=extra_query,
                extra_body=extra_body,
                timeout=timeout,
                query=await async_maybe_transform(
                    {
                        "limit": limit,
                        "offset": offset,
                    },
                    portfolio_list_params.PortfolioListParams,
                ),
            ),
            cast_to=PortfolioListResponse,
        )

    async def rebalance(
        self,
        portfolio_id: object,
        *,
        target_risk_tolerance: Literal["conservative", "moderate", "aggressive", "very_aggressive"],
        confirmation_required: object | Omit = omit,
        dry_run: object | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioRebalanceResponse:
        """
        Triggers an AI-driven rebalancing process for a specific investment portfolio
        based on a target risk tolerance or strategy.

        Args:
          target_risk_tolerance: The desired risk tolerance for rebalancing the portfolio.

          confirmation_required: If true, user confirmation is required before executing actual trades after a
              dry run.

          dry_run: If true, only simulate the rebalance without executing trades. Returns proposed
              trades.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            f"/investments/portfolios/{portfolio_id}/rebalance",
            body=await async_maybe_transform(
                {
                    "target_risk_tolerance": target_risk_tolerance,
                    "confirmation_required": confirmation_required,
                    "dry_run": dry_run,
                },
                portfolio_rebalance_params.PortfolioRebalanceParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioRebalanceResponse,
        )


class PortfoliosResourceWithRawResponse:
    def __init__(self, portfolios: PortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = to_raw_response_wrapper(
            portfolios.create,
        )
        self.retrieve = to_raw_response_wrapper(
            portfolios.retrieve,
        )
        self.update = to_raw_response_wrapper(
            portfolios.update,
        )
        self.list = to_raw_response_wrapper(
            portfolios.list,
        )
        self.rebalance = to_raw_response_wrapper(
            portfolios.rebalance,
        )


class AsyncPortfoliosResourceWithRawResponse:
    def __init__(self, portfolios: AsyncPortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = async_to_raw_response_wrapper(
            portfolios.create,
        )
        self.retrieve = async_to_raw_response_wrapper(
            portfolios.retrieve,
        )
        self.update = async_to_raw_response_wrapper(
            portfolios.update,
        )
        self.list = async_to_raw_response_wrapper(
            portfolios.list,
        )
        self.rebalance = async_to_raw_response_wrapper(
            portfolios.rebalance,
        )


class PortfoliosResourceWithStreamingResponse:
    def __init__(self, portfolios: PortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = to_streamed_response_wrapper(
            portfolios.create,
        )
        self.retrieve = to_streamed_response_wrapper(
            portfolios.retrieve,
        )
        self.update = to_streamed_response_wrapper(
            portfolios.update,
        )
        self.list = to_streamed_response_wrapper(
            portfolios.list,
        )
        self.rebalance = to_streamed_response_wrapper(
            portfolios.rebalance,
        )


class AsyncPortfoliosResourceWithStreamingResponse:
    def __init__(self, portfolios: AsyncPortfoliosResource) -> None:
        self._portfolios = portfolios

        self.create = async_to_streamed_response_wrapper(
            portfolios.create,
        )
        self.retrieve = async_to_streamed_response_wrapper(
            portfolios.retrieve,
        )
        self.update = async_to_streamed_response_wrapper(
            portfolios.update,
        )
        self.list = async_to_streamed_response_wrapper(
            portfolios.list,
        )
        self.rebalance = async_to_streamed_response_wrapper(
            portfolios.rebalance,
        )
