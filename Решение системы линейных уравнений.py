print('Введите количество переменных.')
n = int(input())
print('Введите количество уравнений.')
m = int(input())
print('Введите матрицу системы.')
A = []
b = []
for i in range(m):
    A = A + list(map(int, input().split()))
print('Введите столбец свободных членов (в одну строку).')
b = b + list(map(int, input().split()))

def dev(X, k1):
    k = (k1-1)*m + k1 - 1
    if X[k] != 0:
        p = X[k]
        for i in range(m):
            X[(k // m)*m + i] = X[(k // m)*m + i] / p
        b[k // m] = b[k // m] / p
    return X

def per(X, k):
    i = 0
    if (k+i-1)*m + k <= n:
        while X[(k+i-1)*m + k - 1] == 0:
            i = i + 1
        for p in range(n-k+1):
            s = X[(i+k-1)*m + k + p - 1]
            X[(i + k - 1) * m + k + p - 1] = X[(k-1)*m + k + p - 1]
            X[(k - 1) * m + k + p - 1] = s
            s1 = b[k+i-1]
            b[k+i-1] = b[k-1]
            b[k-1] = s1
    return X

def razn(X, k):
    for q in range(1, n-k+1):
        l = A[(k+q-1)*m + k - 1] / A[(k-1)*m + k - 1]
        for p in range(n-k+1):
            A[(k+q-1)*m + k+p - 1] = A[(k+q-1)*m + k+p - 1] - A[(k-1)*m + k + p - 1]*l
        b[k+q-1] = b[k+q-1] - b[k-1]*l
    return X

def razn2(X, k):
    for q in range(1, k-1+1):
        if A[(k-1)*m + k - 1] != 0:
            l = A[(k-q-1)*m + k - 1] / A[(k-1)*m + k - 1]
            for p in range(n - k + 1):
                A[(k - q - 1) * m + k + p - 1] = A[(k - q - 1) * m + k + p - 1] - A[(k - 1) * m + k + p - 1] * l
            b[k-q-1] = b[k-q-1] - b[k-1]*l
    return X

if m != n: print('Бесконечное количество решений, или их отсутствие.')
else:
    for i in range(1, n+1):
        A = per(A, i)
        A = dev(A, i)
        A = razn(A, i)
        A = razn2(A, i)

    if A[n**2 -1] == 0: print('Бесконечное количество решений.')
    else:
        print('Столбец решений (записан в строку): ', b)