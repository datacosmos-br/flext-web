"""Scalar constants for flext-web.

Copyright (c) 2025 FLEXT Team. All rights reserved.
SPDX-License-Identifier: MIT
"""

from __future__ import annotations

from typing import Final


class FlextWebConstantsValues:
    """Scalar constants mixed into ``c.Web``."""

    SUCCESS_RANGE: Final[tuple[int, int]] = (200, 299)
    ERROR_MIN: Final[int] = 400


__all__: list[str] = ["FlextWebConstantsValues"]
