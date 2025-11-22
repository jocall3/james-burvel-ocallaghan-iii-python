# File generated from our OpenAPI spec by Stainless. See CONTRIBUTING.md for details.

from typing import Optional
from typing_extensions import Literal

from pydantic import Field as FieldInfo

from ..._models import BaseModel

__all__ = ["TransactionInitiateTransferResponse"]


class TransactionInitiateTransferResponse(BaseModel):
    status: Literal["pending_signature", "broadcasting", "pending_confirmation", "completed", "failed"]
    """Current status of the cryptocurrency transfer."""

    transfer_id: str = FieldInfo(alias="transferId")
    """Unique identifier for the initiated crypto transfer."""

    blockchain_txn_hash: Optional[str] = FieldInfo(alias="blockchainTxnHash", default=None)
    """The transaction hash on the blockchain, once broadcasted."""

    failed_reason: Optional[str] = FieldInfo(alias="failedReason", default=None)
    """If failed, the reason for the failure."""

    message: Optional[str] = None
    """A descriptive message regarding the current status or next steps."""
