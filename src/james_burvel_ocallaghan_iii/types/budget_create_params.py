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
    """Name for the new budget."""

    period: Required[Literal["weekly", "monthly", "quarterly", "yearly", "custom"]]
    """The frequency or period of the budget."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """The start date of the budget period."""

    total_amount: Required[Annotated[float, PropertyInfo(alias="totalAmount")]]
    """The total amount allocated for the budget."""

    ai_auto_populate: Annotated[bool, PropertyInfo(alias="aiAutoPopulate")]
    """
    If true, AI will intelligently auto-populate remaining categories and amounts
    based on historical spending.
    """

    alert_threshold: Annotated[Optional[int], PropertyInfo(alias="alertThreshold")]
    """Percentage threshold for budget alerts."""

    categories: Iterable[Category]
    """Initial breakdown of the budget by categories."""


class Category(TypedDict, total=False):
    allocated: Required[float]

    name: Required[str]
