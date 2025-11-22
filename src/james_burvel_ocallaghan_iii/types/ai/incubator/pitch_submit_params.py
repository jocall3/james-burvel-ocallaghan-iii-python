# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from __future__ import annotations

from typing import Iterable
from typing_extensions import Required, Annotated, TypedDict

from ...._utils import PropertyInfo

__all__ = ["PitchSubmitParams", "FinancialProjections", "FoundingTeam"]


class PitchSubmitParams(TypedDict, total=False):
    business_plan: Required[Annotated[str, PropertyInfo(alias="businessPlan")]]
    """
    The user's detailed narrative business plan (e.g., executive summary, vision,
    strategy).
    """

    financial_projections: Required[Annotated[FinancialProjections, PropertyInfo(alias="financialProjections")]]
    """Key financial metrics and projections for the next 3-5 years."""

    founding_team: Required[Annotated[Iterable[FoundingTeam], PropertyInfo(alias="foundingTeam")]]
    """Key profiles and expertise of the founding team members."""

    market_opportunity: Required[Annotated[str, PropertyInfo(alias="marketOpportunity")]]
    """
    Detailed analysis of the target market, problem statement, and proposed
    solution's unique value proposition.
    """


class FinancialProjections(TypedDict, total=False):
    profitability_estimate: Annotated[str, PropertyInfo(alias="profitabilityEstimate")]
    """Estimated time to profitability."""

    projection_years: Annotated[int, PropertyInfo(alias="projectionYears")]
    """Number of years for financial projections."""

    revenue_forecast: Annotated[Iterable[float], PropertyInfo(alias="revenueForecast")]

    seed_round_amount: Annotated[float, PropertyInfo(alias="seedRoundAmount")]
    """Requested seed funding in USD."""

    valuation_pre_money: Annotated[float, PropertyInfo(alias="valuationPreMoney")]
    """Pre-money valuation in USD."""


class FoundingTeam(TypedDict, total=False):
    experience: str
    """Relevant experience."""

    name: str
    """Name of the team member."""

    role: str
    """Role of the team member."""
