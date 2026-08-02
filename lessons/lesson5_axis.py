import numpy as np

arr = np.array([
    [2,4,6],
    [1,3,5],
    [10,20,30]
])

print(arr)
print(30*"=",">")
print(arr.sum())
print(30*"=",">")
print(arr.sum(axis=0))
print(30*"=",">")
print(arr.sum(axis=1))
print(30*"=",">")
print(arr.mean(axis=0))
print(30*"=",">")
print(arr.mean(axis=1))
print(30*"=",">")
print(arr.max(axis=0))
print(30*"=",">")
print(arr.min(axis=1))
print(30*"=",">")
