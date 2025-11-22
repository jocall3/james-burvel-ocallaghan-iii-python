# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Union
from typing_extensions import TypeAlias

from .simulation_response import SimulationResponse
from .advanced_simulation_response import AdvancedSimulationResponse

__all__ = ["SimulationRetrieveResponse"]

SimulationRetrieveResponse: TypeAlias = Union[SimulationResponse, AdvancedSimulationResponse]
