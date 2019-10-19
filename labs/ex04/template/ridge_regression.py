# -*- coding: utf-8 -*-
"""Exercise 3.

Ridge Regression
"""

import numpy as np


def ridge_regression(y, tx, lambda_):
    """implement ridge regression."""
    # ***************************************************
    w = tx.T @ tx + lambda_ * np.identity(tx.shape[1])
    trans = tx.T
    w2 = trans @ y
    w = np.linalg.solve(w, w2)
    error = y - tx.dot(w.transpose())
    loss = 0.5 * np.mean(error ** 2)
    return w, loss
    # ***************************************************
    raise NotImplementedError
