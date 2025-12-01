# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable, Optional
from typing_extensions import Literal

import httpx

from ...._types import Body, Omit, Query, Headers, NotGiven, omit, not_given
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
        length_seconds: object,
        prompt: object,
        style: Literal["Cinematic", "Explainer", "Documentary", "Abstract", "Minimalist"],
        aspect_ratio: Literal["16:9", "9:16", "1:1"] | Omit = omit,
        audience_target: Optional[Literal["general", "corporate", "investor", "youth"]] | Omit = omit,
        background_music_genre: Optional[Literal["corporate", "uplifting", "ambient", "cinematic", "none"]]
        | Omit = omit,
        brand_assets: Optional[Iterable[object]] | Omit = omit,
        brand_colors: Optional[Iterable[object]] | Omit = omit,
        call_to_action: Optional[generate_advanced_params.CallToAction] | Omit = omit,
        keywords: Optional[Iterable[object]] | Omit = omit,
        voiceover_style: Optional[Literal["male_professional", "female_friendly", "neutral_calm"]] | Omit = omit,
        voiceover_text: object | Omit = omit,
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
          length_seconds: Desired length of the video in seconds.

          prompt: The textual prompt to guide the AI video generation.

          style: Artistic style of the video.

          aspect_ratio: Aspect ratio of the video (e.g., 16:9 for widescreen, 9:16 for vertical shorts).

          audience_target: Target audience for the ad, influencing tone and visuals.

          background_music_genre: Genre of background music.

          brand_assets: URLs to brand assets (e.g., logos, specific imagery) to be incorporated.

          brand_colors: Optional: Hex color codes to influence the video's aesthetic.

          call_to_action: Call-to-action text and URL to be displayed.

          keywords: Optional: Additional keywords to guide the AI's content generation.

          voiceover_style: Style/tone for the AI voiceover.

          voiceover_text: Optional: Text for an AI-generated voiceover.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/generate/advanced",
            body=maybe_transform(
                {
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "aspect_ratio": aspect_ratio,
                    "audience_target": audience_target,
                    "background_music_genre": background_music_genre,
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
        length_seconds: object,
        prompt: object,
        style: Literal["Cinematic", "Explainer", "Documentary", "Abstract", "Minimalist"],
        aspect_ratio: Literal["16:9", "9:16", "1:1"] | Omit = omit,
        brand_colors: Optional[Iterable[object]] | Omit = omit,
        keywords: Optional[Iterable[object]] | Omit = omit,
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
          length_seconds: Desired length of the video in seconds.

          prompt: The textual prompt to guide the AI video generation.

          style: Artistic style of the video.

          aspect_ratio: Aspect ratio of the video (e.g., 16:9 for widescreen, 9:16 for vertical shorts).

          brand_colors: Optional: Hex color codes to influence the video's aesthetic.

          keywords: Optional: Additional keywords to guide the AI's content generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return self._post(
            "/ai/ads/generate",
            body=maybe_transform(
                {
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "aspect_ratio": aspect_ratio,
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
        length_seconds: object,
        prompt: object,
        style: Literal["Cinematic", "Explainer", "Documentary", "Abstract", "Minimalist"],
        aspect_ratio: Literal["16:9", "9:16", "1:1"] | Omit = omit,
        audience_target: Optional[Literal["general", "corporate", "investor", "youth"]] | Omit = omit,
        background_music_genre: Optional[Literal["corporate", "uplifting", "ambient", "cinematic", "none"]]
        | Omit = omit,
        brand_assets: Optional[Iterable[object]] | Omit = omit,
        brand_colors: Optional[Iterable[object]] | Omit = omit,
        call_to_action: Optional[generate_advanced_params.CallToAction] | Omit = omit,
        keywords: Optional[Iterable[object]] | Omit = omit,
        voiceover_style: Optional[Literal["male_professional", "female_friendly", "neutral_calm"]] | Omit = omit,
        voiceover_text: object | Omit = omit,
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
          length_seconds: Desired length of the video in seconds.

          prompt: The textual prompt to guide the AI video generation.

          style: Artistic style of the video.

          aspect_ratio: Aspect ratio of the video (e.g., 16:9 for widescreen, 9:16 for vertical shorts).

          audience_target: Target audience for the ad, influencing tone and visuals.

          background_music_genre: Genre of background music.

          brand_assets: URLs to brand assets (e.g., logos, specific imagery) to be incorporated.

          brand_colors: Optional: Hex color codes to influence the video's aesthetic.

          call_to_action: Call-to-action text and URL to be displayed.

          keywords: Optional: Additional keywords to guide the AI's content generation.

          voiceover_style: Style/tone for the AI voiceover.

          voiceover_text: Optional: Text for an AI-generated voiceover.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/generate/advanced",
            body=await async_maybe_transform(
                {
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "aspect_ratio": aspect_ratio,
                    "audience_target": audience_target,
                    "background_music_genre": background_music_genre,
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
        length_seconds: object,
        prompt: object,
        style: Literal["Cinematic", "Explainer", "Documentary", "Abstract", "Minimalist"],
        aspect_ratio: Literal["16:9", "9:16", "1:1"] | Omit = omit,
        brand_colors: Optional[Iterable[object]] | Omit = omit,
        keywords: Optional[Iterable[object]] | Omit = omit,
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
          length_seconds: Desired length of the video in seconds.

          prompt: The textual prompt to guide the AI video generation.

          style: Artistic style of the video.

          aspect_ratio: Aspect ratio of the video (e.g., 16:9 for widescreen, 9:16 for vertical shorts).

          brand_colors: Optional: Hex color codes to influence the video's aesthetic.

          keywords: Optional: Additional keywords to guide the AI's content generation.

          extra_headers: Send extra headers

          extra_query: Add additional query parameters to the request

          extra_body: Add additional JSON properties to the request

          timeout: Override the client-level default timeout for this request, in seconds
        """
        return await self._post(
            "/ai/ads/generate",
            body=await async_maybe_transform(
                {
                    "length_seconds": length_seconds,
                    "prompt": prompt,
                    "style": style,
                    "aspect_ratio": aspect_ratio,
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
