import numpy as np

a = [1,2,3]
b = [4,5,6]

sales = np.concatenate((a,b))

print(sales)



A =\
[
 [1,2],
 [3,4]
]


B =\
[
 [5,6],
 [7,8]
]

print("anxis= 0 ","\n",np.concatenate((A,B),axis=0))
print("anxis= 1 ","\n",np.concatenate((A,B),axis=1))


names = np.array(["Ali", "Sara", "Reza", "Mina"])
scores = np.array([90, 75, 88, 60])

students = np.column_stack((names,scores))
print(students)


jan = np.array([120,200,150])
feb = np.array([180,220,170])
mar = np.array([210,250,190])

print("there month sales")
three = np.column_stack((jan,feb,mar))
print(three)