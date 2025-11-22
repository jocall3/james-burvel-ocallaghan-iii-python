# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["ProductSimulatePurchaseParams"]


class ProductSimulatePurchaseParams(TypedDict, total=False):
    purchase_option: Required[
        Annotated[
            Literal["full_payment", "financed_12_months", "financed_24_months"], PropertyInfo(alias="purchaseOption")
        ]
    ]
    """The payment method to simulate."""

    target_account_id: Annotated[Optional[str], PropertyInfo(alias="targetAccountId")]
    """Optional: The account from which the purchase would be made.

    If omitted, AI will infer.
    """
