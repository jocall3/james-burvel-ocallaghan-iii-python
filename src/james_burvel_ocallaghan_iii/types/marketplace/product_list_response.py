# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = [
    "ProductListResponse",
    "ProductListResponseItem",
    "ProductListResponseItemEstimatedImpactOnBudget",
    "ProductListResponseItemOfferDetails",
]


class ProductListResponseItemEstimatedImpactOnBudget(BaseModel):
    monthly_cost: Optional[float] = FieldInfo(alias="monthlyCost", default=None)
    """Estimated monthly cost from this product (e.g., financing)."""

    monthly_savings: Optional[float] = FieldInfo(alias="monthlySavings", default=None)
    """Estimated monthly savings from this product (if applicable)."""

    overall_budget_impact: Optional[Literal["positive", "neutral", "negative"]] = FieldInfo(
        alias="overallBudgetImpact", default=None
    )
    """Overall impact on user's budget."""

    payback_period_months: Optional[int] = FieldInfo(alias="paybackPeriodMonths", default=None)
    """Estimated number of months to recoup initial investment/cost."""


class ProductListResponseItemOfferDetails(BaseModel):
    discount_percentage: Optional[float] = FieldInfo(alias="discountPercentage", default=None)
    """Discount percentage."""

    offer_code: Optional[str] = FieldInfo(alias="offerCode", default=None)
    """Promotional code."""

    valid_until: Optional[date] = FieldInfo(alias="validUntil", default=None)
    """Offer valid until date."""


class ProductListResponseItem(BaseModel):
    id: str
    """Unique identifier for the marketplace product."""

    ai_recommendation_score: float = FieldInfo(alias="aiRecommendationScore")
    """AI's recommendation score (0-1) for this user."""

    category: str
    """Category of the product."""

    currency: str
    """Currency of the product price."""

    description: str
    """Description of the product."""

    image_url: str = FieldInfo(alias="imageUrl")
    """URL to the product image."""

    name: str
    """Name of the product."""

    personalization_reason: str = FieldInfo(alias="personalizationReason")
    """AI's explanation for why this product is recommended."""

    price: float
    """Price of the product."""

    vendor: str
    """Vendor or brand of the product."""

    estimated_impact_on_budget: Optional[ProductListResponseItemEstimatedImpactOnBudget] = FieldInfo(
        alias="estimatedImpactOnBudget", default=None
    )
    """AI's estimated financial impact of purchasing this product."""

    offer_details: Optional[ProductListResponseItemOfferDetails] = FieldInfo(alias="offerDetails", default=None)


ProductListResponse: TypeAlias = List[ProductListResponseItem]
