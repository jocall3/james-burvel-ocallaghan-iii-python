# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
from ....types.ai.oracle import simulate_run_advanced_params, simulate_run_standard_params
from ....types.ai.oracle.simulation_response import SimulationResponse
from ....types.ai.oracle.advanced_simulation_response import AdvancedSimulationResponse

__all__ = ["SimulateResource", "AsyncSimulateResource"]


class SimulateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> SimulateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return SimulateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> SimulateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return SimulateResourceWithStreamingResponse(self)

    def run_advanced(
        self,
        *,
        prompt: str,
        scenarios: Iterable[simulate_run_advanced_params.Scenario],
        duration_years: int | Omit = omit,
        initial_state: Optional[simulate_run_advanced_params.InitialState] | Omit = omit,
        sensitivity_analysis_params: Optional[Iterable[simulate_run_advanced_params.SensitivityAnalysisParam]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedSimulationResponse:
        """
        Engages the Quantum Oracle for highly complex, multi-variable simulations,
        allowing precise control over numerous financial parameters, market conditions,
        and personal events to generate deep, predictive insights and sensitivity
        analysis.

        Args:
          prompt: Natural language description of the complex simulation goal.

          scenarios: A list of distinct hypothetical scenarios to run.

          duration_years: Overall duration of the simulation in years.

          initial_state: Optional: Override current user financial data for the simulation's starting
              point.

          sensitivity_analysis_params: Parameters to vary for sensitivity analysis within scenarios.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/oracle/simulate/advanced",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "scenarios": scenarios,
                    "duration_years": duration_years,
                    "initial_state": initial_state,
                    "sensitivity_analysis_params": sensitivity_analysis_params,
                },
                simulate_run_advanced_params.SimulateRunAdvancedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedSimulationResponse,
        )

    def run_standard(
        self,
        *,
        prompt: str,
        parameters: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationResponse:
        """
        Submits a hypothetical scenario to the Quantum Oracle AI for standard financial
        impact analysis. The AI simulates the effect on the user's current financial
        state and provides a summary.

        Args:
          prompt: Natural language description of the financial scenario to simulate.

          parameters: Optional: Structured parameters to guide the AI simulation (e.g., duration,
              amount, riskTolerance).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/oracle/simulate",
            body=maybe_transform(
                {
                    "prompt": prompt,
                    "parameters": parameters,
                },
                simulate_run_standard_params.SimulateRunStandardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationResponse,
        )


class AsyncSimulateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncSimulateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncSimulateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncSimulateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncSimulateResourceWithStreamingResponse(self)

    async def run_advanced(
        self,
        *,
        prompt: str,
        scenarios: Iterable[simulate_run_advanced_params.Scenario],
        duration_years: int | Omit = omit,
        initial_state: Optional[simulate_run_advanced_params.InitialState] | Omit = omit,
        sensitivity_analysis_params: Optional[Iterable[simulate_run_advanced_params.SensitivityAnalysisParam]]
        | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> AdvancedSimulationResponse:
        """
        Engages the Quantum Oracle for highly complex, multi-variable simulations,
        allowing precise control over numerous financial parameters, market conditions,
        and personal events to generate deep, predictive insights and sensitivity
        analysis.

        Args:
          prompt: Natural language description of the complex simulation goal.

          scenarios: A list of distinct hypothetical scenarios to run.

          duration_years: Overall duration of the simulation in years.

          initial_state: Optional: Override current user financial data for the simulation's starting
              point.

          sensitivity_analysis_params: Parameters to vary for sensitivity analysis within scenarios.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/oracle/simulate/advanced",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "scenarios": scenarios,
                    "duration_years": duration_years,
                    "initial_state": initial_state,
                    "sensitivity_analysis_params": sensitivity_analysis_params,
                },
                simulate_run_advanced_params.SimulateRunAdvancedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=AdvancedSimulationResponse,
        )

    async def run_standard(
        self,
        *,
        prompt: str,
        parameters: Optional[Dict[str, object]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> SimulationResponse:
        """
        Submits a hypothetical scenario to the Quantum Oracle AI for standard financial
        impact analysis. The AI simulates the effect on the user's current financial
        state and provides a summary.

        Args:
          prompt: Natural language description of the financial scenario to simulate.

          parameters: Optional: Structured parameters to guide the AI simulation (e.g., duration,
              amount, riskTolerance).

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/oracle/simulate",
            body=await async_maybe_transform(
                {
                    "prompt": prompt,
                    "parameters": parameters,
                },
                simulate_run_standard_params.SimulateRunStandardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=SimulationResponse,
        )


class SimulateResourceWithRawResponse:
    def __init__(self, simulate: SimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = to_raw_response_wrapper(
            simulate.run_advanced,
        )
        self.run_standard = to_raw_response_wrapper(
            simulate.run_standard,
        )


class AsyncSimulateResourceWithRawResponse:
    def __init__(self, simulate: AsyncSimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = async_to_raw_response_wrapper(
            simulate.run_advanced,
        )
        self.run_standard = async_to_raw_response_wrapper(
            simulate.run_standard,
        )


class SimulateResourceWithStreamingResponse:
    def __init__(self, simulate: SimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = to_streamed_response_wrapper(
            simulate.run_advanced,
        )
        self.run_standard = to_streamed_response_wrapper(
            simulate.run_standard,
        )


class AsyncSimulateResourceWithStreamingResponse:
    def __init__(self, simulate: AsyncSimulateResource) -> None:
        self._simulate = simulate

        self.run_advanced = async_to_streamed_response_wrapper(
            simulate.run_advanced,
        )
        self.run_standard = async_to_streamed_response_wrapper(
            simulate.run_standard,
        )
