# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionCategorizeParams"]


class TransactionCategorizeParams(TypedDict, total=False):
    category: Required[str]
    """The new category for the transaction (can be hierarchical)."""

    apply_to_future: Annotated[bool, PropertyInfo(alias="applyToFuture")]
    """
    If true, the AI should learn and apply this categorization to similar future
    transactions.
    """

    notes: Optional[str]
    """Optional notes to add to the transaction."""
