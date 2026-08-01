import numpy as np

arr1 = np.zeros(10,dtype=int)
print(f"{10*'='}{arr1}{10*'='}")
print(f"dtype : {arr1.dtype} \nshape: {arr1.shape} \nsize: {arr1.size}\nndim : {arr1.ndim}")

arr2 = np.ones((4,5))
print(f"{10*'='}\n{arr2}\n{10*'='}")
print(f"dtype : {arr2.dtype} \nshape: {arr2.shape} \nsize: {arr2.size}\nndim : {arr2.ndim}")

arr3 = np.full((3,3),9)
print(f"{10*'='}{arr3}{10*'='}")
print(f"dtype : {arr3.dtype} \nshape: {arr3.shape} \nsize: {arr3.size}\nndim : {arr3.ndim}")

