# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Required, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetCreateParams", "Category"]


class BudgetCreateParams(TypedDict, total=False):
    end_date: Required[Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]]
    """End date of the budget period."""

    name: Required[str]
    """Name of the new budget."""

    period: Required[Literal["weekly", "bi_weekly", "monthly", "quarterly", "annually", "custom"]]
    """The frequency or period of the budget."""

    start_date: Required[Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]]
    """Start date of the budget period."""

    total_amount: Required[Annotated[float, PropertyInfo(alias="totalAmount")]]
    """Total amount allocated for the entire budget."""

    ai_auto_populate: Annotated[bool, PropertyInfo(alias="aiAutoPopulate")]
    """
    If true, AI will automatically populate categories and amounts based on
    historical spending.
    """

    alert_threshold: Annotated[int, PropertyInfo(alias="alertThreshold")]
    """Percentage threshold at which an alert is triggered."""

    categories: Iterable[Category]
    """Initial breakdown of the budget by categories."""


class Category(TypedDict, total=False):
    allocated: float

    name: str
