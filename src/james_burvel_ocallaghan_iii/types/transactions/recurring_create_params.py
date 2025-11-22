# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecurringCreateParams"]


class RecurringCreateParams(TypedDict, total=False):
    amount: Required[float]
    """Amount of each recurring payment."""

    category: Required[str]
    """Category of the new recurring transaction."""

    currency: Required[str]
    """Currency of the recurring transaction."""

    description: Required[str]
    """Description of the new recurring transaction."""

    frequency: Required[Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]]
    """Frequency of the recurring transaction."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The date the first payment is expected or scheduled."""

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """Optional: The account to associate with this recurring transaction."""
