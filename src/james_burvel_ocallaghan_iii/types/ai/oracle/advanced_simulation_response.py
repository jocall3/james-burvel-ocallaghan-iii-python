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

    recovery_time_months: Optional[int] = FieldInfo(alias="recoveryTimeMonths", default=None)


class ScenarioResultSensitivityAnalysisGraphData(BaseModel):
    outcome_value: Optional[float] = FieldInfo(alias="outcomeValue", default=None)

    param_value: Optional[float] = FieldInfo(alias="paramValue", default=None)


class ScenarioResultSensitivityAnalysisGraph(BaseModel):
    data: Optional[List[ScenarioResultSensitivityAnalysisGraphData]] = None

    param_name: Optional[str] = FieldInfo(alias="paramName", default=None)


class ScenarioResult(BaseModel):
    final_net_worth_projected: float = FieldInfo(alias="finalNetWorthProjected")
    """Projected net worth at the end of the simulation for this scenario."""

    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """Summary of results for this specific scenario."""

    scenario_name: str = FieldInfo(alias="scenarioName")
    """Name of the specific scenario simulated."""

    liquidity_metrics: Optional[ScenarioResultLiquidityMetrics] = FieldInfo(alias="liquidityMetrics", default=None)
    """Key liquidity metrics for the scenario."""

    sensitivity_analysis_graphs: Optional[List[ScenarioResultSensitivityAnalysisGraph]] = FieldInfo(
        alias="sensitivityAnalysisGraphs", default=None
    )
    """Data points for generating sensitivity analysis charts."""


class AdvancedSimulationResponse(BaseModel):
    overall_summary: str = FieldInfo(alias="overallSummary")
    """A high-level narrative summary of the key findings across all scenarios."""

    scenario_results: List[ScenarioResult] = FieldInfo(alias="scenarioResults")

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the advanced simulation."""

    strategic_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="strategicRecommendations", default=None)
    """Strategic, actionable recommendations derived from the complex simulation."""
