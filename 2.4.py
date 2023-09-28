X = input(); Y = str();
for i in range(len(X)//3): s = X[4*i:4*i+3]; s = s[::-1]; Y = Y + s + ' '
print(Y)