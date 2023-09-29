x = input().split()
k = -1
n = 0
r = 0
m = str()

for i in x:
    k = k + 1
    for m in x:
        if i == m: n = n + 1
        if n>r:
            r = n
            s = m
            n = 0
            
print(s)