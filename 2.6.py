x = input().split()
n = 0
s = str()

for i in x:
    for m in x:
        if i == m:
            n = n + 1

    if n == 1:
        s = s + i
        print(s)
    n = 0
    s = str()