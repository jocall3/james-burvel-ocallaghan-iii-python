# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["GenerateStandardParams"]


class GenerateStandardParams(TypedDict, total=False):
    aspect_ratio: Required[Annotated[Literal["16:9", "9:16", "1:1"], PropertyInfo(alias="aspectRatio")]]
    """Aspect ratio of the video (e.g., 16:9 for landscape, 9:16 for portrait)."""

    length_seconds: Required[Annotated[int, PropertyInfo(alias="lengthSeconds")]]
    """Desired length of the video in seconds."""

    prompt: Required[str]
    """The text prompt describing the desired video content."""

    style: Required[Literal["Cinematic", "Documentary", "Explainer", "Animated", "Minimalist", "Energetic"]]
    """Artistic style of the video."""

    brand_colors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="brandColors")]
    """Optional: Brand hex color codes to influence visual palette."""

    music_genre: Annotated[Optional[str], PropertyInfo(alias="musicGenre")]
    """Optional: Preferred genre for background music."""
