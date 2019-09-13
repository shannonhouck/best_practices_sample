import numpy as np
from numpy import linalg as LIN

def matrix_inv(A, inv=False):
    """
    Returns square root of matrix A.

    Computes and returns the square root of a given positive definite matrix
    A via an eigendecomposition approach.

    :param A: Matrix for which sqare root is computed
    :param inv: Whether to conpute inverse square root (defaults to False)
    :return: Square root of matrix A (invert square root if requested)
    """
    # do eigendecomposition
    A_vals, A_vects = LIN.eig(A)
    # set up diagonal for multiplication
    A_sqrt = np.zeros(A.shape)
    for i in range(0, len(A_vals)):
        if(inv):
           A_sqrt[i,i] = 1.0/np.sqrt(A_vals[i])
        else:
           A_sqrt[i,i] = np.sqrt(A_vals[i])
    return np.dot(A_vects, np.dot(A_sqrt, LIN.inv(A_vects)))

def lowdin_orth(A):
    """
    Performs Lowdin orthogonalization on given matrix A.

    This performs a Lowdin orthogonalization on a matrix A, using an
    SVD-based approach. You may bump into issues if you use this for
    matrices with linearly dependent columns.

    :param A: The matrix to orthogonalize
    :return: Orthogonalized A
    """
    U, S, V = LIN.svd(A)
    return np.dot(U, V)

