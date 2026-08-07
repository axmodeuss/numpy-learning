import numpy as np

x = np.array([2,4,6])
y = np.array([1,3,5])

X, Y = np.meshgrid(x, y)

print(X)
print(Y)

print("X - y =","\n",X-Y)


numbers = np.arange(1,11)
X,Y = np.meshgrid(numbers,numbers)
print("X x Y =","\n",X*Y)

print("distance = √(x² + y²) ","\n",np.sqrt(X**2 + Y**2).round(2))