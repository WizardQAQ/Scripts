import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('./CONTCAR', skiprows=8, max_rows=216)
cell = 13.0012617310165695
C = data[0:108]
C = C * cell
Ti = data[108:]
C_center = np.array([0.5,0.5,0.5]) * cell
distance = []
num = []
for i, R in enumerate(C):
    distance.append(np.sqrt(np.sum(np.power((R - C_center), 2))))
    num.append(i)

distance = np.array(distance)
num = np.array(num)

distance_ls = np.column_stack((distance, num))
#print(distance_ls)
print(distance_ls[np.argsort(distance_ls[:, 0])])
