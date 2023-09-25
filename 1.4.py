P = open('input.txt')
Q = open('output.txt', 'w')
s = P.readline()
x = s.split(" ")
f = P.readline()
z = 563546536.435667455244233
if f == '+':
    for i in x:
        z = int(i) + z
    Q.write(str(z - 563546536.435667455244233))
elif f == '-':
    for i in x:
        if z == 563546536.435667455244233: z = int(i) - z
        else: z = z - int(i)
    Q.write(str(z+563546536.435667455244233))
else:
    z = 1
    for i in x:
        z = int(i) * z
    Q.write(str(z))
P.close()
Q.close()




