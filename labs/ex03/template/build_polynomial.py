# -*- coding: utf-8 -*-
"""implement a polynomial basis function."""

import numpy as np


def build_poly(x, degree):
    """polynomial basis functions for input data x, for j=0 up to j=degree."""
    exp_x = np.array([x, ] * (degree + 1))
    return np.power(exp_x.T, range(degree + 1))
