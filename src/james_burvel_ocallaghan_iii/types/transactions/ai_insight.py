# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AIInsight"]


class AIInsight(BaseModel):
    id: str
    """Unique identifier for the AI insight."""

    actionable_recommendation: Optional[str] = FieldInfo(alias="actionableRecommendation", default=None)
    """A concrete, actionable recommendation based on the insight."""

    category: Literal[
        "spending",
        "saving",
        "investing",
        "budget",
        "compliance",
        "security",
        "sustainability",
        "corporate_treasury",
        "marketplace",
        "technology",
    ]
    """Category of the insight (e.g., spending, saving, security)."""

    description: str
    """Detailed description of the insight."""

    severity: Literal["low", "medium", "high", "critical"]
    """Severity level of the insight."""

    timestamp: datetime
    """Timestamp when the insight was generated."""

    title: str
    """Concise title of the insight."""

    action_trigger: Optional[str] = FieldInfo(alias="actionTrigger", default=None)
    """
    A programmatic identifier to trigger a specific action or navigate to a relevant
    feature.
    """
