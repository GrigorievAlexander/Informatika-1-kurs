x = input().split(' ')
for i in range (1, len(x)+1):
    i = str(i)
    if i in x[1:]: pass
    else: print(i)