from collections.abc import Callable
from dataclasses import dataclass
from typing import Any


@dataclass(frozen=True)
class Command:
    handler: Callable[..., Any]
    description: str
