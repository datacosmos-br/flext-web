"""Base protocol facade for flext-web.

Absorbs every protocol shard through MRO so the public ``protocols.py``
facade composes a single ``Api`` namespace.
"""

from __future__ import annotations

from . import (
    FlextWebProtocolsConfig,
    FlextWebProtocolsData,
    FlextWebProtocolsFramework,
    FlextWebProtocolsLifecycle,
    FlextWebProtocolsMonitoring,
    FlextWebProtocolsTemplate,
)


class FlextWebProtocolsBase(
    FlextWebProtocolsConfig,
    FlextWebProtocolsData,
    FlextWebProtocolsFramework,
    FlextWebProtocolsLifecycle,
    FlextWebProtocolsMonitoring,
    FlextWebProtocolsTemplate,
):
    """FLEXT Web protocol namespace."""


__all__: list[str] = ["FlextWebProtocolsBase"]
