# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["SimulateRunAdvancedParams", "Scenario", "ScenarioEvent", "ScenarioSensitivityAnalysisParam"]


class SimulateRunAdvancedParams(TypedDict, total=False):
    prompt: Required[str]
    """Natural language description of the complex financial simulation."""

    scenarios: Required[Iterable[Scenario]]


class ScenarioEvent(TypedDict, total=False):
    details: Required[object]
    """Specific parameters for the event type."""

    type: Required[
        Literal[
            "job_loss",
            "market_downturn",
            "major_expense",
            "income_increase",
            "large_investment",
            "property_purchase",
            "inheritance",
        ]
    ]
    """Type of event occurring in the scenario."""


class ScenarioSensitivityAnalysisParam(TypedDict, total=False):
    max: Required[float]

    min: Required[float]

    param_name: Required[Annotated[str, PropertyInfo(alias="paramName")]]

    step: Optional[float]


class Scenario(TypedDict, total=False):
    duration_years: Required[Annotated[int, PropertyInfo(alias="durationYears")]]
    """The duration of the simulation in years."""

    events: Required[Iterable[ScenarioEvent]]

    name: Required[str]
    """Name for this specific scenario."""

    sensitivity_analysis_params: Annotated[
        Optional[Iterable[ScenarioSensitivityAnalysisParam]], PropertyInfo(alias="sensitivityAnalysisParams")
    ]
    """
    Parameters for which sensitivity analysis should be performed within this
    scenario.
    """
