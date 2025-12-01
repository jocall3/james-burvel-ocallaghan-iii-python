# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GenerateStandardParams"]


class GenerateStandardParams(TypedDict, total=False):
    length_seconds: Required[Annotated[object, PropertyInfo(alias="lengthSeconds")]]
    """Desired length of the video in seconds."""

    prompt: Required[object]
    """The textual prompt to guide the AI video generation."""

    style: Required[Literal["Cinematic", "Explainer", "Documentary", "Abstract", "Minimalist"]]
    """Artistic style of the video."""

    aspect_ratio: Annotated[Literal["16:9", "9:16", "1:1"], PropertyInfo(alias="aspectRatio")]
    """
    Aspect ratio of the video (e.g., 16:9 for widescreen, 9:16 for vertical shorts).
    """

    brand_colors: Annotated[Optional[Iterable[object]], PropertyInfo(alias="brandColors")]
    """Optional: Hex color codes to influence the video's aesthetic."""

    keywords: Optional[Iterable[object]]
    """Optional: Additional keywords to guide the AI's content generation."""
