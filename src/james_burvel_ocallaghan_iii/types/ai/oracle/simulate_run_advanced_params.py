# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = [
    "SimulateRunAdvancedParams",
    "Scenario",
    "ScenarioEvent",
    "ScenarioSensitivityAnalysisParam",
    "GlobalEconomicFactors",
    "PersonalAssumptions",
]


class SimulateRunAdvancedParams(TypedDict, total=False):
    prompt: Required[str]
    """A natural language prompt describing the complex, multi-variable scenario."""

    scenarios: Required[Iterable[Scenario]]

    global_economic_factors: Annotated[Optional[GlobalEconomicFactors], PropertyInfo(alias="globalEconomicFactors")]
    """Optional: Global economic conditions to apply to all scenarios."""

    personal_assumptions: Annotated[Optional[PersonalAssumptions], PropertyInfo(alias="personalAssumptions")]
    """Optional: Personal financial assumptions to override defaults."""


class ScenarioEvent(TypedDict, total=False):
    details: object
    """Specific parameters for the event (e.g., durationMonths, impactPercentage)."""

    type: Literal["job_loss", "market_downturn", "large_purchase", "income_increase", "medical_emergency"]


class ScenarioSensitivityAnalysisParam(TypedDict, total=False):
    max: float
    """Maximum value for the parameter."""

    min: float
    """Minimum value for the parameter."""

    param_name: Annotated[str, PropertyInfo(alias="paramName")]
    """
    The name of the parameter to vary for sensitivity analysis (e.g.,
    'interestRate', 'inflationRate', 'marketRecoveryRate').
    """

    step: float
    """Step increment for varying the parameter."""


class Scenario(TypedDict, total=False):
    duration_years: Required[Annotated[int, PropertyInfo(alias="durationYears")]]
    """The duration in years over which this scenario is simulated."""

    events: Required[Iterable[ScenarioEvent]]
    """A list of discrete or continuous events that define this scenario."""

    name: Required[str]
    """A descriptive name for this specific scenario."""

    sensitivity_analysis_params: Annotated[
        Optional[Iterable[ScenarioSensitivityAnalysisParam]], PropertyInfo(alias="sensitivityAnalysisParams")
    ]
    """Parameters for multi-variable sensitivity analysis within this scenario."""


class GlobalEconomicFactors(TypedDict, total=False):
    inflation_rate: Annotated[float, PropertyInfo(alias="inflationRate")]

    interest_rate_baseline: Annotated[float, PropertyInfo(alias="interestRateBaseline")]


class PersonalAssumptions(TypedDict, total=False):
    annual_savings_rate: Annotated[float, PropertyInfo(alias="annualSavingsRate")]

    risk_tolerance: Annotated[Literal["conservative", "moderate", "aggressive"], PropertyInfo(alias="riskTolerance")]
