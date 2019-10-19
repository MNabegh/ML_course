# -*- coding: utf-8 -*-
"""Exercise 3.

Least Square
"""

import numpy as np


def least_squares(y, tx):
    """calculate the least squares."""
    # ***************************************************
    w = tx.T @ tx
    trans = tx.T
    w2 = trans @ y
    w = np.linalg.solve(w, w2)
    return w
    # ***************************************************
    raise NotImplementedError
