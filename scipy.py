import matplotlib._pyplot as plt
import numpy as np
from scipy import onterpolate

x = np.arrange(0, 10)
y = np.exp(-x / 3.0)

f = interpolate.interp1d(x, y)
xnew = np.arrange(0, 9, 0.1)
ynew = f(xnew)

plt.plot(x, y, 'o', label='dados')
plot.plot(xnew, ynew, '−', label='interpolação')
plt.legend()
plt.show()
