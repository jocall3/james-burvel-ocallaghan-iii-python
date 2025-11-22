# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Required, TypedDict

__all__ = ["SimulateRunStandardParams"]


class SimulateRunStandardParams(TypedDict, total=False):
    prompt: Required[str]
    """A natural language description of the 'what-if' scenario to simulate."""

    parameters: Optional[object]
    """
    Optional: Structured parameters to guide the simulation (e.g., duration,
    amount).
    """
