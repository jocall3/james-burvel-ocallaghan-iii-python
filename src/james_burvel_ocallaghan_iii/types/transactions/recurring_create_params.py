# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecurringCreateParams"]


class RecurringCreateParams(TypedDict, total=False):
    amount: Required[object]
    """Amount of the recurring transaction."""

    category: Required[object]
    """Category of the recurring transaction."""

    currency: Required[object]
    """ISO 4217 currency code."""

    description: Required[object]
    """Description of the recurring transaction."""

    frequency: Required[Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]]
    """Frequency of the recurring transaction."""

    linked_account_id: Required[Annotated[object, PropertyInfo(alias="linkedAccountId")]]
    """ID of the account to associate with this recurring transaction."""

    start_date: Required[Annotated[object, PropertyInfo(alias="startDate")]]
    """The date when this recurring transaction is expected to start."""
