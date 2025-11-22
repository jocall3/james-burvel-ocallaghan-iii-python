# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PitchSubmitFeedbackParams", "Answer"]


class PitchSubmitFeedbackParams(TypedDict, total=False):
    answers: Optional[Iterable[Answer]]
    """Specific answers to previously asked questions."""

    feedback: Optional[str]
    """General feedback or additional information for Quantum Weaver."""


class Answer(TypedDict, total=False):
    answer: Required[str]
    """The answer to the question."""

    question_id: Required[Annotated[str, PropertyInfo(alias="questionId")]]
    """The ID of the question being answered."""
