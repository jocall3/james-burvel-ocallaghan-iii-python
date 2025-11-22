# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["GenerateAdvancedParams", "CallToAction"]


class GenerateAdvancedParams(TypedDict, total=False):
    aspect_ratio: Required[Annotated[Literal["16:9", "9:16", "1:1"], PropertyInfo(alias="aspectRatio")]]
    """Aspect ratio of the video (e.g., 16:9 for landscape, 9:16 for portrait)."""

    length_seconds: Required[Annotated[int, PropertyInfo(alias="lengthSeconds")]]
    """Desired length of the video in seconds."""

    prompt: Required[str]
    """The text prompt describing the desired video content."""

    style: Required[Literal["Cinematic", "Documentary", "Explainer", "Animated", "Minimalist", "Energetic"]]
    """Artistic style of the video."""

    audience_target: Annotated[
        Optional[Literal["general", "young_adult", "corporate", "small_business", "investors"]],
        PropertyInfo(alias="audienceTarget"),
    ]
    """Optional: Target audience to influence tone and content."""

    background_music_volume: Annotated[Optional[float], PropertyInfo(alias="backgroundMusicVolume")]
    """Optional: Volume level for background music (0-1)."""

    brand_assets: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="brandAssets")]
    """
    Optional: URLs to brand assets (e.g., logo, specific imagery) for AI to
    incorporate.
    """

    brand_colors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="brandColors")]
    """Optional: Brand hex color codes to influence visual palette."""

    call_to_action: Annotated[Optional[CallToAction], PropertyInfo(alias="callToAction")]
    """Optional: Details for a call-to-action overlay at the end of the video."""

    music_genre: Annotated[Optional[str], PropertyInfo(alias="musicGenre")]
    """Optional: Preferred genre for background music."""

    voiceover_style: Annotated[
        Optional[Literal["male_professional", "female_friendly", "neutral_narrator"]],
        PropertyInfo(alias="voiceoverStyle"),
    ]
    """Optional: Style of the AI-generated voiceover."""

    voiceover_text: Annotated[Optional[str], PropertyInfo(alias="voiceoverText")]
    """Optional: Custom voiceover script for the video."""


class CallToAction(TypedDict, total=False):
    text: Required[str]
    """Text to display for the call to action."""

    url: Required[str]
    """URL to link to when the call to action is clicked."""

    display_time_seconds: Annotated[Optional[int], PropertyInfo(alias="displayTimeSeconds")]
    """Duration in seconds to display the CTA at the end of the video."""
