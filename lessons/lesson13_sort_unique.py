import numpy as np

arr = np.array([9,4,7,2,1])

print(np.sort(arr))
print(np.sort(arr)[::-1])

matrix = np.array([
    [7,2,5],
    [9,1,3]
])

print(np.sort(matrix,axis=0))
print(np.sort(matrix,axis=1))

scores = np.array([70,20,90,40])
print(np.argsort(scores))


colors = np.array([
    "red",
    "blue",
    "red",
    "green",
    "blue",
    "red"
])
print(np.unique(colors))


unique, counts = np.unique(
    colors,
    return_counts=True
)
for i,j in zip(counts,unique):
    print(f"{i} : {j}")