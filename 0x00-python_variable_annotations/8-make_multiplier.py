#!/usr/bin/env python3
""" make_multiplier function """
from typing import Callable


def make_multiplier(c: float) -> Callable:
    """ function make_multiplier """
    def fun(x: float) -> float:
        """ function fun """
        return (x * c)

    return (fun)
