# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetUpdateParams", "Category"]


class BudgetUpdateParams(TypedDict, total=False):
    alert_threshold: Annotated[Optional[int], PropertyInfo(alias="alertThreshold")]
    """Updated percentage threshold for alerts."""

    categories: Iterable[Category]
    """Updated breakdown of the budget by categories.

    Existing categories not provided will remain unchanged.
    """

    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """Updated end date of the budget period."""

    name: str
    """Updated name of the budget."""

    period: Literal["weekly", "bi_weekly", "monthly", "quarterly", "annually", "custom"]
    """Updated recurrence period of the budget."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Updated start date of the budget period."""

    status: Literal["active", "completed", "upcoming", "archived"]
    """Updated status of the budget."""

    total_amount: Annotated[float, PropertyInfo(alias="totalAmount")]
    """Updated total allocated amount for the budget."""


class Category(TypedDict, total=False):
    allocated: float

    name: str
