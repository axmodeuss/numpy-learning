import numpy as np

# a= np.array([[3,2],[5,4]])
# b= np.array([16,28])
a= np.array([[3,2],[5,7]])
b= np.array([18,39])

print(np.linalg.solve(a,b).round(2))