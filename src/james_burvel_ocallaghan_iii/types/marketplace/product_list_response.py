# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import datetime
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

    discount_percentage: Optional[float] = FieldInfo(alias="discountPercentage", default=None)

    expires_at: Optional[datetime] = FieldInfo(alias="expiresAt", default=None)


class ProductListResponseItem(BaseModel):
    id: str
    """Unique identifier for the marketplace product."""

    ai_recommendation_score: float = FieldInfo(alias="aiRecommendationScore")
    """AI's personalized recommendation score for the user (0-1)."""

    category: str
    """Category of the product."""

    currency: str
    """Currency of the product price."""

    description: str
    """Detailed description of the product."""

    image_url: str = FieldInfo(alias="imageUrl")
    """URL to the product's image."""

    name: str
    """Name of the product."""

    personalization_reason: str = FieldInfo(alias="personalizationReason")
    """AI-generated explanation for why this product is recommended."""

    price: float
    """Price of the product."""

    vendor: str
    """Name of the product vendor or manufacturer."""

    estimated_impact_on_budget: Optional[ProductListResponseItemEstimatedImpactOnBudget] = FieldInfo(
        alias="estimatedImpactOnBudget", default=None
    )
    """AI's estimated financial impact if the user purchases this product."""

    exclusive_offer: Optional[ProductListResponseItemExclusiveOffer] = FieldInfo(alias="exclusiveOffer", default=None)
    """Details of any exclusive offer available for this product."""

    product_url: Optional[str] = FieldInfo(alias="productUrl", default=None)
    """Direct URL to the product page."""


ProductListResponse: TypeAlias = List[ProductListResponseItem]
