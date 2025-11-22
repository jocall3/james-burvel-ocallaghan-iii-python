# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable, Optional
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetCreateParams", "Category"]


class BudgetCreateParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """End date of the budget period."""

    name: Required[str]
    """Name for the new budget."""

    period: Required[Literal["weekly", "bi_weekly", "monthly", "quarterly", "annually", "custom"]]
    """Recurrence period of the budget."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """Start date of the budget period."""

    total_amount: Required[Annotated[float, PropertyInfo(alias="totalAmount")]]
    """Total allocated amount for the budget."""

    ai_auto_populate: Annotated[bool, PropertyInfo(alias="aiAutoPopulate")]
    """
    If true, AI will automatically suggest and fill in budget categories and amounts
    based on spending history.
    """

    alert_threshold: Annotated[Optional[int], PropertyInfo(alias="alertThreshold")]
    """Percentage threshold at which an alert is triggered."""

    categories: Iterable[Category]
    """
    Initial breakdown of the budget by categories (can be partially defined for AI
    auto-population).
    """


class Category(TypedDict, total=False):
    allocated: float

    name: str
