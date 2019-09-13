import pickle
import numpy as np
from numpy import linalg as LIN

def Matrix_fn1(A):
  A_vals, A_vects = LIN.eig(A)
  A_sqrt = np.zeros(A.shape)
  for i in range(0, len(A_vals)):
    A_sqrt[i,i] = np.sqrt(A_vals[i])
  return np.dot(A_vects, np.dot(A_sqrt, LIN.inv(A_vects)))

def Matrix_fn2(A):
  A_vals, A_vects = LIN.eig(A)
  A_sqrt = np.zeros(A.shape)
  for i in range(0, len(A_vals)):
    A_sqrt[i,i] = 1.0/np.sqrt(A_vals[i])
  return np.dot(A_vects, np.dot(A_sqrt, LIN.inv(A_vects)))

def Matrix_fn3(A):
  U, S, V = LIN.svd(A)
  return np.dot(U, V)

def MAKE_A_PICKLE(a, b, c):
  with open('output_pickle.pickle', 'wb') as f:
    pickle.dump({'a': a, 'b': b, 'c': c}, f, pickle.HIGHEST_PROTOCOL)

