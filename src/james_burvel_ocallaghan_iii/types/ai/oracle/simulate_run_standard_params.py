# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SimulateRunStandardParams"]


class SimulateRunStandardParams(TypedDict, total=False):
    prompt: Required[str]
    """A natural language prompt describing the 'what-if' scenario."""

    parameters: Optional[object]
    """
    Optional structured parameters to guide the simulation (e.g., duration, amount,
    risk tolerance).
    """
