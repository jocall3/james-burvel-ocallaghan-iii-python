# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Union, Iterable
from datetime import date
from typing_extensions import Literal, Annotated, TypedDict

from .._utils import PropertyInfo

__all__ = ["BudgetUpdateParams", "Category"]


class BudgetUpdateParams(TypedDict, total=False):
    alert_threshold: Annotated[int, PropertyInfo(alias="alertThreshold")]
    """Updated percentage threshold for alerts."""

    categories: Iterable[Category]
    """Updated breakdown of the budget by categories.

    Existing categories will be updated, new ones added.
    """

    end_date: Annotated[Union[str, date], PropertyInfo(alias="endDate", format="iso8601")]
    """Updated end date of the budget period."""

    name: str
    """Updated name of the budget."""

    start_date: Annotated[Union[str, date], PropertyInfo(alias="startDate", format="iso8601")]
    """Updated start date of the budget period."""

    status: Literal["active", "archived", "ended"]
    """Updated status of the budget."""

    total_amount: Annotated[float, PropertyInfo(alias="totalAmount")]
    """Updated total amount for the entire budget."""


class Category(TypedDict, total=False):
    allocated: float

    name: str
