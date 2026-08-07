import numpy as np
import matplotlib.pyplot as plt


sales = np.array([
    120,
    200,
    150,
    300,
    250
])


months = [
    "Jan",
    "Feb",
    "Mar",
    "Apr",
    "May"
]


plt.plot(
    months,
    sales,
    marker="o"
)


plt.title("Monthly Sales")
plt.xlabel("Month")
plt.ylabel("Sales")


plt.grid(True)

plt.savefig(
    "sales_chart.png"
)


print("chart saved")


products = [
    "Laptop",
    "Mouse",
    "Phone"
]

product_sales = [
    500,
    300,
    700
]


plt.figure()

plt.bar(
    products,
    product_sales
)


plt.title("Product Sales")
plt.xlabel("Product")
plt.ylabel("Units")


plt.savefig(
    "product_sales.png"
)


print("bar chart saved")