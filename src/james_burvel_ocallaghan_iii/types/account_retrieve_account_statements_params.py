# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing_extensions import Literal, Required, TypedDict

__all__ = ["AccountRetrieveAccountStatementsParams"]


class AccountRetrieveAccountStatementsParams(TypedDict, total=False):
    month: Required[object]
    """Month for the statement (1-12)."""

    year: Required[object]
    """Year for the statement."""

    format: Literal["pdf", "csv"]
    """Desired format for the statement.

    Use 'application/json' Accept header for download links.
    """
