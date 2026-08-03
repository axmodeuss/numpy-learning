import numpy as np


arr = np.arange(1,10).reshape(3,3)

flatt = arr.flatten()
rav = arr.ravel()

print(10*"=","ravel")
rav[0] = 999

print(arr)
print(rav)
print(np.shares_memory(arr,rav))
print(10*"=","flatten")
flatt[0] = 999

print(arr)
print(flatt)
print(np.shares_memory(arr,flatt))


print(10*"=")

print(flatt.base)
print(rav.base)

