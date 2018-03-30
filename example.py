import matplotlib.pyplot as plt
import math

x = []
y = []

for i in range(0, 50, 1):
	i = i/10
	x.append(i)
	y.append(math.sin(i))

plt.plot(x,y)
plt.show()