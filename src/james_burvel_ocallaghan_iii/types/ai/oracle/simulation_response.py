# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = ["SimulationResponse", "KeyImpact", "RiskAnalysis", "Visualization"]


class KeyImpact(BaseModel):
    metric: Optional[str] = None

    severity: Optional[Literal["low", "medium", "high"]] = None

    value: Optional[str] = None


class RiskAnalysis(BaseModel):
    max_drawdown: Optional[float] = FieldInfo(alias="maxDrawdown", default=None)
    """Maximum potential loss from peak to trough (e.g., 0.25 for 25%)."""

    volatility_index: Optional[float] = FieldInfo(alias="volatilityIndex", default=None)
    """Measure of market volatility associated with the scenario."""


class Visualization(BaseModel):
    data_uri: Optional[str] = FieldInfo(alias="dataUri", default=None)

    title: Optional[str] = None

    type: Optional[Literal["line_chart", "bar_chart", "table"]] = None


class SimulationResponse(BaseModel):
    key_impacts: List[KeyImpact] = FieldInfo(alias="keyImpacts")
    """Key quantitative and qualitative impacts identified by the AI."""

    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """A natural language summary of the simulation's results and key findings."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the completed simulation."""

    recommendations: Optional[List[AIInsight]] = None
    """Actionable recommendations derived from the simulation."""

    risk_analysis: Optional[RiskAnalysis] = FieldInfo(alias="riskAnalysis", default=None)
    """AI-driven risk assessment of the simulated scenario."""

    visualizations: Optional[List[Visualization]] = None
    """Optional: URLs to generated visualization data or images."""
