import numpy as np
import pandas as pd

np.random.seed(42)

sales = np.random.randint(
    100,
    1000,
    size=(50,5)
)

print("="*10,"INFO","="*10)

print("dtype :", sales.dtype)
print("shape :", sales.shape)
print("size :", sales.size)
print("ndim :", sales.ndim)

print("="*10,"DATA SAMPLE","="*10)

print(sales[:5])

total_sales = sales.sum()
print("Total_sales : ",total_sales)

product_sales = sales.sum(axis=0)

print(product_sales)


best_product = np.argmax(product_sales)

print(best_product)
products = np.array([
    "Laptop",
    "Mouse",
    "Keyboard",
    "Monitor",
    "Phone"
])

print(products[best_product])