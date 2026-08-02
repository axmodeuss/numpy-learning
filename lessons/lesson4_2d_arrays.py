import numpy as np

arr = np.array([
    [10,20,30,40],
    [50,60,70,80],
    [90,100,110,120]
])

print(20*"=","array",20*"=")
print(arr)
print(arr.shape)
print(arr.ndim)
print(arr.size)

print(5,arr[0])
print(6,arr[-1])
print(7,arr[:,0])
print(8,arr[:,2])
print(9,arr[1,2])
print(10,arr[:2])
print(11,arr[:,0:2])

