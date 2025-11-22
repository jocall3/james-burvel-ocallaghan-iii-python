# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "SimulateRunAdvancedParams",
    "Scenario",
    "ScenarioEvent",
    "ScenarioSensitivityAnalysisParam",
    "InitialState",
    "SensitivityAnalysisParam",
]


class SimulateRunAdvancedParams(TypedDict, total=False):
    prompt: Required[str]
    """Natural language description of the complex simulation goal."""

    scenarios: Required[Iterable[Scenario]]
    """A list of distinct hypothetical scenarios to run."""

    duration_years: Annotated[int, PropertyInfo(alias="durationYears")]
    """Overall duration of the simulation in years."""

    initial_state: Annotated[Optional[InitialState], PropertyInfo(alias="initialState")]
    """
    Optional: Override current user financial data for the simulation's starting
    point.
    """

    sensitivity_analysis_params: Annotated[
        Optional[Iterable[SensitivityAnalysisParam]], PropertyInfo(alias="sensitivityAnalysisParams")
    ]
    """Parameters to vary for sensitivity analysis within scenarios."""


class ScenarioEvent(TypedDict, total=False):
    details: Required[Dict[str, object]]
    """Specific parameters for the event type (e.g., durationMonths for job_loss)."""

    type: Required[
        Literal[
            "job_loss",
            "market_downturn",
            "market_boom",
            "inheritance",
            "major_expense",
            "new_income_stream",
            "interest_rate_change",
        ]
    ]
    """Type of event occurring in the scenario."""

    start_month: Annotated[Optional[int], PropertyInfo(alias="startMonth")]
    """Optional: The month (relative to simulation start) when this event occurs."""


class ScenarioSensitivityAnalysisParam(TypedDict, total=False):
    max: float

    min: float

    param_name: Annotated[str, PropertyInfo(alias="paramName")]

    step: float


class Scenario(TypedDict, total=False):
    events: Required[Iterable[ScenarioEvent]]
    """
    Key events that define this scenario (e.g., job loss, market crash,
    inheritance).
    """

    name: Required[str]
    """A descriptive name for the scenario."""

    duration_years: Annotated[Optional[int], PropertyInfo(alias="durationYears")]
    """
    Optional: Duration of this specific scenario, overrides global duration if
    present.
    """

    sensitivity_analysis_params: Annotated[
        Optional[Iterable[ScenarioSensitivityAnalysisParam]], PropertyInfo(alias="sensitivityAnalysisParams")
    ]
    """Optional: Scenario-specific parameters for sensitivity analysis."""


class InitialState(TypedDict, total=False):
    monthly_income_override: Annotated[Optional[float], PropertyInfo(alias="monthlyIncomeOverride")]

    net_worth_override: Annotated[Optional[float], PropertyInfo(alias="netWorthOverride")]


class SensitivityAnalysisParam(TypedDict, total=False):
    max: float

    min: float

    param_name: Annotated[str, PropertyInfo(alias="paramName")]

    step: float
