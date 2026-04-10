import numpy as np
import matplotlib.pyplot as plt

x = np.linespace(-np.pi, np.pi, 35)
y_sen = np.sin(x)
y_cos = np.cos(x)

plt.plot(x , y_sen, label='seno')
plt.plot(x, y_cos, label='cosseno')
plt.xlim(-np.pi, np.pi)
plt.xlabel('Ângulo [rad]')
plt.ylabel('Função trigonométrica(X)')
plt.legend()
plt.show()

print(f'x: =\n {x}')
print(f'y_sen: =\n {y_sen}')
print(f'y_cos: =\n {y_cos}')
