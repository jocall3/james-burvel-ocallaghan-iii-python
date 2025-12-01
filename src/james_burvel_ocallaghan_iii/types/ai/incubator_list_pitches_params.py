# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["IncubatorListPitchesParams"]


class IncubatorListPitchesParams(TypedDict, total=False):
    limit: object
    """Maximum number of items to return in a single page."""

    offset: object
    """Number of items to skip before starting to collect the result set."""

    status: Literal[
        "submitted",
        "initial_review",
        "ai_analysis",
        "feedback_required",
        "test_phase",
        "final_review",
        "approved_for_funding",
        "rejected",
        "incubated_graduated",
    ]
    """Filter pitches by their current stage."""
