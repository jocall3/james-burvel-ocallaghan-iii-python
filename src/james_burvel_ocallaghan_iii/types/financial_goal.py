# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinancialGoal", "AIStrategicPlan", "AIStrategicPlanStep"]


class AIStrategicPlanStep(BaseModel):
    action_trigger: Optional[str] = FieldInfo(alias="actionTrigger", default=None)

    description: Optional[str] = None

    status: Optional[Literal["pending", "in_progress", "completed", "overdue"]] = None

    timeline: Optional[str] = None

    title: Optional[str] = None


class AIStrategicPlan(BaseModel):
    steps: List[AIStrategicPlanStep]
    """Actionable steps to be taken as part of the plan."""

    summary: str
    """A summary of the strategic plan."""

    title: str
    """Title of the AI-generated strategic plan."""

    generated_on: Optional[datetime] = FieldInfo(alias="generatedOn", default=None)
    """Timestamp when the plan was generated/last updated."""


class FinancialGoal(BaseModel):
    id: str
    """Unique identifier for the financial goal."""

    current_amount: float = FieldInfo(alias="currentAmount")
    """The current amount saved or invested towards this goal."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the goal's status or details were last updated."""

    name: str
    """User-defined name for the goal."""

    progress_percentage: float = FieldInfo(alias="progressPercentage")
    """Current progress towards the goal in percentage."""

    risk_tolerance: Literal["low", "medium", "aggressive", "very_aggressive"] = FieldInfo(alias="riskTolerance")
    """The risk tolerance associated with the investment strategy for this goal."""

    status: Literal["on_track", "ahead_of_schedule", "behind_schedule", "achieved", "cancelled"]
    """Current status of the goal's progress."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """The target amount to achieve for this goal."""

    target_date: date = FieldInfo(alias="targetDate")
    """The target date for achieving the goal."""

    type: Literal[
        "retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "investment_growth", "other"
    ]
    """Type of financial goal."""

    ai_strategic_plan: Optional[AIStrategicPlan] = FieldInfo(alias="aiStrategicPlan", default=None)
    """AI-generated strategic plan to achieve the goal."""

    contributing_accounts: Optional[List[str]] = FieldInfo(alias="contributingAccounts", default=None)
    """List of account IDs contributing to this goal."""
