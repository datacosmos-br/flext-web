"""Base model facade for flext-web.

Absorbs every model shard through MRO so the public ``models.py`` facade
composes a single ``Api`` namespace.
"""

from __future__ import annotations

from ._auth import FlextWebModelsAuth
from ._config import FlextWebModelsConfig
from ._entity import FlextWebModelsEntity
from ._factory import FlextWebModelsFactory
from ._http import FlextWebModelsHttp
from ._responses import FlextWebModelsResponses
from ._system import FlextWebModelsSystem
from ._web_message import FlextWebModelsWebMessage
from ._web_request import FlextWebModelsWebRequest


class FlextWebModelsBase(
    FlextWebModelsAuth,
    FlextWebModelsConfig,
    FlextWebModelsEntity,
    FlextWebModelsFactory,
    FlextWebModelsHttp,
    FlextWebModelsResponses,
    FlextWebModelsSystem,
    FlextWebModelsWebMessage,
    FlextWebModelsWebRequest,
):
    """FLEXT Web model namespace."""


__all__: list[str] = ["FlextWebModelsBase"]
