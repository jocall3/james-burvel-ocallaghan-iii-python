# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetUpdateParams", "Category"]


class BudgetUpdateParams(TypedDict, total=False):
    alert_threshold: Annotated[Optional[int], PropertyInfo(alias="alertThreshold")]
    """Updated percentage for budget alert threshold."""

    categories: Iterable[Category]
    """Updated breakdown of the budget by categories.

    Existing categories will be updated, new ones added.
    """

    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """Updated end date of the budget period."""

    name: str
    """Updated name of the budget."""

    period: Literal["weekly", "monthly", "quarterly", "annually", "custom"]
    """Updated recurrence period of the budget."""

    reset_spent_amounts: Annotated[bool, PropertyInfo(alias="resetSpentAmounts")]
    """If true, resets `spentAmount` for all categories and total to 0.

    Useful for starting a new cycle of a recurring budget.
    """

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Updated start date of the budget period."""

    status: Literal["active", "completed", "archived", "overspent"]
    """Updated status of the budget."""

    total_amount: Annotated[float, PropertyInfo(alias="totalAmount")]
    """Updated total allocated budget amount."""


class Category(TypedDict, total=False):
    allocated: Required[float]
    """Amount allocated to this category."""

    name: Required[str]
    """Category name."""
