import matplotlib.pyplot as plt
import numpy as np

###
#### Suryaansh Jain
#### cs21btech11057
###

plt.rcParams.update({'font.size': 15})
x1 = np.linspace(0,5000,1000)

y1 = x1*x1/100 + 100*x1 + 40
y2 = 200*x1 - x1*x1/400
y3 = 100 - x1/40
plt.plot(x1,y1,'blue')
plt.plot(x1,y2, 'red')
plt.plot(x1,y2-y1, 'yellow')

plt.plot(4000, 199960, marker = 'o', markersize = 5, markerfacecolor = 'blue')

plt.axhline(y = 0,color = "black")
plt.axvline(x = 0,color = "black")

plt.show()
