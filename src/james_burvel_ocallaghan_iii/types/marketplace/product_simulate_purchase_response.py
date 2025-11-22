# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["ProductSimulatePurchaseResponse", "KeyImpact"]


class KeyImpact(BaseModel):
    metric: Optional[str] = None

    severity: Optional[Literal["low", "medium", "high"]] = None

    value: Optional[str] = None


class ProductSimulatePurchaseResponse(BaseModel):
    ai_recommendations: List[AIInsight] = FieldInfo(alias="aiRecommendations")
    """AI-driven recommendations based on the simulation results."""

    key_impacts: List[KeyImpact] = FieldInfo(alias="keyImpacts")
    """Key financial metrics and their projected impact."""

    product_id: str = FieldInfo(alias="productId")
    """The ID of the product for which the simulation was run."""

    purchase_option: Literal["full_payment", "financed_12_months", "financed_24_months"] = FieldInfo(
        alias="purchaseOption"
    )
    """The purchase option that was simulated."""

    simulation_summary: str = FieldInfo(alias="simulationSummary")
    """A natural language summary of the simulation results."""
