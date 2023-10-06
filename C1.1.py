X = list(map(int,input().split()))
Y = []
Y0 = []
Z = []
Z0 = []
s = str()
m = 0

for i in range(len(X)):
    if len(str(X[i])) > m: m = len(str(X[i]))

for i in range(len(X)):
    for l in range(1,m+1):
        x = str(X[i])
        if len(x) == l:
            x = x + '0'*(m-l)
            Y = Y + [x]
            Z = Z + [m-l]

Y0 = Y + []
Y0.sort(reverse = True)

for i in range(len(X)):
    for n in range(len(X)):
        if Y0[i] == Y[n]:
            Z0 = Z0 + [Z[n]]

for i in range(len(X)):
    y = str(Y0[i])
    s = s + y[0:m-Z0[i]]
print(s)

