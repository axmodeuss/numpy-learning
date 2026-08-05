import numpy as np

arr = np.array([12,15,18,20,25,30,35,40,45,50])

print("mean :",np.mean(arr))
print("median :",np.median(arr))
print("std :",np.std(arr))
print("variance :",np.var(arr))


arr2 = np.random.randint(0,20,100)
print(arr2)
print("mean : " ,np.mean(arr2))
print("max : ",np.max(arr2))
print("min : ",np.min(arr2))
print("median : ",np.median(arr2))
print("percentile 75 : ",np.percentile(arr2,75))


import pandas as pd

df = pd.DataFrame(arr2,columns=["Score"])
df["result"] = np.where(df["Score"]>=10,"Passed","Failed")
print(df)
print(df.describe())

