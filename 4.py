open("main.txt", "r")
s = input()
x = s.split(" ")
f = input()
z = 563546536.435667455244234
if f == '+':
    for i in x:
        z = int(i) + z
    print(z - 563546536.435667455244234)
elif f == '-':
    for i in x:
        if z == 563546536.435667455244234: z = int(i) - z
        else: z = z - int(i)
    print(z+563546536.435667455244234)
else:
    z = 1
    for i in x:
        z = int(i) * z
    print(z)




