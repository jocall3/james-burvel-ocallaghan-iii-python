# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel

__all__ = ["SimulationResponse", "KeyImpact", "Recommendation", "RiskAnalysis"]


class KeyImpact(BaseModel):
    metric: Optional[str] = None

    severity: Optional[Literal["low", "medium", "high", "critical"]] = None

    value: Optional[str] = None


class Recommendation(BaseModel):
    action_trigger: Optional[str] = FieldInfo(alias="actionTrigger", default=None)

    description: Optional[str] = None

    title: Optional[str] = None


class RiskAnalysis(BaseModel):
    max_drawdown: Optional[float] = FieldInfo(alias="maxDrawdown", default=None)
    """Maximum potential percentage loss from peak to trough."""

    volatility_index: Optional[float] = FieldInfo(alias="volatilityIndex", default=None)
    """AI-calculated volatility index for the simulated scenario."""


class SimulationResponse(BaseModel):
    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """A natural language summary of the simulation's findings and overall impact."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the completed simulation."""

    key_impacts: Optional[List[KeyImpact]] = FieldInfo(alias="keyImpacts", default=None)
    """Key financial metrics and their projected changes due to the simulation."""

    recommendations: Optional[List[Recommendation]] = None
    """Actionable recommendations derived from the simulation results."""

    risk_analysis: Optional[RiskAnalysis] = FieldInfo(alias="riskAnalysis", default=None)
    """AI-driven risk assessment of the simulated scenario."""
