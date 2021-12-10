#!/usr/bin/env python3
import numpy as np


def add_arrays(arr1, arr2):
    """
    Function that adds two arrays
    """
    if np.array(arr1).shape == np.array(arr2).shape:
        return np.add(arr1, arr2)
    else:
        return None
