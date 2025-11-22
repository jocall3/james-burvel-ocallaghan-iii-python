# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, SequenceNotStr, omit, not_given
from ...._utils import maybe_transform, async_maybe_transform
from ...._compat import cached_property
from ...._resource import SyncAPIResource, AsyncAPIResource
from ...._response import (
    to_raw_response_wrapper,
    to_streamed_response_wrapper,
    async_to_raw_response_wrapper,
    async_to_streamed_response_wrapper,
)
from ...._base_client import make_request_options
from ....types.ai.ads import generate_advanced_params, generate_standard_params
from ....types.ai.ads.generate_advanced_response import GenerateAdvancedResponse
from ....types.ai.ads.generate_standard_response import GenerateStandardResponse

__all__ = ["GenerateResource", "AsyncGenerateResource"]


class GenerateResource(SyncAPIResource):
    @cached_property
    def with_raw_response(self) -> GenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return GenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> GenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return GenerateResourceWithStreamingResponse(self)

    def advanced(
        self,
        *,
        aspect_ratio: Literal["16:9", "9:16", "1:1"],
        length_seconds: int,
        prompt: str,
        style: Literal["Realistic", "Cinematic", "Animated", "Abstract", "Minimalist"],
        audience_target: Optional[Literal["general", "young_adults", "corporate", "small_business", "investors"]]
        | Omit = omit,
        background_music: Optional[Literal["upbeat", "calm", "dramatic", "none"]] | Omit = omit,
        brand_assets: Optional[SequenceNotStr[str]] | Omit = omit,
        brand_colors: Optional[SequenceNotStr[str]] | Omit = omit,
        call_to_action: Optional[generate_advanced_params.CallToAction] | Omit = omit,
        keywords: Optional[SequenceNotStr[str]] | Omit = omit,
        voiceover_style: Optional[Literal["male_professional", "female_friendly", "neutral_calm"]] | Omit = omit,
        voiceover_text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateAdvancedResponse:
        """
        Submits a highly customized request to generate a video ad, allowing
        fine-grained control over artistic style, aspect ratio, voiceover, background
        music, target audience, and call-to-action elements for professional-grade
        productions.

        Args:
          aspect_ratio: Desired aspect ratio of the video (e.g., for YouTube, Instagram Reels).

          length_seconds: Desired length of the video in seconds.

          prompt: Textual description for the AI to generate the video content.

          style: Artistic style preference for the video.

          audience_target: Target audience to optimize messaging and visuals.

          background_music: Desired background music style.

          brand_assets: URLs to brand assets (e.g., logos, specific imagery) to be incorporated.

          brand_colors: Optional list of brand hex colors to influence the video's aesthetic.

          call_to_action: Details for an integrated call-to-action button or text overlay.

          keywords: Additional keywords to guide AI content generation.

          voiceover_style: Style of the AI-generated voiceover.

          voiceover_text: Specific text for a generated voiceover.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/generate/advanced",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "audience_target": audience_target,
                    "background_music": background_music,
                    "brand_assets": brand_assets,
                    "brand_colors": brand_colors,
                    "call_to_action": call_to_action,
                    "keywords": keywords,
                    "voiceover_style": voiceover_style,
                    "voiceover_text": voiceover_text,
                },
                generate_advanced_params.GenerateAdvancedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateAdvancedResponse,
        )

    def standard(
        self,
        *,
        aspect_ratio: Literal["16:9", "9:16", "1:1"],
        length_seconds: int,
        prompt: str,
        style: Literal["Realistic", "Cinematic", "Animated", "Abstract", "Minimalist"],
        brand_colors: Optional[SequenceNotStr[str]] | Omit = omit,
        keywords: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateStandardResponse:
        """
        Submits a request to generate a high-quality video ad using the advanced Veo 2.0
        generative AI model. This is an asynchronous operation, suitable for standard ad
        content creation.

        Args:
          aspect_ratio: Desired aspect ratio of the video (e.g., for YouTube, Instagram Reels).

          length_seconds: Desired length of the video in seconds.

          prompt: Textual description for the AI to generate the video content.

          style: Artistic style preference for the video.

          brand_colors: Optional list of brand hex colors to influence the video's aesthetic.

          keywords: Additional keywords to guide AI content generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/generate",
            body=maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "brand_colors": brand_colors,
                    "keywords": keywords,
                },
                generate_standard_params.GenerateStandardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateStandardResponse,
        )


