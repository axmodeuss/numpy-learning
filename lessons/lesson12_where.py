import numpy as np

numbers = np.array([1,5,10,15,20])

numbers_morethan10 = np.where(numbers>10,"Big","Small")
print(numbers_morethan10)

scores = np.array([20,55,90,40,75])
passed_scores = np.where(scores>=50,"Passed","Failed")
print(passed_scores)

ages = np.array([12,18,25,9,40])
ages_above18= np.where(ages>18,"adult","child")
print(ages_above18)

import pandas as pd

df = pd.DataFrame({
    "score":[40,70,90,30]
})

df["Status"] = np.where(df["score"]>=50,"Passed","Failed")
print(df)
