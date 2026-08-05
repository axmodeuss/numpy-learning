import numpy as np

arr = np.array([10,25,40,55,70,85])
print("numbers biger than 50 :",arr[arr>50])
print("numbers smaller than 40 :",arr[arr<=40])

arr2 = np.random.randint(0,100,30)
print("even numbers :",arr2[arr2%2 == 0])
print("numbers bigger than 70 :",arr2[arr2 > 70])
print("numbers between 30 and 60 :",arr2[(arr2 < 60)&(arr2 > 30)])

arr2[arr2<20] = 0
print(arr2)
arr2[arr2>90] = 90
print(arr2)

import pandas as pd

df = pd.DataFrame(arr2,columns=["Score"])
df["Excellent"] = np.where(df["Score"]>=85,"true","False")
print(df)



