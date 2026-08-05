import numpy as np
import pandas as pd

scores = np.arange(1,21)

# np.save("numbers.npy",scores)

# print(np.load("numbers.npy"))

matrix = np.random.randint(0,100,size=(6,4))
# np.savetxt(
#     "scores.csv",
#     matrix,
#     fmt="%d",
#     delimiter=","
# )
# print(np.loadtxt("scores.csv",delimiter=",",dtype=int))

df = pd.DataFrame(matrix,columns=["Math","Physics","Python","Database"])
df["Average"] = df.mean(axis=1)
df["P_F"] = df["Average"].apply(lambda x : "Passed" if x >= 50 else "Failed")
df.to_csv("report.csv")







