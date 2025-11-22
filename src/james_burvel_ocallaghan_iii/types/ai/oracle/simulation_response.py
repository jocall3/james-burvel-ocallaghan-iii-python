# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = ["SimulationResponse", "KeyImpact", "RiskAnalysis", "RiskAnalysisStressTestResult"]


class KeyImpact(BaseModel):
    metric: Optional[str] = None

    severity: Optional[Literal["low", "medium", "high"]] = None

    value: Optional[str] = None


class RiskAnalysisStressTestResult(BaseModel):
    impact: Optional[str] = None

    scenario: Optional[str] = None


class RiskAnalysis(BaseModel):
    max_drawdown: Optional[float] = FieldInfo(alias="maxDrawdown", default=None)
    """Maximum expected percentage drop from a peak value."""

    stress_test_results: Optional[List[RiskAnalysisStressTestResult]] = FieldInfo(
        alias="stressTestResults", default=None
    )

    volatility_index: Optional[float] = FieldInfo(alias="volatilityIndex", default=None)
    """An index representing the expected volatility of the outcome."""


class SimulationResponse(BaseModel):
    key_impacts: List[KeyImpact] = FieldInfo(alias="keyImpacts")
    """Key financial metrics and their projected values/changes."""

    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """A natural language summary of the simulation's findings."""

    recommendations: List[AIInsight]
    """Actionable recommendations derived from the simulation."""

    risk_analysis: Optional[RiskAnalysis] = FieldInfo(alias="riskAnalysis", default=None)
    """Detailed analysis of risks and potential stress test scenarios."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the completed simulation."""

    generated_on: Optional[datetime] = FieldInfo(alias="generatedOn", default=None)
    """Timestamp when the simulation was generated."""
