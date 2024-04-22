#!/usr/bin/env python3
"""importing tuple and union"""
from typing import Tuple, Union


def to_kv(k: str, v: Union[int, float]) -> Tuple[str, float]:
    """return """
    return k, v * v
