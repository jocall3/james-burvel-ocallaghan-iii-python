# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, TypedDict

__all__ = ["AdListGeneratedParams"]


class AdListGeneratedParams(TypedDict, total=False):
    limit: int
    """Maximum number of items to return in the response."""

    offset: int
    """Number of items to skip before starting to collect the result set."""

    status: Literal["queued", "generating", "done", "error"]
    """Filter ads by their generation status."""
