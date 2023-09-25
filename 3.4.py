x = int(input())
s = input()
n = 0
for i in range(x//2):
    n = n + 1
    print(s*n)
if x%2 == 1: print(s*(x//2+1))
m = x//2+1
for i in range(x // 2):
    m = m - 1
    print(s*m)
