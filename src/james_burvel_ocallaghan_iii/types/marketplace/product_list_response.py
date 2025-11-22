# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ProductListResponse",
    "ProductListResponseItem",
    "ProductListResponseItemEstimatedImpactOnBudget",
    "ProductListResponseItemExclusiveOffer",
]


class ProductListResponseItemEstimatedImpactOnBudget(BaseModel):
    monthly_savings: Optional[float] = FieldInfo(alias="monthlySavings", default=None)

    payback_period_months: Optional[int] = FieldInfo(alias="paybackPeriodMonths", default=None)


class ProductListResponseItemExclusiveOffer(BaseModel):
    description: Optional[str] = None

    expires_date: Optional[date] = FieldInfo(alias="expiresDate", default=None)

    title: Optional[str] = None


class ProductListResponseItem(BaseModel):
    id: str
    """Unique identifier for the marketplace product."""

    ai_recommendation_score: float = FieldInfo(alias="aiRecommendationScore")
    """
    AI's recommendation score (0-1) indicating relevance and suitability for the
    user.
    """

    category: str
    """Category of the product (e.g., 'Smart Home Devices', 'Financial Education')."""

    currency: str
    """Currency of the product's price (ISO 4217 code)."""

    description: str
    """Detailed description of the product."""

    image_url: str = FieldInfo(alias="imageUrl")
    """URL to the product's main image."""

    name: str
    """Name of the product."""

    personalization_reason: str = FieldInfo(alias="personalizationReason")
    """AI-generated explanation of why this product is recommended to the user."""

    price: float
    """Current price of the product."""

    vendor: str
    """Name of the product vendor or brand."""

    estimated_impact_on_budget: Optional[ProductListResponseItemEstimatedImpactOnBudget] = FieldInfo(
        alias="estimatedImpactOnBudget", default=None
    )
    """AI-estimated financial impact of the product on the user's budget."""

    exclusive_offer: Optional[ProductListResponseItemExclusiveOffer] = FieldInfo(alias="exclusiveOffer", default=None)
    """Details of any exclusive offers available for this product."""


ProductListResponse: TypeAlias = List[ProductListResponseItem]
