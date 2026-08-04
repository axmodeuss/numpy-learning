import numpy as np

arr = np.arange(1,25)

arr_splited = np.split(arr,4)
print(arr_splited)


arr_array_split = np.arange(15)
print(np.array_split(arr_array_split,4))

matrix = np.array([
    [10,20],
    [30,40],
    [50,60],
    [70,80]
])
print(np.hsplit(matrix,2))


sales = np.array([
    [120,180,210],
    [200,220,250],
    [150,170,190]
])
splited = np.hsplit(sales,3)
for i in range(3):
    print(np.mean(splited[i]))


data = np.arange(1,13).reshape(3,4)

print(data)

print("vsplit:")
print(np.vsplit(data,3))

print("hsplit:")
print(np.hsplit(data,2))