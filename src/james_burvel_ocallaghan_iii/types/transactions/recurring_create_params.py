# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecurringCreateParams"]


class RecurringCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The expected amount of the recurring transaction."""

    category: Required[str]
    """Category of the recurring transaction."""

    currency: Required[str]
    """The currency of the transaction (ISO 4217 code)."""

    description: Required[str]
    """Description for the new recurring transaction."""

    frequency: Required[Literal["daily", "weekly", "bi_weekly", "monthly", "quarterly", "semi_annually", "annually"]]
    """How often the transaction is expected to occur."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The date the first recurring transaction is expected."""

    linked_account_id: Annotated[Optional[str], PropertyInfo(alias="linkedAccountId")]
    """
    Optional: The account from which this recurring transaction will be paid or
    received.
    """
