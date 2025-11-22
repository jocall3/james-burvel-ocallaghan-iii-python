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
        "spending", "saving", "investing", "budget", "security", "sustainability", "financial_health", "corporate"
    ]
    """Category of the insight (e.g., spending, saving, investing)."""

    description: str
    """Detailed description of the insight."""

    severity: Literal["low", "medium", "high", "critical"]
    """The severity or urgency of the insight."""

    timestamp: datetime
    """Timestamp when the insight was generated."""

    title: str
    """A concise title for the insight."""

    actionable_recommendation: Optional[str] = FieldInfo(alias="actionableRecommendation", default=None)
    """A concrete, actionable step the user can take based on the insight."""
