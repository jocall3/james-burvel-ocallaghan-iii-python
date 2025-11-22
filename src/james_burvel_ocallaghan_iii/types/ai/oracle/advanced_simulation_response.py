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
    emergency_fund_depletion_months: Optional[int] = FieldInfo(alias="emergencyFundDepletionMonths", default=None)
    """How many months the emergency fund lasted."""

    min_cash_balance: Optional[float] = FieldInfo(alias="minCashBalance", default=None)
    """The lowest cash balance reached during the simulation."""

    recovery_time_months: Optional[int] = FieldInfo(alias="recoveryTimeMonths", default=None)
    """Time (in months) to recover from a financial shock, if applicable."""


class ScenarioResultSensitivityAnalysisGraphData(BaseModel):
    outcome_value: Optional[float] = FieldInfo(alias="outcomeValue", default=None)
    """The resulting key outcome value."""

    param_value: Optional[float] = FieldInfo(alias="paramValue", default=None)
    """The value of the varied parameter."""


class ScenarioResultSensitivityAnalysisGraph(BaseModel):
    data: List[ScenarioResultSensitivityAnalysisGraphData]
    """Data points for plotting the parameter's impact on a key outcome."""

    param_name: str = FieldInfo(alias="paramName")
    """The name of the parameter varied in the sensitivity analysis."""


class ScenarioResult(BaseModel):
    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """Summary of results specific to this scenario."""

    scenario_name: str = FieldInfo(alias="scenarioName")
    """Name of the simulated scenario."""

    detailed_financial_projections: Optional[object] = FieldInfo(alias="detailedFinancialProjections", default=None)
    """Time-series data for various financial metrics (e.g., monthly cash balance)."""

    final_net_worth_projected: Optional[float] = FieldInfo(alias="finalNetWorthProjected", default=None)
    """Projected net worth at the end of the simulation period for this scenario."""

    liquidity_metrics: Optional[ScenarioResultLiquidityMetrics] = FieldInfo(alias="liquidityMetrics", default=None)
    """Key liquidity indicators for the scenario."""

    sensitivity_analysis_graphs: Optional[List[ScenarioResultSensitivityAnalysisGraph]] = FieldInfo(
        alias="sensitivityAnalysisGraphs", default=None
    )
    """Data points for visualizing sensitivity analysis of key parameters."""


class AdvancedSimulationResponse(BaseModel):
    overall_summary: str = FieldInfo(alias="overallSummary")
    """A high-level summary of the simulation across all scenarios."""

    scenario_results: List[ScenarioResult] = FieldInfo(alias="scenarioResults")
    """Detailed results for each simulated scenario."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the advanced simulation."""

    comparison_analysis: Optional[object] = FieldInfo(alias="comparisonAnalysis", default=None)
    """Quantitative comparison across scenarios (e.g., best-case vs. worst-case NPV)."""

    strategic_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="strategicRecommendations", default=None)
    """Overarching strategic recommendations derived from the complex simulation."""
