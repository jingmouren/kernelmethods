# -*- coding: utf-8 -*-

"""Kernel methods module."""

from kernelmethods.base import KernelMatrix
import numpy as np
from scipy.linalg import eigh, LinAlgError
import warnings

def is_positive_semidefinite(input_matrix, tolerance=1e-8):
    """
    Tests whether a given matrix is PSD.

    A symmetric matrix is PSD if ALL its eigen values >= 0 (non-negative).
        If any of its eigen values are negative, it is not PSD.

    Accouting for numerical instabilities with tolerance

    """

    if isinstance(input_matrix, KernelMatrix):
        sym_matrix = input_matrix.full_dense
    else:
        sym_matrix = input_matrix

    if sym_matrix.shape[0] != sym_matrix.shape[1]:
        warnings.warn('Input matrix is not square, and hence not PSD')
        return False

    if not np.isclose(sym_matrix, sym_matrix.T).all():
        warnings.warn('Input matrix is not symmetric, and hence not PSD')
        return False

    try:
        eig_values = eigh(sym_matrix, eigvals_only=True)
    except LinAlgError:
        print('LinAlgError raised - eigen value computation failed --> not PSD')
        psd = False
    except:
        warnings.warn('Unknown exception during eigen value computation  --> not PSD')
        psd = False
    else:
        if any(eig_values < tolerance):
            psd = False
        else:
            psd = True

    return psd


# shorter alias
is_PSD = is_positive_semidefinite


def center_KM(KM):
    """Center the given kernel matrix"""

    pass

def eval_similarity(km_one, km_two):
    """Evaluate similarity between two kernel matrices"""

    pass

def linear_comb(km_list, param_list):
    """Linear combinations of a list of kernels"""