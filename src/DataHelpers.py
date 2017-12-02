# -*- coding: utf-8 -*-


import numpy as np


def shuffle_data(list_X, list_Y):
    shuffle_indices = np.random.permutation(np.arange(len(list_X)))
    return np.array(list_X)[shuffle_indices], np.array(list_Y)[shuffle_indices]
