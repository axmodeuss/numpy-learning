import numpy as np

products = np.array([
    "Keyboard",
    "Mouse",
    "Monitor",
    "Laptop",
    "Headphone"
])

prices = np.array([50, 25, 300, 1200, 80])

print(products[[0,3,4]])
print(products[np.argsort(prices)[4:1:-1]])