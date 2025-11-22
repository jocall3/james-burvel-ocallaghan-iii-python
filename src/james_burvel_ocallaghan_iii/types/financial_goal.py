# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transactions.ai_insight import AIInsight

__all__ = ["FinancialGoal", "AIStrategicPlan", "AIStrategicPlanStep"]


class AIStrategicPlanStep(BaseModel):
    description: Optional[str] = None

    status: Optional[Literal["pending", "in_progress", "completed"]] = None

    title: Optional[str] = None


class AIStrategicPlan(BaseModel):
    plan_id: Optional[str] = FieldInfo(alias="planId", default=None)

    steps: Optional[List[AIStrategicPlanStep]] = None

    summary: Optional[str] = None


class FinancialGoal(BaseModel):
    id: str
    """Unique identifier for the financial goal."""

    current_amount: float = FieldInfo(alias="currentAmount")
    """The current amount saved or invested towards the goal."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the goal's status or progress was last updated."""

    name: str
    """Name of the financial goal."""

    progress_percentage: float = FieldInfo(alias="progressPercentage")
    """Percentage completion of the goal."""

    status: Literal["on_track", "behind_schedule", "ahead_of_schedule", "completed", "paused", "cancelled"]
    """Current status of the goal's progress."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """The target monetary amount for the goal."""

    target_date: date = FieldInfo(alias="targetDate")
    """The target completion date for the goal."""

    type: Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "other"]
    """Type of financial goal."""

    ai_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiInsights", default=None)
    """AI-driven insights and recommendations related to this goal."""

    ai_strategic_plan: Optional[AIStrategicPlan] = FieldInfo(alias="aiStrategicPlan", default=None)
    """AI-generated strategic plan for achieving the goal."""

    contributing_accounts: Optional[List[str]] = FieldInfo(alias="contributingAccounts", default=None)
    """List of account IDs contributing to this goal."""

    risk_tolerance: Optional[Literal["conservative", "moderate", "aggressive"]] = FieldInfo(
        alias="riskTolerance", default=None
    )
    """Recommended or chosen risk tolerance for investments related to this goal."""
