# -*- coding: utf-8 -*-
"""Exercise 3.

Split the dataset based on the given ratio.
"""


import numpy as np


def split_data(x, y, ratio, seed=1):
    """split the dataset based on the split ratio."""
    # set seed
    np.random.seed(seed)
    # ***************************************************
    indicies = np.random.permutation(x.shape[0])
    train_x, test_x = x[indicies[:int(len(y)*ratio)]], x[indicies[int(len(y)*ratio):]]
    train_y, test_y = y[indicies[:int(len(y)*ratio)]], y[indicies[int(len(y)*ratio):]]
    return train_y, train_x, test_y, test_x
    # ***************************************************
    raise NotImplementedError
