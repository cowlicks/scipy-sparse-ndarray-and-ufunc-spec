## terms



## ndarry

> An `ndarray` is a (usually fixed-size) multidimensional container of items of the same type and size. The number of dimensions and items in an array is defined by its `shape`, which is a `tuple` of N positive integers that specify the sizes of each dimension. The type of items in the array is specified by a separate data-type object (dtype), one of which is associated with each ndarray.

## ufunc
NumPy's ufuncs currently do not support sparse matrices. And have even less support binary operation on sparse dense combinations. The proposed remedy:


1. The numpy ufunc class will recognize it is operating on a sparse matrix, so it will dispatch the operation and args to a 'magic function' in the sparse package. 
2. The magic function will look at the operation and type of args (sparse/dense, sparse/sparse, sparse, etc.) then call the correct sparse function/method. (Currently most of these are methods, but should probably be functions, this would eliminate a lot of repeated code and help consolidate the interface... I think.)
3. The function will do the operation and handle the guess work of whether a sparse or dense matrix should be returned. (A lot of these functions do not exist. e.g divide, add, etc.)

## Unary ufuncs

A unary `ufunc` operating on a `spmatrix` should return a spmatrix. This is tested with `test_unary_ufuncs` in the test suite. There is an exception to this `numpy.modf` and `numpy.frex` which return two spmatrix objects.

Unary ufuncs: 
TODO  
...

Unary with two ouputs:  

    modf
    frex

## Binary ufuncs

A binary `ufunc` should return a `spmatrix` object when both of its inputs are `spmatrix` objects. If its inputs are mixed, it should return an `ndarray` object. And if there are no `spmatrix` objects the `ufunc` is unaffected.

Note that this is not optimal. For example `np.multiply` acting on mixed `spmatrix`/`ndarray` objects could return a `spmatrix` in the case where `ndarray` is vector like.  
