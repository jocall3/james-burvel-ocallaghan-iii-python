# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["ProductListResponse", "Data", "DataOfferDetails"]


class DataOfferDetails(BaseModel):
    code: Optional[object] = None
    """Optional redemption code."""

    type: Optional[Literal["discount", "special_rate", "free_trial"]] = None

    value: Optional[object] = None


class Data(BaseModel):
    id: object
    """Unique identifier for the marketplace product."""

    ai_personalization_score: object = FieldInfo(alias="aiPersonalizationScore")
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

    description: object
    """Detailed description of the product/service."""

    image_url: object = FieldInfo(alias="imageUrl")
    """URL to an image representing the product."""

    name: object
    """Name of the product/service."""

    price: object
    """Pricing information (can be a range or fixed text)."""

    provider: object
    """Provider or vendor of the product/service."""

    rating: object
    """Average user rating for the product (0-5)."""

    ai_recommendation_reason: Optional[object] = FieldInfo(alias="aiRecommendationReason", default=None)
    """AI-generated explanation for recommending this product."""

    offer_details: Optional[DataOfferDetails] = FieldInfo(alias="offerDetails", default=None)
    """Details of any special offers associated with the product."""

    product_url: Optional[object] = FieldInfo(alias="productUrl", default=None)
    """Direct URL to the product on the provider's website."""


class ProductListResponse(BaseModel):
    limit: object
    """The maximum number of items returned in the current page."""

    offset: object
    """The number of items skipped before the current page."""

    total: object
    """The total number of items available across all pages."""

    data: Optional[List[Data]] = None

    next_offset: Optional[object] = FieldInfo(alias="nextOffset", default=None)
    """The offset for the next page of results, if available. Null if no more pages."""
