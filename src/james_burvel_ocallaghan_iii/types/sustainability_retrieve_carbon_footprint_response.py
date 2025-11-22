# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transactions.ai_insight import AIInsight

__all__ = ["SustainabilityRetrieveCarbonFootprintResponse", "BreakdownByCategory", "OffsetRecommendation"]


class BreakdownByCategory(BaseModel):
    carbon_footprint_kg_co2e: float = FieldInfo(alias="carbonFootprintKgCO2e")
    """Carbon footprint for this category in Kg CO2e."""

    category: str
    """Name of the spending category."""

    percentage: float
    """Percentage of the total carbon footprint for this category."""


class OffsetRecommendation(BaseModel):
    cost_per_ton_usd: float = FieldInfo(alias="costPerTonUSD")
    """Cost per ton of CO2e offset in USD."""

    offset_amount_kg_co2e: float = FieldInfo(alias="offsetAmountKgCO2e")
    """Amount of CO2e to offset (e.g., matching user's footprint)."""

    project: str
    """Recommended carbon offset project name."""

    total_cost_usd: float = FieldInfo(alias="totalCostUSD")
    """Total estimated cost to purchase the recommended offset amount."""

    project_details_url: Optional[str] = FieldInfo(alias="projectDetailsUrl", default=None)
    """URL for more information about the project."""


class SustainabilityRetrieveCarbonFootprintResponse(BaseModel):
    ai_insights: List[AIInsight] = FieldInfo(alias="aiInsights")
    """AI-generated insights and recommendations for reducing carbon footprint."""

    breakdown_by_category: List[BreakdownByCategory] = FieldInfo(alias="breakdownByCategory")
    """Breakdown of the carbon footprint by category (e.g., transportation, food)."""

    period: str
    """The period covered by the report."""

    report_id: str = FieldInfo(alias="reportId")
    """Unique identifier for the carbon footprint report."""

    total_carbon_footprint_kg_co2e: float = FieldInfo(alias="totalCarbonFootprintKgCO2e")
    """Total estimated carbon footprint in kilograms of CO2 equivalent."""

    offset_recommendations: Optional[List[OffsetRecommendation]] = FieldInfo(
        alias="offsetRecommendations", default=None
    )
    """Suggestions for carbon offset projects."""
