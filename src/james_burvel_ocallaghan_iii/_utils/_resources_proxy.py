from __future__ import annotations

from typing import Any
from typing_extensions import override

from ._proxy import LazyProxy


class ResourcesProxy(LazyProxy[Any]):
    """A proxy for the `james_burvel_ocallaghan_iii.resources` module.

    This is used so that we can lazily import `james_burvel_ocallaghan_iii.resources` only when
    needed *and* so that users can just import `james_burvel_ocallaghan_iii` and reference `james_burvel_ocallaghan_iii.resources`
    """

    @override
    def __load__(self) -> Any:
        import importlib

        mod = importlib.import_module("james_burvel_ocallaghan_iii.resources")
        return mod


resources = ResourcesProxy().__as_proxied__()
