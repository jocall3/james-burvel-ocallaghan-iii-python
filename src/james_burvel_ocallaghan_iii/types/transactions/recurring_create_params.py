# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecurringCreateParams"]


class RecurringCreateParams(TypedDict, total=False):
    amount: Required[float]
    """Amount of the recurring transaction."""

    category: Required[str]
    """Category of the recurring transaction."""

    currency: Required[str]
    """ISO 4217 currency code."""

    description: Required[str]
    """Description of the recurring transaction."""

    frequency: Required[Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]]
    """Frequency of the recurring transaction."""

    linked_account_id: Required[Annotated[str, PropertyInfo(alias="linkedAccountId")]]
    """ID of the account to associate with this recurring transaction."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The date when this recurring transaction is expected to start."""
