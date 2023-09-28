X = input()
l = int(input())
Y = str()
for i in range(len(X)//l):
    s = X[l*i:l*(i+1)]
    s = s[::-1]
    Y = Y + s
print(Y)