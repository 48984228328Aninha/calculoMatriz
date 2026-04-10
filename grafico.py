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

#caso os dois gráficos estejam separados :)
x = np.linespace(-np.pi, np.pi, 35)
y_sen = np.sin(x)
y_cos = np.cos(x)

fig, (ax1, ax2) = plt.subplots(1, 2)

#gráfico 1
ax1.grid(True)
ax1.plot(x, y_sen)
ax1.set(title='Funções trigonométricas', ylabel = 'sen(x)')
ax1.set_xlim(-np.pi, np.pi)

#gráfico 2
ax2.grid(True)
ax2.plot(x , y_cos, color='orange')
ax2.set(xlabel = 'Ângulo [rad]', ylabel = 'cos(x)')
ax2.set_xlim(-np.pi, np.pi)


