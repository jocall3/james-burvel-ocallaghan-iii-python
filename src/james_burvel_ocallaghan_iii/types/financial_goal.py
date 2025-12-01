# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel
from .transactions.ai_insight import AIInsight

__all__ = ["FinancialGoal", "AIStrategicPlan", "AIStrategicPlanStep"]


class AIStrategicPlanStep(BaseModel):
    description: Optional[object] = None

    status: Optional[Literal["pending", "in_progress", "completed"]] = None

    title: Optional[object] = None


class AIStrategicPlan(BaseModel):
    plan_id: Optional[object] = FieldInfo(alias="planId", default=None)

    steps: Optional[List[AIStrategicPlanStep]] = None

    summary: Optional[object] = None


class FinancialGoal(BaseModel):
    id: object
    """Unique identifier for the financial goal."""

    current_amount: object = FieldInfo(alias="currentAmount")
    """The current amount saved or invested towards the goal."""

    last_updated: object = FieldInfo(alias="lastUpdated")
    """Timestamp when the goal's status or progress was last updated."""

    name: object
    """Name of the financial goal."""

    progress_percentage: object = FieldInfo(alias="progressPercentage")
    """Percentage completion of the goal."""

    status: Literal["on_track", "behind_schedule", "ahead_of_schedule", "completed", "paused", "cancelled"]
    """Current status of the goal's progress."""

    target_amount: object = FieldInfo(alias="targetAmount")
    """The target monetary amount for the goal."""

    target_date: object = FieldInfo(alias="targetDate")
    """The target completion date for the goal."""

    type: Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "other"]
    """Type of financial goal."""

    ai_insights: Optional[List[AIInsight]] = FieldInfo(alias="aiInsights", default=None)
    """AI-driven insights and recommendations related to this goal."""

    ai_strategic_plan: Optional[AIStrategicPlan] = FieldInfo(alias="aiStrategicPlan", default=None)
    """AI-generated strategic plan for achieving the goal."""

    contributing_accounts: Optional[List[object]] = FieldInfo(alias="contributingAccounts", default=None)
    """List of account IDs contributing to this goal."""

    risk_tolerance: Optional[Literal["conservative", "moderate", "aggressive"]] = FieldInfo(
        alias="riskTolerance", default=None
    )
    """Recommended or chosen risk tolerance for investments related to this goal."""
