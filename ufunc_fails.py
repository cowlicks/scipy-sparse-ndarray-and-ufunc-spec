""" Test numpy.ufunc and numpy.ndarray behave as defined in the
specification.
"""
import scipy.sparse as sp
import numpy as np
from numpy.testing import assert_equal, assert_almost_equal


def test_unary_ufuncs():
    """ Test that unary ufuncs act the same on spmatrix objects as
    ndarrays.
    """

    # data
    square = np.random.random((4, 4))
    sp_square = spmatrix(square)

    unary_ufuncs = []
    unary_with

    # ufuncs with one output
    for ufunc in unary_ufunc:
        sp_val = ufunc(sp_square)
        val = ufunc(square)

        # ufuncs that have two outputs.
        if type(val) == tuple:
            for sp, dense in zip(sp_val, val):
                # Type check.
                assert_equal(type(sp) == sp.spmatrix, True)

                # Equity test.
                assert_almost_equal(sp.toarray(), dense)
        # ufuncs with single outputs.
        else:
            # Type check.
            assert_equal(type(sp) == sp.spmatrix, True)

            # Equalit check.
            assert_almost_equal(sp_val.toarray(), val)
