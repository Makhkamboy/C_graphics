import numpy as np
import matplotlib.pyplot as plt
import scipy.interpolate as si

points = np.array([[0, 0], [0, 2], [2, 3], [4, 0], [6, 3], [8, 2], [8, 0]])
x = points[:,0]
y = points[:,1]

t = range(len(x))
knots = [2, 3, 4]
ipl_t = np.linspace(0.0, len(points) - 1, 100)

x_tup = si.splrep(t, x, k=3, t=knots)
y_tup = si.splrep(t, y, k=3, t=knots)
x_i = si.splev(ipl_t, x_tup)
y_i = si.splev(ipl_t, y_tup)

print ('knots:', x_tup)

fig = plt.figure()
ax = fig.add_subplot(111)
plt.plot(x, y, label='original')
plt.plot(x_i, y_i, label='spline')
plt.xlim([min(x) - 1.0, max(x) + 1.0])
plt.ylim([min(y) - 1.0, max(y) + 1.0])
plt.legend()
plt.show()
