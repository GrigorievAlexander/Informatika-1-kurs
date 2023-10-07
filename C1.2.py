X = [0] + list(map(int,input().split())) + [0]
m = 0
s = 0

for i in range(1, len(X) - 1):
    if X[i] <= X[i-1] + X[i+1]:
        for n in range(1, len(X) - 1):
            if X[n] > m:
                m = X[n]
                k = n
        s = s + m
        X[k] = 0
        X[k-1] = 0
        X[k+1] = 0
        m = 0
    else:
        s = s + X[i]
        X[i] = 0
        X[i - 1] = 0
        X[i + 1] = 0

print(s)