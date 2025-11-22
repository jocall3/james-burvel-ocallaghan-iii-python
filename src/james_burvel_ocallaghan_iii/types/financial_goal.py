# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinancialGoal", "AIStrategicPlan", "AIStrategicPlanStep"]


class AIStrategicPlanStep(BaseModel):
    description: str
    """Detailed description of the action."""

    status: Literal["pending", "in_progress", "completed", "deferred"]
    """Current status of the step."""

    timeline: str
    """Suggested timeline for completion (e.g., 'Immediately', 'Quarterly')."""

    title: str
    """Title of the step."""

    associated_action_id: Optional[str] = FieldInfo(alias="associatedActionId", default=None)
    """Optional: ID of a related action (e.g., an automated transfer setup)."""


class AIStrategicPlan(BaseModel):
    steps: List[AIStrategicPlanStep]
    """Detailed, actionable steps for achieving the goal."""

    summary: str
    """Summary of the strategic plan."""

    title: str
    """Title of the strategic plan."""

    ai_optimized: Optional[bool] = FieldInfo(alias="aiOptimized", default=None)
    """Indicates if the plan was optimized by AI."""

    last_generated: Optional[datetime] = FieldInfo(alias="lastGenerated", default=None)
    """Timestamp when this plan was last generated or updated."""


class FinancialGoal(BaseModel):
    id: str
    """Unique identifier for the financial goal."""

    current_amount: float = FieldInfo(alias="currentAmount")
    """The current amount accumulated towards the goal."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the goal's status or details were last updated."""

    name: str
    """Name of the financial goal."""

    progress_percentage: float = FieldInfo(alias="progressPercentage")
    """Current progress towards the goal as a percentage."""

    risk_tolerance: Literal["conservative", "balanced", "medium", "aggressive", "speculative"] = FieldInfo(
        alias="riskTolerance"
    )
    """Risk tolerance associated with investments for this goal."""

    status: Literal["on_track", "behind_schedule", "ahead_of_schedule", "completed", "paused"]
    """Current status of the goal's progress."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """The target amount to save or achieve for this goal."""

    target_date: date = FieldInfo(alias="targetDate")
    """The target date by which the goal should be achieved."""

    type: Literal["retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "custom"]
    """Type of financial goal."""

    ai_strategic_plan: Optional[AIStrategicPlan] = FieldInfo(alias="aiStrategicPlan", default=None)
    """AI-generated strategic plan to achieve the goal."""

    contributing_accounts: Optional[List[str]] = FieldInfo(alias="contributingAccounts", default=None)
    """List of account IDs contributing to this goal."""

    monthly_contribution_needed: Optional[float] = FieldInfo(alias="monthlyContributionNeeded", default=None)
    """AI's calculated monthly contribution needed to reach the goal."""
