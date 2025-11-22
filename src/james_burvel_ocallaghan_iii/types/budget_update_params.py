# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetUpdateParams", "Category"]


class BudgetUpdateParams(TypedDict, total=False):
    alert_threshold: Annotated[Optional[int], PropertyInfo(alias="alertThreshold")]
    """Updated percentage threshold for budget alerts."""

    categories: Iterable[Category]
    """Updated or new categories for the budget.

    Existing categories not included will remain unchanged unless explicitly set to
    null/0.
    """

    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """The updated end date of the budget period."""

    name: str
    """Updated name for the budget."""

    period: Literal["weekly", "monthly", "quarterly", "yearly", "custom"]
    """The updated frequency or period of the budget."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """The updated start date of the budget period."""

    total_amount: Annotated[float, PropertyInfo(alias="totalAmount")]
    """The updated total allocated budget amount."""


class Category(TypedDict, total=False):
    allocated: Required[float]

    name: Required[str]
