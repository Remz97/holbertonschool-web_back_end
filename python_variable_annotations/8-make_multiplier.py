#!/usr/bin/env python3
"""importing callable"""
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """returns a function that multiplies a float by multiplier"""
    def mul_num(num: float) -> float:
        return multiplier * num
    return mul_num
