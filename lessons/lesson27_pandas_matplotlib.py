import pandas as pd
import matplotlib.pyplot as plt


df = pd.read_csv(
    "final_sales_report.csv"
)


print("=" * 20)
print("DATA")
print("=" * 20)

print(df.head())


print("=" * 20)
print("PRODUCT SALES")
print("=" * 20)


products = [
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Phone"
]


product_sales = df[products].sum()


print(product_sales)


plt.figure(figsize=(8,5))


plt.bar(
    product_sales.index,
    product_sales.values
)


plt.title(
    "Total Product Sales"
)

plt.xlabel(
    "Product"
)

plt.ylabel(
    "Sales"
)


plt.xticks(rotation=45)

plt.show()
# plt.savefig(
#     "product_sales.png",
#     bbox_inches="tight"
# )


# print("chart saved")