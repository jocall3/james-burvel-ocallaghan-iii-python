# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List
from typing_extensions import TypeAlias

from .financial_goal import FinancialGoal

__all__ = ["GoalListResponse"]

GoalListResponse: TypeAlias = List[FinancialGoal]
