#!/usr/bin/env python3
""" make_multiplier function """
from typing import Callable


def make_multiplier(multiplier: float) -> Callable[[float], float]:
    """ make_multiplier function """
    def func(x: float) -> float:
        return (x * multiplier)

    return (func)
