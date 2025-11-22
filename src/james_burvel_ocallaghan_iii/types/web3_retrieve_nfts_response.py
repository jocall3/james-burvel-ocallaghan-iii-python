# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Web3RetrieveNFTsResponse", "Web3RetrieveNFTsResponseItem", "Web3RetrieveNFTsResponseItemAttribute"]


class Web3RetrieveNFTsResponseItemAttribute(BaseModel):
    trait_type: Optional[str] = None

    value: Optional[str] = None


class Web3RetrieveNFTsResponseItem(BaseModel):
    id: str
    """Unique identifier for the NFT within ."""

    blockchain_network: Literal["Ethereum", "Solana", "Polygon", "other"] = FieldInfo(alias="blockchainNetwork")
    """The blockchain network where the NFT resides."""

    collection_name: str = FieldInfo(alias="collectionName")
    """Name of the NFT collection."""

    contract_address: str = FieldInfo(alias="contractAddress")
    """The smart contract address of the NFT collection."""

    image_url: str = FieldInfo(alias="imageUrl")
    """URL to the NFT's image or media."""

    name: str
    """Name or title of the specific NFT."""

    owner_address: str = FieldInfo(alias="ownerAddress")
    """The blockchain address of the current owner."""

    token_id: str = FieldInfo(alias="tokenId")
    """The unique ID of the NFT within its contract."""

    attributes: Optional[List[Web3RetrieveNFTsResponseItemAttribute]] = None
    """List of traits/attributes of the NFT."""

    description: Optional[str] = None
    """Description of the NFT."""

    estimated_value_usd: Optional[float] = FieldInfo(alias="estimatedValueUSD", default=None)
    """AI-estimated current market value of the NFT in USD."""

    last_sale_price_usd: Optional[float] = FieldInfo(alias="lastSalePriceUSD", default=None)
    """The last known sale price of the NFT in USD."""


Web3RetrieveNFTsResponse: TypeAlias = List[Web3RetrieveNFTsResponseItem]
