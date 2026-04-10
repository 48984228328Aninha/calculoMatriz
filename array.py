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

a = py.range(15)
print(f'a: =\n {a}')

a = a.reshape(3,5)
print(f'a: =\n {a}')

b = a[1:3, 3:5] # para a linha de índice2 (os índices das 3 linhas são 0, 1 e 2), serão selecionados os elementos que ocupam os lugares dos índices 1 ao 3.
print(f'b: =\n {b}')