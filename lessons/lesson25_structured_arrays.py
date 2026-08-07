import numpy as np

employees = np.array([
    ("Ali", 30, 4500.5),
    ("Sara", 25, 5200.0),
    ("Reza", 28, 4800.75),
    ("Mina", 35, 6500.0),
    ("Omid", 40, 7200.25)
],
dtype=[
    ("name" , "U8"),
    ("Age" , "i2"),
    ("Salary", "f4")
])

print(employees["name"])

print(employees[employees["Salary"]>5000])
sorted_employees = employees[np.argsort(employees["Salary"])]
print(sorted_employees)

