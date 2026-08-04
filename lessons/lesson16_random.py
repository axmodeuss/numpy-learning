import numpy as np
import pandas as pd

numbers = np.random.rand()
print(numbers)
numbers1 = np.random.randint(1,50,10)
print(numbers1)
np.random.seed(50)
numbers2 = np.random.randint(0,20,size=(5,3))
print(f"mean_for everystudent : {np.mean(numbers2,axis=1)}")
print(f"mean for every lesson : {np.mean(numbers2,axis=0)}")
print(f"max for every lesson : {np.max(numbers2,axis=0)}")



df = pd.DataFrame(numbers2, columns=["Math", "Python", "Database"])

df["Average"] = df.mean(axis=1)

print(df)

df.to_csv("students_scores.csv", index=False)

print("CSV saved successfully!")













