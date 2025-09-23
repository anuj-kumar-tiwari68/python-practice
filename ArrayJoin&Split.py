import numpy as np
arr1 = np.array([[1,2],[4,5]])
arr2 = np.array([[1,3],[7,5]])
print(np.concatenate((arr1, arr2), axis=0))
print(np.concatenate((arr1, arr2), axis=1))
print(np.hstack([arr1, arr2])) # axis 1
print(np.vstack([arr1, arr2])) # axis 0