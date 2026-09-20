"""Base protocol facade for flext-web.

Owns the single composition of every protocol shard ``Web`` namespace so the
public ``protocols.py`` facade delegates to one canonical merge.
"""

from __future__ import annotations

from .config import FlextWebProtocolsConfig
from .data import FlextWebProtocolsData
from .framework import FlextWebProtocolsFramework
from .lifecycle import FlextWebProtocolsLifecycle
from .monitoring import FlextWebProtocolsMonitoring
from .template import FlextWebProtocolsTemplate


class FlextWebProtocolsBase:
    """FLEXT Web protocol namespace."""

    class Web(
        FlextWebProtocolsLifecycle.Web,
        FlextWebProtocolsData.Web,
        FlextWebProtocolsTemplate.Web,
        FlextWebProtocolsMonitoring.Web,
        FlextWebProtocolsConfig.Web,
        FlextWebProtocolsFramework.Web,
    ):
        """Composed Web protocol surface."""


__all__: list[str] = ["FlextWebProtocolsBase"]
