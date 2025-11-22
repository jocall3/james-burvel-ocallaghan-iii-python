# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["RecurringCreateParams"]


class RecurringCreateParams(TypedDict, total=False):
    amount: Required[float]
    """The amount of each recurring transaction."""

    category: Required[str]
    """Category of the recurring transaction."""

    currency: Required[str]
    """The currency of the recurring transaction."""

    description: Required[str]
    """Description of the new recurring transaction."""

    frequency: Required[Literal["daily", "weekly", "bi-weekly", "monthly", "quarterly", "annually"]]
    """How often the transaction occurs."""

    linked_account_id: Required[Annotated[str, PropertyInfo(alias="linkedAccountId")]]
    """The ID of the account from which this recurring transaction typically occurs."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The date the recurring transaction is expected to start."""

    status: Literal["active", "paused"]
    """Initial status of the recurring transaction."""
