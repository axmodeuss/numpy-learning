import numpy as np

def show_info(arr):
    print("="*30)
    print(arr)
    print(f"""
dtype : {arr.dtype}
shape : {arr.shape}
size  : {arr.size}
ndim  : {arr.ndim}
""")

arr1 = np.zeros(10,dtype=int)
print(f"{10*'='}{arr1}{10*'='}")
show_info(arr1)

arr2 = np.ones((4,5))
print(f"{10*'='}\n{arr2}\n{10*'='}")
show_info(arr2)

arr3 = np.full((3,3),9)
print(f"{10*'='}{arr3}{10*'='}")
show_info(arr2)

print(10*"=")

print(np.arange(0,50,5))
print(np.arange(10,101,10))
print(np.linspace(0,1,10))
print(np.linspace(100,200,5))

arr4= np.arange(0,100,2)
show_info(arr4)

arr5= np.linspace(-5,5,20)
show_info(arr5)

arr6= np.arange(2000,2026)
show_info(arr6)

arr7=np.linspace(15,25,7)
show_info(arr7)