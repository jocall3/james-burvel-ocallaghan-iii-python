# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["TransactionCategorizeParams"]


class TransactionCategorizeParams(TypedDict, total=False):
    category: Required[object]
    """The new category for the transaction. Can be hierarchical."""

    apply_to_future: Annotated[object, PropertyInfo(alias="applyToFuture")]
    """
    If true, the AI will learn from this correction and try to apply it to similar
    future transactions.
    """

    notes: object
    """Optional notes to add to the transaction."""
