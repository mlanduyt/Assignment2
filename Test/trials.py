import numpy as np

A = np.array([[1, 3, 2],[2, 2, 1],[3, 1, 3]])
e_vals, e_vecs = np.linalg.eig(A)
print (e_vals[0])