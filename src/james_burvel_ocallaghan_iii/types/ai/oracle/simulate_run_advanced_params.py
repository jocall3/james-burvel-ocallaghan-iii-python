# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypeAlias, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "SimulateRunAdvancedParams",
    "Scenario",
    "ScenarioEvent",
    "ScenarioEventDetails",
    "ScenarioEventDetailsJobLossDetails",
    "ScenarioEventDetailsMarketDownturnDetails",
    "ScenarioEventDetailsUnionMember2",
    "ScenarioMarketConditions",
    "ScenarioSensitivityAnalysisParam",
]


class SimulateRunAdvancedParams(TypedDict, total=False):
    prompt: Required[str]
    """A high-level natural language prompt describing the complex simulation."""

    scenarios: Required[Iterable[Scenario]]
    """A list of one or more detailed scenarios to simulate."""

    global_parameters: Annotated[Optional[object], PropertyInfo(alias="globalParameters")]
    """
    Optional: Parameters that apply to all scenarios unless overridden (e.g.,
    overall economic growth rate).
    """


class ScenarioEventDetailsJobLossDetails(TypedDict, total=False):
    duration_months: Required[Annotated[int, PropertyInfo(alias="durationMonths")]]
    """Expected duration of unemployment in months."""

    severance_amount: Required[Annotated[float, PropertyInfo(alias="severanceAmount")]]
    """Total severance package received."""

    new_job_salary_multiplier: Annotated[float, PropertyInfo(alias="newJobSalaryMultiplier")]
    """Multiplier for new job salary compared to old (e.g., 0.9 for 90%)."""

    unemployment_benefits: Annotated[Optional[float], PropertyInfo(alias="unemploymentBenefits")]
    """Monthly unemployment benefits."""


class ScenarioEventDetailsMarketDownturnDetails(TypedDict, total=False):
    impact_percentage: Required[Annotated[float, PropertyInfo(alias="impactPercentage")]]
    """Percentage drop in investment portfolio value (e.g., 0.15 for 15% drop)."""

    recovery_years: Required[Annotated[int, PropertyInfo(alias="recoveryYears")]]
    """Number of years expected for market to recover."""


class ScenarioEventDetailsUnionMember2(TypedDict, total=False):
    amount: float
    """Amount for the event."""

    timing_months: Annotated[int, PropertyInfo(alias="timingMonths")]
    """Timing of the event in months from start."""


ScenarioEventDetails: TypeAlias = Union[
    ScenarioEventDetailsJobLossDetails, ScenarioEventDetailsMarketDownturnDetails, ScenarioEventDetailsUnionMember2
]


class ScenarioEvent(TypedDict, total=False):
    type: Required[
        Literal["job_loss", "market_downturn", "significant_expense", "windfall", "salary_increase", "new_investment"]
    ]
    """Type of financial or life event."""

    details: ScenarioEventDetails
    """Specific details for the event type."""

    year_in_simulation: Annotated[int, PropertyInfo(alias="yearInSimulation")]
    """The year in the simulation when this event occurs."""


class ScenarioMarketConditions(TypedDict, total=False):
    average_annual_return: Annotated[float, PropertyInfo(alias="averageAnnualReturn")]
    """Average annual market return."""

    volatility: float
    """Market volatility index."""


class ScenarioSensitivityAnalysisParam(TypedDict, total=False):
    max: Required[float]
    """Maximum value for the parameter."""

    min: Required[float]
    """Minimum value for the parameter."""

    param_name: Required[Annotated[str, PropertyInfo(alias="paramName")]]
    """Name of the parameter to vary."""

    step: Optional[float]
    """Step increment for the parameter."""


class Scenario(TypedDict, total=False):
    duration_years: Required[Annotated[int, PropertyInfo(alias="durationYears")]]
    """The total duration of the simulation for this scenario in years."""

    name: Required[str]
    """A descriptive name for the individual scenario."""

    description: Optional[str]
    """Detailed description of the scenario."""

    events: Optional[Iterable[ScenarioEvent]]
    """A sequence of financial or life events to include in the simulation."""

    market_conditions: Annotated[Optional[ScenarioMarketConditions], PropertyInfo(alias="marketConditions")]

    sensitivity_analysis_params: Annotated[
        Optional[Iterable[ScenarioSensitivityAnalysisParam]], PropertyInfo(alias="sensitivityAnalysisParams")
    ]
    """Parameters to vary for sensitivity analysis within this scenario."""
