# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Dict

from ...._models import BaseModel

__all__ = ["AIFunctionCall"]


class AIFunctionCall(BaseModel):
    id: str
    """A unique ID for this specific function call instance."""

    args: Dict[str, object]
    """Arguments to pass to the tool function."""

    name: str
    """The name of the tool function to be invoked."""
