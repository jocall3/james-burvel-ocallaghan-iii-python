# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from datetime import date, datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["FinancialGoal", "AIStrategicPlan", "AIStrategicPlanStep"]


class AIStrategicPlanStep(BaseModel):
    description: Optional[str] = None

    linked_action_id: Optional[str] = FieldInfo(alias="linkedActionId", default=None)
    """ID of a related action (e.g., auto-transfer setup)."""

    priority: Optional[Literal["low", "medium", "high"]] = None

    status: Optional[Literal["pending", "in_progress", "completed"]] = None

    target_amount: Optional[float] = FieldInfo(alias="targetAmount", default=None)

    timeline: Optional[str] = None

    title: Optional[str] = None


class AIStrategicPlan(BaseModel):
    steps: Optional[List[AIStrategicPlanStep]] = None

    summary: Optional[str] = None

    title: Optional[str] = None


class FinancialGoal(BaseModel):
    id: str
    """Unique identifier for the financial goal."""

    current_amount: float = FieldInfo(alias="currentAmount")
    """Current amount accumulated towards the goal."""

    last_updated: datetime = FieldInfo(alias="lastUpdated")
    """Timestamp when the goal status or associated plan was last updated."""

    name: str
    """Name of the financial goal."""

    progress_percentage: float = FieldInfo(alias="progressPercentage")
    """Percentage of the target amount achieved."""

    risk_tolerance: Literal["conservative", "moderate", "balanced", "aggressive", "very_aggressive"] = FieldInfo(
        alias="riskTolerance"
    )
    """Risk tolerance associated with investments for this goal."""

    status: Literal["on_track", "ahead_of_schedule", "behind_schedule", "completed", "cancelled"]
    """Current status of the goal's progress."""

    target_amount: float = FieldInfo(alias="targetAmount")
    """The target amount for the goal."""

    target_date: date = FieldInfo(alias="targetDate")
    """Target completion date for the goal."""

    type: Literal[
        "retirement", "home_purchase", "education", "large_purchase", "debt_reduction", "wealth_creation", "other"
    ]
    """Type of financial goal."""

    ai_strategic_plan: Optional[AIStrategicPlan] = FieldInfo(alias="aiStrategicPlan", default=None)
    """AI-generated strategic plan with actionable steps to achieve the goal."""

    contributing_accounts: Optional[List[str]] = FieldInfo(alias="contributingAccounts", default=None)
    """List of account IDs contributing to this goal."""
