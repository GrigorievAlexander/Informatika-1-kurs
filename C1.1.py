T = list(map(int, input().split()))
s = 0
x = 0
y = 0

for i in range(len(T)):
    if i%2 == 1:
        x = max(x + T[i], y)
    else:
        y = max(y + T[i], x)
s = s + max(x, y)

print(s)
