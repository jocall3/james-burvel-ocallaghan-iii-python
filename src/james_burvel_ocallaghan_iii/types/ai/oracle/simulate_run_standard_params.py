# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Dict, Optional
from typing_extensions import Required, TypedDict

__all__ = ["SimulateRunStandardParams"]


class SimulateRunStandardParams(TypedDict, total=False):
    prompt: Required[str]
    """Natural language description of the financial scenario to simulate."""

    parameters: Optional[Dict[str, object]]
    """
    Optional: Structured parameters to guide the AI simulation (e.g., duration,
    amount, riskTolerance).
    """
