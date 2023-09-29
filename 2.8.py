x = input().split()
for k in range(len(x)):
    for m in range(len(x)-1):
        for i in range(1+m+k,len(x)):
            if x[i] > x[k]: x[i], x[k] = x[k], x[i]
print(x[len(x)//2])