# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulationResponse", "KeyImpact", "Recommendation", "RiskAnalysis"]


class KeyImpact(BaseModel):
    metric: str
    """The financial metric being impacted."""

    value: str
    """The projected value or range for the metric."""

    severity: Optional[Literal["low", "medium", "high"]] = None
    """The severity of the impact (e.g., positive or negative significant change)."""


class Recommendation(BaseModel):
    description: str
    """Detailed explanation of the recommendation."""

    title: str
    """A concise title for the recommendation."""

    action_trigger: Optional[str] = FieldInfo(alias="actionTrigger", default=None)
    """An identifier or URI to trigger a specific action within the application."""


class RiskAnalysis(BaseModel):
    max_drawdown: Optional[float] = FieldInfo(alias="maxDrawdown", default=None)
    """Worst historical decline from a peak (e.g., 0.25 for 25% drop)."""

    scenario_analysis: Optional[object] = FieldInfo(alias="scenarioAnalysis", default=None)
    """Further details on how different adverse scenarios impact the outcome."""

    volatility_index: Optional[float] = FieldInfo(alias="volatilityIndex", default=None)
    """A measure of market or portfolio volatility (e.g., standard deviation)."""


class SimulationResponse(BaseModel):
    key_impacts: List[KeyImpact] = FieldInfo(alias="keyImpacts")
    """Key financial metrics and their projected impact."""

    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """A natural language summary of the simulation results."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the completed simulation."""

    recommendations: Optional[List[Recommendation]] = None
    """Actionable AI-driven recommendations based on the simulation."""

    risk_analysis: Optional[RiskAnalysis] = FieldInfo(alias="riskAnalysis", default=None)
    """Detailed analysis of potential risks associated with the simulated scenario."""
