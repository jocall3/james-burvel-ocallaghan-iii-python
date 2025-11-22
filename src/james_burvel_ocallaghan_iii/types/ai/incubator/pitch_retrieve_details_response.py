# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict, List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ...._models import BaseModel
from .quantum_weaver_state import QuantumWeaverState

__all__ = [
    "PitchRetrieveDetailsResponse",
    "PitchRetrieveDetailsResponseAICoachingPlan",
    "PitchRetrieveDetailsResponseAICoachingPlanStep",
    "PitchRetrieveDetailsResponseAICoachingPlanStepResource",
    "PitchRetrieveDetailsResponseAIFinancialModel",
    "PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis",
    "PitchRetrieveDetailsResponseAIMarketAnalysis",
    "PitchRetrieveDetailsResponseAIRiskAssessment",
]


class PitchRetrieveDetailsResponseAICoachingPlanStepResource(BaseModel):
    name: Optional[str] = None
    """Name of the resource."""

    url: Optional[str] = None
    """URL to the resource."""


class PitchRetrieveDetailsResponseAICoachingPlanStep(BaseModel):
    description: str
    """Detailed description of the step."""

    status: Literal["pending", "in_progress", "completed", "deferred"]
    """Current status of the step."""

    timeline: str
    """Suggested timeline for completing the step."""

    title: str
    """Title of the coaching step."""

    resources: Optional[List[PitchRetrieveDetailsResponseAICoachingPlanStepResource]] = None
    """Optional: Links to helpful resources for the step."""


class PitchRetrieveDetailsResponseAICoachingPlan(BaseModel):
    steps: Optional[List[PitchRetrieveDetailsResponseAICoachingPlanStep]] = None
    """Detailed steps of the coaching plan."""

    summary: Optional[str] = None
    """Summary of the coaching plan."""

    title: Optional[str] = None
    """Title of the coaching plan."""


class PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis(BaseModel):
    projected_irr: Optional[float] = FieldInfo(alias="projectedIRR", default=None)

    scenario: Optional[str] = None

    terminal_value: Optional[float] = FieldInfo(alias="terminalValue", default=None)


class PitchRetrieveDetailsResponseAIFinancialModel(BaseModel):
    breakeven_point: Optional[str] = FieldInfo(alias="breakevenPoint", default=None)
    """AI's estimate of when the venture will break even."""

    capital_requirements: Optional[float] = FieldInfo(alias="capitalRequirements", default=None)
    """AI's estimated total capital required to reach profitability."""

    cost_structure_analysis: Optional[Dict[str, str]] = FieldInfo(alias="costStructureAnalysis", default=None)
    """AI's analysis of the venture's cost structure."""

    revenue_breakdown: Optional[Dict[str, str]] = FieldInfo(alias="revenueBreakdown", default=None)
    """AI's projected revenue breakdown over years."""

    sensitivity_analysis: Optional[List[PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis]] = FieldInfo(
        alias="sensitivityAnalysis", default=None
    )
    """Sensitivity analysis for different growth scenarios."""


class PitchRetrieveDetailsResponseAIMarketAnalysis(BaseModel):
    competitive_advantages: Optional[List[str]] = FieldInfo(alias="competitiveAdvantages", default=None)
    """AI's identified competitive advantages of the venture."""

    growth_opportunities: Optional[str] = FieldInfo(alias="growthOpportunities", default=None)
    """AI-identified growth opportunities."""

    risk_factors: Optional[str] = FieldInfo(alias="riskFactors", default=None)
    """AI-identified market-related risk factors."""

    target_market_size: Optional[str] = FieldInfo(alias="targetMarketSize", default=None)
    """AI's assessment of the total addressable market size."""


class PitchRetrieveDetailsResponseAIRiskAssessment(BaseModel):
    market_risk: Optional[str] = FieldInfo(alias="marketRisk", default=None)
    """Assessment of market risks."""

    overall_score: Optional[float] = FieldInfo(alias="overallScore", default=None)
    """Overall AI risk score (0-1, lower is better)."""

    regulatory_risk: Optional[str] = FieldInfo(alias="regulatoryRisk", default=None)
    """Assessment of regulatory risks."""

    team_risk: Optional[str] = FieldInfo(alias="teamRisk", default=None)
    """Assessment of team-related risks."""

    technical_risk: Optional[str] = FieldInfo(alias="technicalRisk", default=None)
    """Assessment of technical risks."""


class PitchRetrieveDetailsResponse(QuantumWeaverState):
    ai_coaching_plan: Optional[PitchRetrieveDetailsResponseAICoachingPlan] = FieldInfo(
        alias="aiCoachingPlan", default=None
    )
    """
    AI-generated coaching plan to help refine the business or prepare for next
    steps.
    """

    ai_financial_model: Optional[PitchRetrieveDetailsResponseAIFinancialModel] = FieldInfo(
        alias="aiFinancialModel", default=None
    )
    """AI-generated financial model and projections based on the pitch."""

    ai_market_analysis: Optional[PitchRetrieveDetailsResponseAIMarketAnalysis] = FieldInfo(
        alias="aiMarketAnalysis", default=None
    )
    """AI's in-depth market analysis and validation."""

    ai_risk_assessment: Optional[PitchRetrieveDetailsResponseAIRiskAssessment] = FieldInfo(
        alias="aiRiskAssessment", default=None
    )
    """AI's assessment of various risks associated with the venture."""

    feedback_summary: Optional[object] = FieldInfo(alias="feedbackSummary", default=None)  # type: ignore
    """A detailed summary of Quantum Weaver's initial analysis and feedback."""

    investor_match_score: Optional[float] = FieldInfo(alias="investorMatchScore", default=None)
    """AI's score on how well the pitch aligns with investor criteria."""
