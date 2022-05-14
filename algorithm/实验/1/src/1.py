import matplotlib.pyplot as plt
import numpy
import numpy as np

solution1 = np.loadtxt('time1.txt')
# solution1 = [numpy.log10(k) for k in solution1]
solution2 = np.loadtxt('time2.txt')
# solution2 = [numpy.log10(k) for k in solution2]

x1 = [10, 100, 1000, 10000, 100000]
x2 = [1, 2, 3, 4, 5]
plt.plot(x1, solution1, x1, solution2)
plt.xlabel('problem size')
plt.ylabel('time(ms)')
plt.show()
