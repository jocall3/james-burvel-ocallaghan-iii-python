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
    prompt: Required[object]
    """A natural language prompt describing the complex, multi-variable scenario."""

    scenarios: Required[Iterable[Scenario]]

    global_economic_factors: Annotated[GlobalEconomicFactors, PropertyInfo(alias="globalEconomicFactors")]
    """Optional: Global economic conditions to apply to all scenarios."""

    personal_assumptions: Annotated[PersonalAssumptions, PropertyInfo(alias="personalAssumptions")]
    """Optional: Personal financial assumptions to override defaults."""


class ScenarioEvent(TypedDict, total=False):
    details: object
    """Specific parameters for the event (e.g., durationMonths, impactPercentage)."""

    type: Literal["job_loss", "market_downturn", "large_purchase", "income_increase", "medical_emergency"]


class ScenarioSensitivityAnalysisParam(TypedDict, total=False):
    max: object
    """Maximum value for the parameter."""

    min: object
    """Minimum value for the parameter."""

    param_name: Annotated[object, PropertyInfo(alias="paramName")]
    """
    The name of the parameter to vary for sensitivity analysis (e.g.,
    'interestRate', 'inflationRate', 'marketRecoveryRate').
    """

    step: object
    """Step increment for varying the parameter."""


class Scenario(TypedDict, total=False):
    duration_years: Required[Annotated[object, PropertyInfo(alias="durationYears")]]
    """The duration in years over which this scenario is simulated."""

    events: Required[Iterable[ScenarioEvent]]
    """A list of discrete or continuous events that define this scenario."""

    name: Required[object]
    """A descriptive name for this specific scenario."""

    sensitivity_analysis_params: Annotated[
        Optional[Iterable[ScenarioSensitivityAnalysisParam]], PropertyInfo(alias="sensitivityAnalysisParams")
    ]
    """Parameters for multi-variable sensitivity analysis within this scenario."""


class GlobalEconomicFactors(TypedDict, total=False):
    """Optional: Global economic conditions to apply to all scenarios."""

    inflation_rate: Annotated[object, PropertyInfo(alias="inflationRate")]

    interest_rate_baseline: Annotated[object, PropertyInfo(alias="interestRateBaseline")]


class PersonalAssumptions(TypedDict, total=False):
    """Optional: Personal financial assumptions to override defaults."""

    annual_savings_rate: Annotated[object, PropertyInfo(alias="annualSavingsRate")]

    risk_tolerance: Annotated[Literal["conservative", "moderate", "aggressive"], PropertyInfo(alias="riskTolerance")]
