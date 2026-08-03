import numpy as np

arr = np.array([2,4,6,8,10])


#add 7 to all
arr2 = arr + 7
print(arr2)
# all * 5
arr3 = arr* 5
print(arr3)
# all ^ 3
arr4 = arr ** 3
print(arr4)
# all % 4
arr5 = arr % 4
print(arr5)

arr10 = np.array([1,2,3,4,5])

print(arr+arr10)

print(arr[arr>6])
print(np.sqrt(arr))

challeng = np.array([3,6,9,12,15])
challeng_done = challeng*2 -1
print(challeng_done)
