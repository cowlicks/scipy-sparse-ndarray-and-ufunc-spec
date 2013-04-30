## ufuncs
NumPy's ufuncs currently do not support sparse matrices. And have even less support binary operation on sparse dense combinations. The proposed remedy:


1. The numpy ufunc class will recognize it is operating on a sparse matrix, so it will dispatch the operation and args to a 'magic function' in the sparse package. 
2. The magic function will look at the operation and type of args (sparse/dense, sparse/sparse, sparse, etc.) then call the correct sparse function/method. (Currently most of these are methods, but should probably be functions, this would eliminate a lot of repeated code and help consolidate the interface... I think.)
3. The function will do the operation and handle the guess work of whether a sparse or dense matrix should be returned. (A lot of these functions do not exist. e.g divide, add, etc.)
