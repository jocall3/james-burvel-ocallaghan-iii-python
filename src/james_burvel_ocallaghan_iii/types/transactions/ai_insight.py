# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from datetime import datetime
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["AIInsight"]


class AIInsight(BaseModel):
    id: str
    """Unique identifier for the insight."""

    category: Literal[
        "spending",
        "saving",
        "investing",
        "budget",
        "security",
        "sustainability",
        "corporate_treasury",
        "marketplace",
        "compliance",
        "credit",
        "lending",
    ]
    """Category of the insight."""

    description: str
    """Detailed description of the insight."""

    severity: Literal["low", "medium", "high", "critical"]
    """Severity level of the insight."""

    timestamp: datetime
    """Timestamp when the insight was generated."""

    title: str
    """Concise title of the insight."""

    actionable_recommendation: Optional[str] = FieldInfo(alias="actionableRecommendation", default=None)
    """A concrete, actionable step the user can take."""

    action_trigger: Optional[str] = FieldInfo(alias="actionTrigger", default=None)
    """A programmatic identifier to trigger an action within the client application."""
