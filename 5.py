N = int(input(), 2)
b = int(input())
c = int(input())
x = str()
s = N
N = str(N)
for i in range(0, len(N)):
    x = str(x) + str(s%c)
    s = s//c
print(x + str(s) [::-1])



