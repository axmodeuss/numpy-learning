import numpy as np

arr = np.arange(1,6)
arr2 = arr
arr2[0] = 100
print(arr,arr2)

print(np.shares_memory(arr,arr2))
print(arr.base)
print(arr2.base)