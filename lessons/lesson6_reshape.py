import numpy as np

arr = np.arange(1,13)

print(arr)
print(arr.shape)
print(30*"=",">")
print(arr.reshape(3,4))
print(30*"=",">")
print(arr.reshape(4,3))
print(30*"=",">")
print(arr.reshape(2,-1))
print(arr.reshape(-1,6))
print(30*"=",">")
print(arr.reshape(5,3))
