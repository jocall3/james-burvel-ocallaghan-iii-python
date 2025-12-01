# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AIInsight"]


class AIInsight(BaseModel):
    id: object
    """Unique identifier for the AI insight."""

    category: Literal[
        "spending",
        "saving",
        "investing",
        "budgeting",
        "security",
        "financial_goals",
        "sustainability",
        "corporate_treasury",
        "compliance",
        "other",
    ]
    """Category of the insight (e.g., spending, saving, investing)."""

    description: object
    """Detailed explanation of the insight."""

    severity: Literal["low", "medium", "high", "critical"]
    """AI-assessed severity or importance of the insight."""

    timestamp: object
    """Timestamp when the insight was generated."""

    title: object
    """A concise title for the insight."""

    actionable_recommendation: Optional[object] = FieldInfo(alias="actionableRecommendation", default=None)
    """Optional: A concrete action the user can take based on the insight."""

    action_trigger: Optional[object] = FieldInfo(alias="actionTrigger", default=None)
    """
    Optional: A programmatic trigger or deep link to initiate the recommended
    action.
    """
