# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProductClaimOfferParams"]


class ProductClaimOfferParams(TypedDict, total=False):
    redemption_channel: Annotated[Literal["email", "in_app", "external_link"], PropertyInfo(alias="redemptionChannel")]
    """Preferred channel for offer redemption details."""
