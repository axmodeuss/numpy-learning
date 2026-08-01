import numpy as np



arr1 = np.array([10,20,30,40,50])
print(f"{10*'='}{arr1}{10*'='}")
print(f"dtype : {arr1.dtype} \nshape: {arr1.shape} \nsize: {arr1.size}\nndim : {arr1.ndim}")
arr2 = np.array([1.5,2.5,3.5])
print(f"{10*'='}{arr2}{10*'='}")
print(f"dtype : {arr2.dtype} \nshape: {arr2.shape} \nsize: {arr2.size}\nndim : {arr2.ndim}")
arr3 = np.array(["python","numpy","pandas"])
print(f"{10*'='}{arr3}{10*'='}")
print(f"dtype : {arr3.dtype} \nshape: {arr3.shape} \nsize: {arr3.size}\nndim : {arr3.ndim}")
arr4 = np.random.randint(10,100,20)
print(f"{10*'='}{arr4}{10*'='}")
print(f"dtype : {arr4.dtype} \nshape: {arr4.shape} \nsize: {arr4.size}\nndim : {arr4.ndim}")

