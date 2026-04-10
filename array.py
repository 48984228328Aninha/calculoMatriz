import numpy as py

A = py.array([[1, 2, 3],
              [4, 5, 6],
              [7, 8, 9]])
B = py.array([[10, 11, 12],
              [13, 14, 15],
              [16, 17, 18]])

C = A @ B
print(C)

#criar uma matriz 3x5 sem precisar digitar tudo
a = py.arrange(15)
a = a.reshape(3,5)
print(a)
print(a.shape)
print(a.size)
print(len(a))