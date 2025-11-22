# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ..._utils import PropertyInfo

__all__ = ["AnomalyUpdateStatusParams"]


class AnomalyUpdateStatusParams(TypedDict, total=False):
    status: Required[Literal["Dismissed", "Resolved", "Under Review", "Escalated"]]
    """The new status for the financial anomaly."""

    resolution_notes: Annotated[Optional[str], PropertyInfo(alias="resolutionNotes")]
    """Optional notes regarding the resolution or dismissal of the anomaly."""
