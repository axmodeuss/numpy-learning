import numpy as np

A = np.array([[2,4],
     [6,8]])

B = np.array([[1,3],
     [5,7]])
print(A * B)
print(A@B)


matrix = np.arange(6).reshape(2,3)
print(matrix)
print(np.transpose(matrix))
print(matrix.T)

#3
print(10*"=")

arr = np.array([[15,18,20],
 [12,16,14],
 [20,19,18]])
nomre = arr @ [3,2,4]
print((nomre / 9).round(2))

