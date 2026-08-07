import numpy as np
import matplotlib.pyplot as plt


products = np.array([
    "Laptop",
    "Mouse",
    "Keyboard",
    "Phone",
    "Monitor"
])

sales = np.array([
    500,
    300,
    450,
    700,
    600
])


# Bar chart
plt.figure(figsize=(7,4))

plt.bar(products, sales)

plt.title("Product Sales")
plt.xlabel("Products")
plt.ylabel("Sales")

plt.xticks(rotation=45)

plt.savefig("product_sales_bar.png")

plt.close()



# Scatter chart

customers = np.array([
    20,
    30,
    45,
    60,
    80
])


plt.figure(figsize=(7,4))

plt.scatter(
    customers,
    sales
)

plt.title("Customers vs Sales")
plt.xlabel("Customers")
plt.ylabel("Sales")

plt.savefig("customers_sales_scatter.png")

plt.close()



# Histogram

data = np.random.randint(
    0,
    100,
    100
)


plt.figure(figsize=(7,4))

plt.hist(
    data,
    bins=10
)

plt.title("Score Distribution")
plt.xlabel("Score")
plt.ylabel("Frequency")

plt.savefig("score_distribution.png")


print("charts created")