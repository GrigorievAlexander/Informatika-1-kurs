X = list(map(int, input().split()))
Y = list(map(int, input().split()))
XY = []
X1 = []
Y1 = []


for x in X:
    if x in Y:
        XY = XY + [x]

for x in X:
    if x not in XY:
        X1 = X1 + [x]
print('Уникальные для 1-го списка: ', X1)

for y in Y:
    if y not in XY:
        Y1 = Y1 + [y]
print('Уникальные для 2-го списка: ', Y1)

print('Уникальные для объединения: ', X1+Y1)

print('Содержащиеся в обоих списках: ', XY)