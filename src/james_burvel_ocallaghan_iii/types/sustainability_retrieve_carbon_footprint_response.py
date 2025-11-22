# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transactions.ai_insight import AIInsight

__all__ = ["SustainabilityRetrieveCarbonFootprintResponse", "BreakdownByCategory", "OffsetRecommendation"]


class BreakdownByCategory(BaseModel):
    carbon_footprint_kg_co2e: Optional[float] = FieldInfo(alias="carbonFootprintKgCO2e", default=None)

    category: Optional[str] = None

    percentage: Optional[float] = None


class OffsetRecommendation(BaseModel):
    cost_per_ton_usd: Optional[float] = FieldInfo(alias="costPerTonUSD", default=None)

    offset_amount_kg_co2e: Optional[float] = FieldInfo(alias="offsetAmountKgCO2e", default=None)

    project: Optional[str] = None

    total_cost_usd: Optional[float] = FieldInfo(alias="totalCostUSD", default=None)


class SustainabilityRetrieveCarbonFootprintResponse(BaseModel):
    ai_insights: List[AIInsight] = FieldInfo(alias="aiInsights")
    """AI-generated insights and recommendations for reducing carbon footprint."""

    breakdown_by_category: List[BreakdownByCategory] = FieldInfo(alias="breakdownByCategory")
    """
    Breakdown of the carbon footprint by categories (e.g., Transportation, Food,
    Housing).
    """

    period: str
    """The time period covered by the report."""

    report_id: str = FieldInfo(alias="reportId")
    """Unique identifier for the carbon footprint report."""

    total_carbon_footprint_kg_co2e: float = FieldInfo(alias="totalCarbonFootprintKgCO2e")
    """Total estimated carbon footprint in kilograms of CO2 equivalent."""

    offset_recommendations: Optional[List[OffsetRecommendation]] = FieldInfo(
        alias="offsetRecommendations", default=None
    )
    """Recommendations for purchasing carbon offsets."""
