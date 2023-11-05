class vector():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

print('Сколько точек?')
n = int(input())
V = []
m = 0
for i in range(n):
    print('Введите поочередно координаты', i+1,'- ой точки.')
    V = V + [vector(input(),input(),input())]

for i1 in range(n):
    for i2 in range(n):
        for i3 in range(n):
            a = ((V[i1].x - V[i2].x)**2 + (V[i1].y - V[i2].y)**2 + (V[i1].z - V[i2].z)**2)**0.5
            b = ((V[i1].x - V[i3].x)**2 + (V[i1].y - V[i3].y)**2 + (V[i1].z - V[i3].z)**2)**0.5
            c = ((V[i3].x - V[i2].x)**2 + (V[i3].y - V[i2].y)**2 + (V[i3].z - V[i2].z)**2)**0.5
            p = 0.5*(a + b + c)
            S = (p*(p-a)*(p-b)*(p-c))**0.5
            if S > m: m = S

print(m)