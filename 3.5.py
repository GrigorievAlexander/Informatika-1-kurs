import numpy
n = int(input())
m = int(input())
X = numpy.zeros((n,m))

M = m
N = n
r = 0

if n>m: s = m
else: s = n

for l in range(0,s//2+1):

    n2 = 0 + l*(m+1)
    y2 = 2 * (N + M) - 3 + r
    for b2 in range(1, N):
        y2 = y2 - 1
        n2 = n2 + m
        numpy.put(X, n2, y2)

    i2 = m * (n - 1) - 1 + l*(-m+1)
    x2 = 2 * M + N - 1 + r
    for a2 in range(1, M):
        x2 = x2 - 1
        i2 = i2 + 1
        numpy.put(X, i2, x2)

    n1 = m - 1 + l*(m-1)
    y1 = M + r
    for b1 in range(1, N):
        y1 = y1 + 1
        n1 = n1 + m
        numpy.put(X, n1, y1)

    i1 = -1 + l*(m+1)
    x1 = 0 + r
    for a1 in range(1, M+1):
        i1 = i1 + 1
        x1 = x1 + 1
        numpy.put(X, i1, x1)

    r = (2 * (M + N) - 3) + r - 1
    N = N - 2
    M = M - 2

print(X)

for q in range(n):
    for i in range(m):
        t = X[0+q][i]
        numpy.put(X, i+q*m, (q+1)*t)
print(X)
