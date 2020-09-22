import matplotlib.pyplot as plt
import numpy as np
import os

fig, ax = plt.subplots()
x = np.linspace(-5.12, 5.12, num = 401)
A = 10
y = ((np.sin(A*np.pi*x))/2*x)+(x-1)**4
path = 'results'
if not os.path.exists(path):
    os.mkdir(path)#Создаю папку
file = open(r'results\task_01_207_KRASKOVSKY_13.txt','w')
count = 0
while count < x.size:
    file.write(str(x[count]))
    file.write("    ")
    file.write(str(y[count]))
    file.write("\n")
    count += 1
file.close()
ax.plot(x, y)
plt.show()