import numpy as np

randoms = np.random.randint(1,100,20)
print(np.mean(randoms))

tas_10 = np.random.randint(1,7,10)


animals = np.array([
    "Cat",
    "Dog",
    "Bird",
    "Lion"
])
print(np.random.choice(animals))

base = np.arange(1,21)

print(base)
base_permutation = np.random.permutation(base)
print(base_permutation)

print(base)
np.random.shuffle(base)
print(base)





