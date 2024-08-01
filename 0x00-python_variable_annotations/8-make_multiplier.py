#!/usr/bin/env python3
""" make_multiplier function """
from typing import Callable


def make_multiplier(c: float) -> Callable[[float], float]:
    """ function make_multiplier """
    def fun(x: float) -> float:
        return (x * c)

    return (fun)
