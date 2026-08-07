import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv("final_sales_report.csv")


print("="*10, "INFO", "="*10)
print(df.info())


print("="*10, "HEAD", "="*10)
print(df.head())


print("="*10, "STATISTICS", "="*10)
print(df.describe())


print("="*10, "CATEGORY", "="*10)
print(df["Category"].value_counts())


best = df.sort_values(
    by="Total",
    ascending=False
)

print("="*10, "BEST CUSTOMERS", "="*10)
print(best.head())


plt.figure(figsize=(8,5))


plt.bar(
    df["Customer"],
    df["Total"]
)


plt.title("Customer Total Sales")

plt.xlabel("Customer")
plt.ylabel("Sales")


plt.savefig("customer_sales_report.png")


plt.close()


plt.figure(figsize=(7,5))

df["Category"].value_counts().plot(
    kind="pie",
    autopct="%1.1f%%"
)

plt.title("Customer Categories")

plt.ylabel("")

plt.savefig("customer_category.png")


print("Report created")