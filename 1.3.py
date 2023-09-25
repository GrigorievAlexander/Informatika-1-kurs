A = input().split()
print(A)
P = 1
n = 0
for i in A:
    P = P * int(i)
    n = n + 1
print(P**(1/n))
