# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["GenerateAdvancedParams", "CallToAction"]


class GenerateAdvancedParams(TypedDict, total=False):
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

    audience_target: Annotated[
        Optional[Literal["general", "corporate", "investor", "youth"]], PropertyInfo(alias="audienceTarget")
    ]
    """Target audience for the ad, influencing tone and visuals."""

    background_music_genre: Annotated[
        Optional[Literal["corporate", "uplifting", "ambient", "cinematic", "none"]],
        PropertyInfo(alias="backgroundMusicGenre"),
    ]
    """Genre of background music."""

    brand_assets: Annotated[Optional[Iterable[object]], PropertyInfo(alias="brandAssets")]
    """URLs to brand assets (e.g., logos, specific imagery) to be incorporated."""

    brand_colors: Annotated[Optional[Iterable[object]], PropertyInfo(alias="brandColors")]
    """Optional: Hex color codes to influence the video's aesthetic."""

    call_to_action: Annotated[Optional[CallToAction], PropertyInfo(alias="callToAction")]
    """Call-to-action text and URL to be displayed."""

    keywords: Optional[Iterable[object]]
    """Optional: Additional keywords to guide the AI's content generation."""

    voiceover_style: Annotated[
        Optional[Literal["male_professional", "female_friendly", "neutral_calm"]], PropertyInfo(alias="voiceoverStyle")
    ]
    """Style/tone for the AI voiceover."""

    voiceover_text: Annotated[object, PropertyInfo(alias="voiceoverText")]
    """Optional: Text for an AI-generated voiceover."""


class CallToAction(TypedDict, total=False):
    """Call-to-action text and URL to be displayed."""

    display_time_seconds: Annotated[object, PropertyInfo(alias="displayTimeSeconds")]

    text: object

    url: object
