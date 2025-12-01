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

    url: Optional[str] = None


class PitchRetrieveDetailsResponseAICoachingPlanStep(BaseModel):
    description: Optional[str] = None

    resources: Optional[List[PitchRetrieveDetailsResponseAICoachingPlanStepResource]] = None

    status: Optional[Literal["pending", "in_progress", "completed"]] = None

    timeline: Optional[str] = None

    title: Optional[str] = None


class PitchRetrieveDetailsResponseAICoachingPlan(BaseModel):
    steps: Optional[List[PitchRetrieveDetailsResponseAICoachingPlanStep]] = None

    summary: Optional[str] = None

    title: Optional[str] = None


class PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis(BaseModel):
    projected_irr: Optional[float] = FieldInfo(alias="projectedIRR", default=None)

    scenario: Optional[str] = None

    terminal_value: Optional[float] = FieldInfo(alias="terminalValue", default=None)


class PitchRetrieveDetailsResponseAIFinancialModel(BaseModel):
    breakeven_point: Optional[str] = FieldInfo(alias="breakevenPoint", default=None)

    capital_requirements: Optional[float] = FieldInfo(alias="capitalRequirements", default=None)

    cost_structure_analysis: Optional[Dict[str, str]] = FieldInfo(alias="costStructureAnalysis", default=None)

    revenue_breakdown: Optional[Dict[str, str]] = FieldInfo(alias="revenueBreakdown", default=None)

    sensitivity_analysis: Optional[List[PitchRetrieveDetailsResponseAIFinancialModelSensitivityAnalysis]] = FieldInfo(
        alias="sensitivityAnalysis", default=None
    )


class PitchRetrieveDetailsResponseAIMarketAnalysis(BaseModel):
    competitive_advantages: Optional[List[str]] = FieldInfo(alias="competitiveAdvantages", default=None)

    growth_opportunities: Optional[str] = FieldInfo(alias="growthOpportunities", default=None)

    risk_factors: Optional[str] = FieldInfo(alias="riskFactors", default=None)

    target_market_size: Optional[str] = FieldInfo(alias="targetMarketSize", default=None)


class PitchRetrieveDetailsResponseAIRiskAssessment(BaseModel):
    market_risk: Optional[str] = FieldInfo(alias="marketRisk", default=None)

    team_risk: Optional[str] = FieldInfo(alias="teamRisk", default=None)

    technical_risk: Optional[str] = FieldInfo(alias="technicalRisk", default=None)


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

    investor_match_score: Optional[float] = FieldInfo(alias="investorMatchScore", default=None)
    """
    AI's score for how well the pitch matches potential investors in the network
    (0-1).
    """
