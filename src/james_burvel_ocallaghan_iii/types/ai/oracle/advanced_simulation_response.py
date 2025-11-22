# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime

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
    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """A summary of the outcomes for this specific scenario."""

    scenario_name: str = FieldInfo(alias="scenarioName")
    """The name of the simulated scenario."""

    final_net_worth_projected: Optional[float] = FieldInfo(alias="finalNetWorthProjected", default=None)
    """Projected net worth at the end of the scenario."""

    liquidity_metrics: Optional[ScenarioResultLiquidityMetrics] = FieldInfo(alias="liquidityMetrics", default=None)
    """Key metrics related to cash flow and liquidity within the scenario."""

    scenario_specific_recommendations: Optional[List[AIInsight]] = FieldInfo(
        alias="scenarioSpecificRecommendations", default=None
    )
    """Recommendations specific to this scenario."""

    sensitivity_analysis_graphs: Optional[List[ScenarioResultSensitivityAnalysisGraph]] = FieldInfo(
        alias="sensitivityAnalysisGraphs", default=None
    )
    """Data points for generating sensitivity analysis graphs."""


class AdvancedSimulationResponse(BaseModel):
    overall_summary: str = FieldInfo(alias="overallSummary")
    """A high-level summary of all scenario findings and overarching conclusions."""

    scenario_results: List[ScenarioResult] = FieldInfo(alias="scenarioResults")
    """Detailed results for each simulated scenario."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the completed advanced simulation."""

    generated_on: Optional[datetime] = FieldInfo(alias="generatedOn", default=None)
    """Timestamp when the simulation was generated."""

    strategic_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="strategicRecommendations", default=None)
    """Long-term strategic recommendations derived from the complex simulations."""
