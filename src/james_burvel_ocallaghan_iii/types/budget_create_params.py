# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetCreateParams", "Category"]


class BudgetCreateParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """The end date of the budget period."""

    name: Required[str]
    """Name of the new budget."""

    period: Required[Literal["weekly", "monthly", "quarterly", "annually", "custom"]]
    """The recurrence period of the budget."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The start date of the budget period."""

    total_amount: Required[Annotated[float, PropertyInfo(alias="totalAmount")]]
    """The total amount allocated for the budget."""

    ai_auto_populate: Annotated[bool, PropertyInfo(alias="aiAutoPopulate")]
    """
    If true, AI will automatically suggest and populate budget categories and
    amounts based on historical spending.
    """

    alert_threshold: Annotated[Optional[int], PropertyInfo(alias="alertThreshold")]
    """Percentage of budget spent at which an alert should be triggered."""

    categories: Optional[Iterable[Category]]
    """Optional: Initial breakdown of the budget by categories.

    If omitted and `aiAutoPopulate` is true, AI will generate.
    """


class Category(TypedDict, total=False):
    allocated: Required[float]
    """Amount allocated to this category."""

    name: Required[str]
    """Category name."""
