# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
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
    name: Optional[object] = None

    url: Optional[object] = None


class PitchRetrieveDetailsResponseAICoachingPlanStep(BaseModel):
    description: Optional[object] = None

    resources: Optional[List[PitchRetrieveDetailsResponseAICoachingPlanStepResource]] = None

    status: Optional[Literal["pending", "in_progress", "completed"]] = None

    timeline: Optional[object] = None

    title: Optional[object] = None


class PitchRetrieveDetailsResponseAICoachingPlan(BaseModel):
    """AI-generated coaching plan for the entrepreneur."""

    steps: Optional[List[PitchRetrieveDetailsResponseAICoachingPlanStep]] = None

    summary: Optional[object] = None

    title: Optional[object] = None


class PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis(BaseModel):
    projected_irr: Optional[object] = FieldInfo(alias="projectedIRR", default=None)

    scenario: Optional[object] = None

    terminal_value: Optional[object] = FieldInfo(alias="terminalValue", default=None)


class PitchRetrieveDetailsResponseAIFinancialModel(BaseModel):
    """AI's detailed financial model analysis."""

    breakeven_point: Optional[object] = FieldInfo(alias="breakevenPoint", default=None)

    capital_requirements: Optional[object] = FieldInfo(alias="capitalRequirements", default=None)

    cost_structure_analysis: Optional[object] = FieldInfo(alias="costStructureAnalysis", default=None)

    revenue_breakdown: Optional[object] = FieldInfo(alias="revenueBreakdown", default=None)

    sensitivity_analysis: Optional[List[PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis]] = FieldInfo(
        alias="sensitivityAnalysis", default=None
    )


class PitchRetrieveDetailsResponseAIMarketAnalysis(BaseModel):
    """AI's detailed market analysis."""

    competitive_advantages: Optional[List[object]] = FieldInfo(alias="competitiveAdvantages", default=None)

    growth_opportunities: Optional[object] = FieldInfo(alias="growthOpportunities", default=None)

    risk_factors: Optional[object] = FieldInfo(alias="riskFactors", default=None)

    target_market_size: Optional[object] = FieldInfo(alias="targetMarketSize", default=None)


class PitchRetrieveDetailsResponseAIRiskAssessment(BaseModel):
    """AI's assessment of risks associated with the venture."""

    market_risk: Optional[object] = FieldInfo(alias="marketRisk", default=None)

    team_risk: Optional[object] = FieldInfo(alias="teamRisk", default=None)

    technical_risk: Optional[object] = FieldInfo(alias="technicalRisk", default=None)


class PitchRetrieveDetailsResponse(QuantumWeaverState):
    ai_coaching_plan: Optional[PitchRetrieveDetailsResponseAICoachingPlan] = FieldInfo(
        alias="aiCoachingPlan", default=None
    )
    """AI-generated coaching plan for the entrepreneur."""

    ai_financial_model: Optional[PitchRetrieveDetailsResponseAIFinancialModel] = FieldInfo(
        alias="aiFinancialModel", default=None
    )
    """AI's detailed financial model analysis."""

    ai_market_analysis: Optional[PitchRetrieveDetailsResponseAIMarketAnalysis] = FieldInfo(
        alias="aiMarketAnalysis", default=None
    )
    """AI's detailed market analysis."""

    ai_risk_assessment: Optional[PitchRetrieveDetailsResponseAIRiskAssessment] = FieldInfo(
        alias="aiRiskAssessment", default=None
    )
    """AI's assessment of risks associated with the venture."""

    investor_match_score: Optional[object] = FieldInfo(alias="investorMatchScore", default=None)
    """
    AI's score for how well the pitch matches potential investors in the network
    (0-1).
    """
