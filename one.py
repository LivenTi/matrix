import numpy as np


n = np.random.randint(2, 4)
m = np.random.randint(2, 4)
zeros = np.zeros((n, n))
bzeros = []
for i in range(m):
    block_str = []
    for j in range(m):
        block_str.append(zeros)
    bzeros.append(block_str)
matrix = np.block(bzeros)
for i in range(m):
    matrix[i * n: (i + 1) * n, i * n: (i + 1) * n] = np.random.randint(-10, 10, (n, n))

print(matrix)
