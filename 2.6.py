x = input().split()
n = 0
for i in x:
    s = str()
    for m in x:
        if i == m:
            n = n + 1
            s = s + m
    if n == 1:
        print(s)
    n = 0