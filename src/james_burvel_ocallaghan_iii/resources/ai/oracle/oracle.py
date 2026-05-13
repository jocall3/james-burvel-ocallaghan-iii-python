# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from .simulate import (
    SimulateResource,
    AsyncSimulateResource,
    SimulateResourceWithRawResponse,
    AsyncSimulateResourceWithRawResponse,
    SimulateResourceWithStreamingResponse,
    AsyncSimulateResourceWithStreamingResponse,
)
from ...._compat import cached_property
from .simulations import (
    SimulationsResource,
    AsyncSimulationsResource,
    SimulationsResourceWithRawResponse,
    AsyncSimulationsResourceWithRawResponse,
    SimulationsResourceWithStreamingResponse,
    AsyncSimulationsResourceWithStreamingResponse,
)
from ...._resource import SyncAPIResource, AsyncAPIResource

__all__ = ["OracleResource", "AsyncOracleResource"]


class OracleResource(SyncAPIResource):
    @cached_property
    def simulate(self) -> SimulateResource:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return SimulateResource(self._client)

    @cached_property
    def simulations(self) -> SimulationsResource:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return SimulationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> OracleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return OracleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> OracleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return OracleResourceWithStreamingResponse(self)


class AsyncOracleResource(AsyncAPIResource):
    @cached_property
    def simulate(self) -> AsyncSimulateResource:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return AsyncSimulateResource(self._client)

    @cached_property
    def simulations(self) -> AsyncSimulationsResource:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return AsyncSimulationsResource(self._client)

    @cached_property
    def with_raw_response(self) -> AsyncOracleResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncOracleResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncOracleResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncOracleResourceWithStreamingResponse(self)


class OracleResourceWithRawResponse:
    def __init__(self, oracle: OracleResource) -> None:
        self._oracle = oracle

    @cached_property
    def simulate(self) -> SimulateResourceWithRawResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return SimulateResourceWithRawResponse(self._oracle.simulate)

    @cached_property
    def simulations(self) -> SimulationsResourceWithRawResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return SimulationsResourceWithRawResponse(self._oracle.simulations)


class AsyncOracleResourceWithRawResponse:
    def __init__(self, oracle: AsyncOracleResource) -> None:
        self._oracle = oracle

    @cached_property
    def simulate(self) -> AsyncSimulateResourceWithRawResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return AsyncSimulateResourceWithRawResponse(self._oracle.simulate)

    @cached_property
    def simulations(self) -> AsyncSimulationsResourceWithRawResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return AsyncSimulationsResourceWithRawResponse(self._oracle.simulations)


class OracleResourceWithStreamingResponse:
    def __init__(self, oracle: OracleResource) -> None:
        self._oracle = oracle

    @cached_property
    def simulate(self) -> SimulateResourceWithStreamingResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return SimulateResourceWithStreamingResponse(self._oracle.simulate)

    @cached_property
    def simulations(self) -> SimulationsResourceWithStreamingResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return SimulationsResourceWithStreamingResponse(self._oracle.simulations)


class AsyncOracleResourceWithStreamingResponse:
    def __init__(self, oracle: AsyncOracleResource) -> None:
        self._oracle = oracle

    @cached_property
    def simulate(self) -> AsyncSimulateResourceWithStreamingResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return AsyncSimulateResourceWithStreamingResponse(self._oracle.simulate)

    @cached_property
    def simulations(self) -> AsyncSimulationsResourceWithStreamingResponse:
        """Unleash the power of 'what-if' scenario modeling.

        Run complex, multi-variable financial simulations with AI-powered foresight to understand future impacts and optimize strategies.
        """
        return AsyncSimulationsResourceWithStreamingResponse(self._oracle.simulations)
