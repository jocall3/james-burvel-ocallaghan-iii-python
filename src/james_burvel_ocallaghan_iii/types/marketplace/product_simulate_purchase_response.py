# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel
from ..transactions.ai_insight import AIInsight

__all__ = ["ProductSimulatePurchaseResponse", "KeyImpact"]


class KeyImpact(BaseModel):
    metric: str
    """The financial metric being impacted."""

    value: str
    """The projected value or range for the metric."""

    severity: Optional[Literal["low", "medium", "high"]] = None
    """The severity of the impact (e.g., positive or negative significant change)."""


class ProductSimulatePurchaseResponse(BaseModel):
    key_impacts: List[KeyImpact] = FieldInfo(alias="keyImpacts")
    """Key financial metrics and their projected impact."""

    product_id: str = FieldInfo(alias="productId")
    """The ID of the product for which the simulation was run."""

    purchase_option: Literal["full_payment", "financed_12_months", "financed_24_months"] = FieldInfo(
        alias="purchaseOption"
    )
    """The payment option simulated."""

    simulation_summary: str = FieldInfo(alias="simulationSummary")
    """A narrative summary of the financial impact."""

    ai_recommendations: Optional[List[AIInsight]] = FieldInfo(alias="aiRecommendations", default=None)
    """AI-generated recommendations or insights based on the purchase simulation."""
