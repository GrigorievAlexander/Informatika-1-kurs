x = input().split(); l = len(x)-1; p = x[l]
for i in range(len(x)): x[l-i] = x[l-1-i]
x[0] = p; print(x)
