# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from ...transactions.ai_insight import AIInsight

__all__ = [
    "AdvancedSimulationResponse",
    "ScenarioResult",
    "ScenarioResultLiquidityMetrics",
    "ScenarioResultSensitivityAnalysisGraph",
    "ScenarioResultSensitivityAnalysisGraphData",
]


class ScenarioResultLiquidityMetrics(BaseModel):
    min_cash_balance: Optional[float] = FieldInfo(alias="minCashBalance", default=None)
    """Minimum cash balance reached during the scenario."""

    recovery_time_months: Optional[int] = FieldInfo(alias="recoveryTimeMonths", default=None)
    """Time in months to recover to pre-event financial state."""


class ScenarioResultSensitivityAnalysisGraphData(BaseModel):
    outcome_value: Optional[float] = FieldInfo(alias="outcomeValue", default=None)

    param_value: Optional[float] = FieldInfo(alias="paramValue", default=None)


class ScenarioResultSensitivityAnalysisGraph(BaseModel):
    data: Optional[List[ScenarioResultSensitivityAnalysisGraphData]] = None

    param_name: Optional[str] = FieldInfo(alias="paramName", default=None)


class ScenarioResult(BaseModel):
    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """Summary of results for this specific scenario."""

    scenario_name: str = FieldInfo(alias="scenarioName")
    """Name of the individual scenario."""

    ai_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiInsights", default=None)
    """Specific AI insights for this scenario."""

    final_net_worth_projected: Optional[float] = FieldInfo(alias="finalNetWorthProjected", default=None)
    """Projected net worth at the end of the simulation period for this scenario."""

    liquidity_metrics: Optional[ScenarioResultLiquidityMetrics] = FieldInfo(alias="liquidityMetrics", default=None)

    sensitivity_analysis_graphs: Optional[List[ScenarioResultSensitivityAnalysisGraph]] = FieldInfo(
        alias="sensitivityAnalysisGraphs", default=None
    )
    """
    Data for generating sensitivity analysis charts (e.g., how net worth changes as
    a variable is adjusted).
    """


class AdvancedSimulationResponse(BaseModel):
    overall_summary: str = FieldInfo(alias="overallSummary")
    """A high-level summary of findings across all scenarios."""

    scenario_results: List[ScenarioResult] = FieldInfo(alias="scenarioResults")

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the completed advanced simulation."""

    strategic_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="strategicRecommendations", default=None)
    """Overarching strategic recommendations derived from the comparison of scenarios."""
