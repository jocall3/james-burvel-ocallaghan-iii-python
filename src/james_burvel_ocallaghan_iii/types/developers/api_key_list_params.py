# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import TypedDict

__all__ = ["APIKeyListParams"]


class APIKeyListParams(TypedDict, total=False):
    limit: object
    """Maximum number of items to return in a single page."""

    offset: object
    """Number of items to skip before starting to collect the result set."""
