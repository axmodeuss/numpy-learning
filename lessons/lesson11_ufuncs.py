import numpy as np

arr = np.array([9,16,25,36])

print(np.sqrt(arr))


arr = np.array([-20,-5,8,10])

print(np.abs(arr))


arr = np.array([2,3,4])

print(np.power(arr,3))


prices = np.array([12.4,18.9,20.1])

print(np.round(prices))
print(np.ceil(prices))
print(np.floor(prices))

scores = np.array([-10,40,70,120])

print(np.clip(scores,0,100))

a = np.array([1,5,9])

b = np.array([3,4,10])

print(np.maximum(a,b))



temps = np.array([-15,5,18,27,43,60])
print(np.clip(temps,0,50))
