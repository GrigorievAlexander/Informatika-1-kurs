a = int(input())
b = int(input())
t = str()
u = str()
for i in range(1,a+1):
    if a%i==0 and b%i==0: s = i
p = s*(2+abs(2*a*b))
m = s*(2+abs(2*a*b))
for x in range(-m,m):
    y = (s - a * x) / b
    for n in range(1,1+int(abs(y))):
        if y%n == 0 and abs(x)+abs(y)<p:
            p = abs(x) + abs(y)
            t = str(x)
            u = str(int(y))
print(t)
print(u)
print(s)
