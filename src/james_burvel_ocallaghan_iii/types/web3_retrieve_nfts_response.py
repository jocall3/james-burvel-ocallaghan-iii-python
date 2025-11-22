# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import List, Optional
from typing_extensions import Literal, TypeAlias

from pydantic import Field as FieldInfo

from .._models import BaseModel

__all__ = ["Web3RetrieveNFTsResponse", "Web3RetrieveNFTsResponseItem", "Web3RetrieveNFTsResponseItemAttribute"]


class Web3RetrieveNFTsResponseItemAttribute(BaseModel):
    trait_type: Optional[str] = None
    """The type of trait."""

    value: Optional[str] = None
    """The value of the trait."""


class Web3RetrieveNFTsResponseItem(BaseModel):
    id: str
    """Unique identifier for the NFT within ."""

    blockchain_network: Literal["Ethereum", "Solana", "Polygon", "Binance Smart Chain"] = FieldInfo(
        alias="blockchainNetwork"
    )
    """The blockchain network the NFT resides on."""

    collection_name: str = FieldInfo(alias="collectionName")
    """Name of the NFT collection."""

    contract_address: str = FieldInfo(alias="contractAddress")
    """The contract address of the NFT collection."""

    image_url: str = FieldInfo(alias="imageUrl")
    """URL to the NFT's image or metadata."""

    name: str
    """Specific name or title of the NFT."""

    owner_address: str = FieldInfo(alias="ownerAddress")
    """The blockchain address of the current owner."""

    token_id: str = FieldInfo(alias="tokenId")
    """The unique token ID of the NFT within its collection."""

    attributes: Optional[List[Web3RetrieveNFTsResponseItemAttribute]] = None
    """List of traits/attributes of the NFT."""

    description: Optional[str] = None
    """Description of the NFT."""

    estimated_value_usd: Optional[float] = FieldInfo(alias="estimatedValueUSD", default=None)
    """AI's estimated current market value of the NFT in USD."""

    last_sale_price_usd: Optional[float] = FieldInfo(alias="lastSalePriceUSD", default=None)
    """Last known sale price of this NFT in USD."""

    metadata_url: Optional[str] = FieldInfo(alias="metadataUrl", default=None)
    """URL to the NFT's metadata JSON."""


Web3RetrieveNFTsResponse: TypeAlias = List[Web3RetrieveNFTsResponseItem]
