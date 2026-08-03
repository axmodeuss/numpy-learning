import numpy as np
import pandas as pd

np.random.seed(42)

scores = np.random.randint(0,101,size=(10,5))

print(20*"=","data","\n",scores)
print(20*"=","shape","\n",scores.shape)
print(20*"=","ndim","\n",scores.ndim)
print(20*"=","dtype","\n",scores.dtype) 

print(10*"=","mean of every student",10*"=")
print(scores.mean(axis=1))
print(10*"=","mean of every lesson",10*"=")
print(scores.mean(axis=0))
print(10*"=","max of every lesson",10*"=")
print(scores.max(axis=0))
print(10*"=","min of every lesson",10*"=")
print(scores.min(axis=0))
print(10*"=","passed student",10*"=")
print(scores[scores.mean(axis=1)>=50])


df = pd.DataFrame(
    scores,
    columns=[
        "Math",
        "Physics",
        "Chemistry",
        "Biology",
        "English"
    ]
)
print(10*"=","making pandas Table",10*"=")
print(df)

print(10*"=","add columns",10*"=")
df["Passed"] = scores.mean(axis=1) >= 50
df["Average"] = scores.mean(axis=1)
print(df)

df.to_csv("student_scores.csv",index=False)

print(df.head())
print(df.describe())
def extraa(data):
    if data >=85:
        return "A"
    elif data >= 70 and data < 85:
        return "B"
    elif data >= 50 and data < 70:
        return "C"
    else :
        return "F"
df["extra"] = df["Average"].apply(extraa)
print(df)