with open("input.txt", "r") as t: x = t.read()
n = 0
m = 0
k = 0
l = 0

S4 = ['?...', '!...']
S1 = ['.', '?', '!']

for i in range(len(x)):

    if x[i:i + 4] in S4: n = n + 1
    if x[i:i + 3] == '...': m = m + 1
    if x[i:i + 2] == '?!': k = k + 1
    if x[i] in S1: l = l + 1

print(l - k - 2*m - 3*n)