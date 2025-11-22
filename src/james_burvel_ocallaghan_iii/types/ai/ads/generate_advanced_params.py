# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal, Required, Annotated, TypedDict

from ...._types import SequenceNotStr
from ...._utils import PropertyInfo

__all__ = ["GenerateAdvancedParams", "CallToAction"]


class GenerateAdvancedParams(TypedDict, total=False):
    aspect_ratio: Required[Annotated[Literal["16:9", "9:16", "1:1"], PropertyInfo(alias="aspectRatio")]]
    """Desired aspect ratio of the video (e.g., for YouTube, Instagram Reels)."""

    length_seconds: Required[Annotated[int, PropertyInfo(alias="lengthSeconds")]]
    """Desired length of the video in seconds."""

    prompt: Required[str]
    """Textual description for the AI to generate the video content."""

    style: Required[Literal["Realistic", "Cinematic", "Animated", "Abstract", "Minimalist"]]
    """Artistic style preference for the video."""

    audience_target: Annotated[
        Optional[Literal["general", "young_adults", "corporate", "small_business", "investors"]],
        PropertyInfo(alias="audienceTarget"),
    ]
    """Target audience to optimize messaging and visuals."""

    background_music: Annotated[
        Optional[Literal["upbeat", "calm", "dramatic", "none"]], PropertyInfo(alias="backgroundMusic")
    ]
    """Desired background music style."""

    brand_assets: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="brandAssets")]
    """URLs to brand assets (e.g., logos, specific imagery) to be incorporated."""

    brand_colors: Annotated[Optional[SequenceNotStr[str]], PropertyInfo(alias="brandColors")]
    """Optional list of brand hex colors to influence the video's aesthetic."""

    call_to_action: Annotated[Optional[CallToAction], PropertyInfo(alias="callToAction")]
    """Details for an integrated call-to-action button or text overlay."""

    keywords: Optional[SequenceNotStr[str]]
    """Additional keywords to guide AI content generation."""

    voiceover_style: Annotated[
        Optional[Literal["male_professional", "female_friendly", "neutral_calm"]], PropertyInfo(alias="voiceoverStyle")
    ]
    """Style of the AI-generated voiceover."""

    voiceover_text: Annotated[Optional[str], PropertyInfo(alias="voiceoverText")]
    """Specific text for a generated voiceover."""


class CallToAction(TypedDict, total=False):
    display_time_seconds: Annotated[int, PropertyInfo(alias="displayTimeSeconds")]

    text: str

    url: str
