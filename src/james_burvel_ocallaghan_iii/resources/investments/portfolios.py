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
from ...types.investments import portfolio_create_params, portfolio_update_params, portfolio_rebalance_params
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
        currency: str,
        initial_investment: float,
        name: str,
        risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"],
        type: Literal["equities", "bonds", "diversified", "retirement", "crypto", "custom"],
        ai_auto_allocate: bool | Omit = omit,
        linked_account_id: Optional[str] | Omit = omit,
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
          currency: The base currency of the portfolio.

          initial_investment: Initial amount to invest in this portfolio.

          name: Name for the new investment portfolio.

          risk_tolerance: Desired risk tolerance for this portfolio.

          type: Type or strategy of the investment portfolio.

          ai_auto_allocate: If true, AI will automatically suggest and allocate assets based on risk
              tolerance.

          linked_account_id: Optional: The ID of a linked bank account to draw initial investment from.

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
        portfolio_id: str,
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
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        return self._get(
            f"/investments/portfolios/{portfolio_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    def update(
        self,
        portfolio_id: str,
        *,
        ai_rebalancing_frequency: Literal["never", "monthly", "quarterly", "annually"] | Omit = omit,
        name: str | Omit = omit,
        risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"] | Omit = omit,
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

          risk_tolerance: Updated risk tolerance for this portfolio.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListResponse:
        """Retrieves a summary of all investment portfolios linked to the user's account."""
        return self._get(
            "/investments/portfolios",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioListResponse,
        )

    def rebalance(
        self,
        portfolio_id: str,
        *,
        target_risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"],
        confirmation_required: bool | Omit = omit,
        dry_run: bool | Omit = omit,
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
          target_risk_tolerance: The desired risk tolerance for the portfolio after rebalancing.

          confirmation_required: If true, explicit user confirmation is required before trades are executed.

          dry_run: If true, the AI will only propose trades without executing them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
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
        currency: str,
        initial_investment: float,
        name: str,
        risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"],
        type: Literal["equities", "bonds", "diversified", "retirement", "crypto", "custom"],
        ai_auto_allocate: bool | Omit = omit,
        linked_account_id: Optional[str] | Omit = omit,
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
          currency: The base currency of the portfolio.

          initial_investment: Initial amount to invest in this portfolio.

          name: Name for the new investment portfolio.

          risk_tolerance: Desired risk tolerance for this portfolio.

          type: Type or strategy of the investment portfolio.

          ai_auto_allocate: If true, AI will automatically suggest and allocate assets based on risk
              tolerance.

          linked_account_id: Optional: The ID of a linked bank account to draw initial investment from.

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
        portfolio_id: str,
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
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
        return await self._get(
            f"/investments/portfolios/{portfolio_id}",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=InvestmentPortfolio,
        )

    async def update(
        self,
        portfolio_id: str,
        *,
        ai_rebalancing_frequency: Literal["never", "monthly", "quarterly", "annually"] | Omit = omit,
        name: str | Omit = omit,
        risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"] | Omit = omit,
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

          risk_tolerance: Updated risk tolerance for this portfolio.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
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
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> PortfolioListResponse:
        """Retrieves a summary of all investment portfolios linked to the user's account."""
        return await self._get(
            "/investments/portfolios",
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=PortfolioListResponse,
        )

    async def rebalance(
        self,
        portfolio_id: str,
        *,
        target_risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"],
        confirmation_required: bool | Omit = omit,
        dry_run: bool | Omit = omit,
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
          target_risk_tolerance: The desired risk tolerance for the portfolio after rebalancing.

          confirmation_required: If true, explicit user confirmation is required before trades are executed.

          dry_run: If true, the AI will only propose trades without executing them.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        if not portfolio_id:
            raise ValueError(f"Expected a non-empty value for `portfolio_id` but received {portfolio_id!r}")
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
