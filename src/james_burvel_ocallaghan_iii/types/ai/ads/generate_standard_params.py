# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["GenerateStandardParams"]


class GenerateStandardParams(TypedDict, total=False):
    aspect_ratio: Required[Annotated[Literal["16:9", "9:16", "1:1"], PropertyInfo(alias="aspectRatio")]]
    """Desired aspect ratio of the video (e.g., for YouTube, Instagram Reels)."""

    length_seconds: Required[Annotated[int, PropertyInfo(alias="lengthSeconds")]]
    """Desired length of the video in seconds."""

    prompt: Required[str]
    """Textual description for the AI to generate the video content."""

    style: Required[Literal["Realistic", "Cinematic", "Animated", "Abstract", "Minimalist"]]
    """Artistic style preference for the video."""

    brand_colors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="brandColors")]
    """Optional list of brand hex colors to influence the video's aesthetic."""

    keywords: Optional[SequenceNotStr[str]]
    """Additional keywords to guide AI content generation."""
