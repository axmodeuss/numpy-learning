import numpy as np
# arr = np.array([10,20,30,40,50,60,70,80])

# print(arr)

# print(f"first number : {arr[0]}")
# print(f"last number  : {arr[-1]}")
# print(f"third number  : {arr[2]}")
# print(f"first to third number  : {arr[:3]}")
# # print(f"40 to 70  : {arr[]}")
# even_numbers = arr[arr % 2 == 0]

# print(f"evens : {even_numbers}")

# print(arr[-3:])
# print(arr[::-1])
# print(arr[1:6])

arr = np.array([5,12,18,25,30,42,55,70,90])

print(arr[arr>40])
print(arr[arr<30])
print(arr[(20<arr ) & (arr<70)])
print(arr[arr % 2 != 0])
