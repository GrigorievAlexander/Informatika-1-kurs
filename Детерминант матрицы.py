import itertools

print('Введите порядок матрицы.')
n = int(input())
print('Введите саму квадратную матрицу.')
A = []
for i in range(n):
    A = A + list(map(float, input().split()))

N = []
for i in range(n):
    N.append(i+1)

K = itertools.permutations(N)
s = 0
for X in K:
    P = 1
    z = 0
    for i in range(n):
        for j in range(n):
            if i<j and X[i]>X[j]: z = z + 1
    for i in range(1, n+1):
        P = P * A[(i-1)*n + X[i-1] -1]
    s = s + ((-1)**z)*P
print('Ваш определитель равен: ', s, '', sep='')