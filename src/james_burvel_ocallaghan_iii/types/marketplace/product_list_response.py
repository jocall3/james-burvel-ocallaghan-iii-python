# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductListResponse", "Data", "DataOfferDetails"]


class DataOfferDetails(BaseModel):
    code: Optional[str] = None
    """Optional redemption code."""

    type: Optional[Literal["discount", "special_rate", "free_trial"]] = None

    value: Optional[str] = None


class Data(BaseModel):
    id: str
    """Unique identifier for the marketplace product."""

    ai_personalization_score: float = FieldInfo(alias="aiPersonalizationScore")
    """AI's score for how well this product is personalized to the user (0-1)."""

    category: Literal[
        "loans",
        "insurance",
        "credit_cards",
        "investments",
        "budgeting_tools",
        "smart_home",
        "travel",
        "education",
        "health",
    ]
    """Category of the product/service."""

    description: str
    """Detailed description of the product/service."""

    image_url: Optional[str] = FieldInfo(alias="imageUrl", default=None)
    """URL to an image representing the product."""

    name: str
    """Name of the product/service."""

    price: str
    """Pricing information (can be a range or fixed text)."""

    provider: str
    """Provider or vendor of the product/service."""

    rating: float
    """Average user rating for the product (0-5)."""

    ai_recommendation_reason: Optional[str] = FieldInfo(alias="aiRecommendationReason", default=None)
    """AI-generated explanation for recommending this product."""

    offer_details: Optional[DataOfferDetails] = FieldInfo(alias="offerDetails", default=None)
    """Details of any special offers associated with the product."""

    product_url: Optional[str] = FieldInfo(alias="productUrl", default=None)
    """Direct URL to the product on the provider's website."""


class ProductListResponse(BaseModel):
    limit: int
    """The maximum number of items returned in the current page."""

    offset: int
    """The number of items skipped before the current page."""

    total: int
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[int] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
