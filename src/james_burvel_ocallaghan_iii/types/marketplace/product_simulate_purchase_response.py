# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["ProductSimulatePurchaseResponse", "KeyImpact", "ProjectedAmortizationSchedule"]


class KeyImpact(BaseModel):
    metric: Optional[str] = None

    severity: Optional[Literal["low", "medium", "high"]] = None

    value: Optional[str] = None


class ProjectedAmortizationSchedule(BaseModel):
    interest: Optional[float] = None

    month: Optional[int] = None

    payment: Optional[float] = None

    principal: Optional[float] = None

    remaining_balance: Optional[float] = FieldInfo(alias="remainingBalance", default=None)


class ProductSimulatePurchaseResponse(BaseModel):
    key_impacts: List[KeyImpact] = FieldInfo(alias="keyImpacts")
    """
    Key financial impacts identified by the AI (e.g., on cash flow, debt-to-income).
    """

    narrative_summary: str = FieldInfo(alias="narrativeSummary")
    """A natural language summary of the simulation's results for this product."""

    product_id: str = FieldInfo(alias="productId")
    """The ID of the marketplace product being simulated."""

    simulation_id: str = FieldInfo(alias="simulationId")
    """Unique identifier for the simulation performed."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """Actionable recommendations or advice related to the product and its impact."""

    projected_amortization_schedule: Optional[List[ProjectedAmortizationSchedule]] = FieldInfo(
        alias="projectedAmortizationSchedule", default=None
    )
    """Projected amortization schedule for loan products."""
