""" Test numpy.ufunc and numpy.ndarray behave as defined in the
specification.
"""
import scipy.sparse as sp
import numpy as np
from numpy.testing import assert_almost_equal, assert_equal, assert_raises,\
    run_module_suite


def test_unary_ufuncs():
    """ Test that unary ufuncs act the same on spmatrix objects as
    ndarrays.
    """
    # data
    square = np.random.random((4, 4))
    sp_square = sp.csc_matrix(square)
    unary_ufunc = []
    for i in dir(np):
        attr = getattr(np, i)
        if type(attr) == np.ufunc and attr.nin == 1:
            unary_ufunc.append(attr)

    # ufuncs with one output
    for ufunc in unary_ufunc:
        # does the ufunc work?
        try:
            sp_val = ufunc(sp_square)
        except AttributeError:
            assert_raises(AttributeError, ufunc, sp_square)
            continue
        except TypeError:
            assert_raises(TypeError, ufunc, sp_square)
            continue
        val = ufunc(square)

        # ufuncs that have two or more outputs.
        if ufunc.nout != 1:
            for sparse, dense in zip(sp_val, val):
                # Type check.
                assert_equal(type(sparse) == sp.spmatrix, True)
                # Equity test.
                assert_almost_equal(sparse.toarray(), dense)

        # ufuncs with single outputs.
        else:
            # Type check.
            assert_equal(type(sp_val) == sp.csc_matrix, True)
            # Equalit check.
            assert_almost_equal(sp_val.toarray(), val)

if __name__ == '__main__':
    run_module_suite()
