from typing import Any


def not_implemented(instance: Any) -> None:
    raise RuntimeError(f"Please implement method in {instance.__class__.__name__}")
