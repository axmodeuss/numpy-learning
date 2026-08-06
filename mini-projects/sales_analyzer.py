import numpy as np
import pandas as pd

np.random.seed(42)

sales = np.random.randint(
    100,
    1000,
    size=(12,5)
)


print(f"{10*"="}INFORMATION{10*"="}")
print(sales.shape,
sales.ndim,
sales.dtype,
sales.size)

print(f"{10*"="}Sales{10*"="}")
print(sales.sum())

print(f"{10*"="}sale of each product{10*"="}")
print(sales.sum(axis=0))
sum_month = sales.sum(axis=1)
print(f"{10*"="}sale of each month{10*"="}")
print(sales.sum(axis=1))

print(f"{10*"="}max and min{10*"="}")
print(f"Max: \n {sales.max(axis=0)}\nMin:\n{sales.min(axis=0)}")

print(f"{10*"="}worst and best month{10*"="}")
print(f"best : {np.argmax(sum_month)+1}\nworst: {np.argmin(sum_month)+1}")

# print(f"{10*"="}monthes with sales more than 3000{10*"="}")
# print(sum_month[(np.where(sum_month>3000))])

print(f"{10*'='} months with sales more than 3000 {10*'='}")

mask = sum_month > 3000

print("Months:", np.arange(1, 13)[mask])
print("Sales :", sum_month[mask])



print(f"{10*'='} income {10*'='}")
prices = np.array([
    20,
    15,
    35,
    40,
    25
])
income = sales@prices
income_dict = {
    month: int(value)
    for month, value in zip(range(1,13), income)
}

print(income_dict)

print(f"{10*'='} 13) np.where {10*'='}")
revenue_100001 = np.where(income>80000,"Excellent","Normal")
print(revenue_100001)





print(f"{10*'='} 14)making Data frame {10*'='}")
df = pd.DataFrame(sales,columns=["Product_A",
"Product_B",
"Product_C",
"Product_D",
"Product_E"])
df["Revenue"] = income
df["Status"] = revenue_100001
months = [
    "Jan","Feb","Mar","Apr",
    "May","Jun","Jul","Aug",
    "Sep","Oct","Nov","Dec"
]

df.insert(0, "Month", months)
print(df)
print(df.head())
print(df.info())
print(df.describe())