class AsyncGenerateResource(AsyncAPIResource):
    @cached_property
    def with_raw_response(self) -> AsyncGenerateResourceWithRawResponse:
        """
        This property can be used as a prefix for any HTTP method call to return
        the raw response object instead of the parsed content.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#accessing-raw-response-data-eg-headers
        """
        return AsyncGenerateResourceWithRawResponse(self)

    @cached_property
    def with_streaming_response(self) -> AsyncGenerateResourceWithStreamingResponse:
        """
        An alternative to `.with_raw_response` that doesn't eagerly read the response body.

        For more information, see https://www.github.com/jocall3/james-burvel-ocallaghan-iii-python#with_streaming_response
        """
        return AsyncGenerateResourceWithStreamingResponse(self)

    async def advanced(
        self,
        *,
        aspect_ratio: Literal["16:9", "9:16", "1:1"],
        length_seconds: int,
        prompt: str,
        style: Literal["Realistic", "Cinematic", "Animated", "Abstract", "Minimalist"],
        audience_target: Optional[Literal["general", "young_adults", "corporate", "small_business", "investors"]]
        | Omit = omit,
        background_music: Optional[Literal["upbeat", "calm", "dramatic", "none"]] | Omit = omit,
        brand_assets: Optional[SequenceNotStr[str]] | Omit = omit,
        brand_colors: Optional[SequenceNotStr[str]] | Omit = omit,
        call_to_action: Optional[generate_advanced_params.CallToAction] | Omit = omit,
        keywords: Optional[SequenceNotStr[str]] | Omit = omit,
        voiceover_style: Optional[Literal["male_professional", "female_friendly", "neutral_calm"]] | Omit = omit,
        voiceover_text: Optional[str] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateAdvancedResponse:
        """
        Submits a highly customized request to generate a video ad, allowing
        fine-grained control over artistic style, aspect ratio, voiceover, background
        music, target audience, and call-to-action elements for professional-grade
        productions.

        Args:
          aspect_ratio: Desired aspect ratio of the video (e.g., for YouTube, Instagram Reels).

          length_seconds: Desired length of the video in seconds.

          prompt: Textual description for the AI to generate the video content.

          style: Artistic style preference for the video.

          audience_target: Target audience to optimize messaging and visuals.

          background_music: Desired background music style.

          brand_assets: URLs to brand assets (e.g., logos, specific imagery) to be incorporated.

          brand_colors: Optional list of brand hex colors to influence the video's aesthetic.

          call_to_action: Details for an integrated call-to-action button or text overlay.

          keywords: Additional keywords to guide AI content generation.

          voiceover_style: Style of the AI-generated voiceover.

          voiceover_text: Specific text for a generated voiceover.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/generate/advanced",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "audience_target": audience_target,
                    "background_music": background_music,
                    "brand_assets": brand_assets,
                    "brand_colors": brand_colors,
                    "call_to_action": call_to_action,
                    "keywords": keywords,
                    "voiceover_style": voiceover_style,
                    "voiceover_text": voiceover_text,
                },
                generate_advanced_params.GenerateAdvancedParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateAdvancedResponse,
        )

    async def standard(
        self,
        *,
        aspect_ratio: Literal["16:9", "9:16", "1:1"],
        length_seconds: int,
        prompt: str,
        style: Literal["Realistic", "Cinematic", "Animated", "Abstract", "Minimalist"],
        brand_colors: Optional[SequenceNotStr[str]] | Omit = omit,
        keywords: Optional[SequenceNotStr[str]] | Omit = omit,
        # Use the following arguments if you need to pass additional parameters to the API that aren't available via kwargs.
        # The extra values given here take precedence over values defined on the client or passed to this method.
        extra_headers: Headers | None = None,
        extra_query: Query | None = None,
        extra_body: Body | None = None,
        timeout: float | httpx.Timeout | None | NotGiven = not_given,
    ) -> GenerateStandardResponse:
        """
        Submits a request to generate a high-quality video ad using the advanced Veo 2.0
        generative AI model. This is an asynchronous operation, suitable for standard ad
        content creation.

        Args:
          aspect_ratio: Desired aspect ratio of the video (e.g., for YouTube, Instagram Reels).

          length_seconds: Desired length of the video in seconds.

          prompt: Textual description for the AI to generate the video content.

          style: Artistic style preference for the video.

          brand_colors: Optional list of brand hex colors to influence the video's aesthetic.

          keywords: Additional keywords to guide AI content generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/generate",
            body=await async_maybe_transform(
                {
                    "aspect_ratio": aspect_ratio,
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "brand_colors": brand_colors,
                    "keywords": keywords,
                },
                generate_standard_params.GenerateStandardParams,
            ),
            options=make_request_options(
                extra_headers=extra_headers, extra_query=extra_query, extra_body=extra_body, timeout=timeout
            ),
            cast_to=GenerateStandardResponse,
        )


class GenerateResourceWithRawResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.advanced = to_raw_response_wrapper(
            generate.advanced,
        )
        self.standard = to_raw_response_wrapper(
            generate.standard,
        )


class AsyncGenerateResourceWithRawResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.advanced = async_to_raw_response_wrapper(
            generate.advanced,
        )
        self.standard = async_to_raw_response_wrapper(
            generate.standard,
        )


class GenerateResourceWithStreamingResponse:
    def __init__(self, generate: GenerateResource) -> None:
        self._generate = generate

        self.advanced = to_streamed_response_wrapper(
            generate.advanced,
        )
        self.standard = to_streamed_response_wrapper(
            generate.standard,
        )


class AsyncGenerateResourceWithStreamingResponse:
    def __init__(self, generate: AsyncGenerateResource) -> None:
        self._generate = generate

        self.advanced = async_to_streamed_response_wrapper(
            generate.advanced,
        )
        self.standard = async_to_streamed_response_wrapper(
            generate.standard,
        )
