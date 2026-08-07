import numpy as np
import pandas as pd

np.random.seed(42)

sales = np.random.randint(
    100,
    1000,
    size=(50, 5)
)

products = np.array([
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Phone"
])


print("=" * 20)
print("DATA INFORMATION")
print("=" * 20)

print("dtype :", sales.dtype)
print("shape :", sales.shape)
print("size  :", sales.size)
print("ndim  :", sales.ndim)


print("\n" + "=" * 20)
print("FIRST 5 CUSTOMERS")
print("=" * 20)

print(
    pd.DataFrame(
        sales[:5],
        columns=products
    )
)


print("\n" + "=" * 20)
print("TOTAL SALES")
print("=" * 20)

total_sales = sales.sum()

print("Total units sold:", total_sales)


print("\n" + "=" * 20)
print("PRODUCT ANALYSIS")
print("=" * 20)

product_sales = sales.sum(axis=0)

product_report = pd.DataFrame({
    "Product": products,
    "Total Sales": product_sales
})

print(product_report)


best_index = np.argmax(product_sales)
worst_index = np.argmin(product_sales)

print("\nBest product :", products[best_index])
print("Worst product:", products[worst_index])


print("\n" + "=" * 20)
print("CUSTOMER ANALYSIS")
print("=" * 20)


customer_average = sales.mean(axis=1)

customer_report = pd.DataFrame({
    "Customer": np.arange(1,51),
    "Average": customer_average
})


customer_report["Category"] = np.where(
    customer_report["Average"] >= 700,
    "VIP",
    "Normal"
)


print(customer_report.head())


print("\nVIP CUSTOMERS")
print("=" * 20)

vip_customers = customer_report[
    customer_report["Category"] == "VIP"
]

print(vip_customers)


print("\n" + "=" * 20)
print("FULL SALES REPORT")
print("=" * 20)


df = pd.DataFrame(
    sales,
    columns=products
)


df["Customer"] = np.arange(1,51)

df["Total"] = sales.sum(axis=1)

df["Average"] = sales.mean(axis=1)

df["Category"] = np.where(
    df["Average"] >= 700,
    "VIP",
    "Normal"
)


df = df[
    [
        "Customer",
        "Laptop",
        "Mouse",
        "Keyboard",
        "Monitor",
        "Phone",
        "Total",
        "Average",
        "Category"
    ]
]


print(df.head(10))


print("\n" + "=" * 20)
print("STATISTICS")
print("=" * 20)

print(df.describe())


print("\n" + "=" * 20)
print("TOP 5 CUSTOMERS")
print("=" * 20)

top_customers = df.sort_values(
    by="Total",
    ascending=False
)

print(top_customers.head())


print("\n" + "=" * 20)
print("CATEGORY COUNT")
print("=" * 20)

print(df["Category"].value_counts())


print("\nSaving report...")

df.to_csv(
    "final_sales_report.csv",
    index=False
)

print("Done!")