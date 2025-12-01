# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransactionInitiateTransferResponse"]


class TransactionInitiateTransferResponse(BaseModel):
    status: Literal["pending_signature", "pending_blockchain_confirmation", "completed", "failed", "cancelled"]
    """Current status of the transfer."""

    transfer_id: str = FieldInfo(alias="transferId")
    """Unique identifier for this cryptocurrency transfer operation."""

    blockchain_txn_hash: Optional[str] = FieldInfo(alias="blockchainTxnHash", default=None)
    """The blockchain transaction hash, if available and confirmed."""

    message: Optional[str] = None
    """A descriptive message about the transfer status."""
