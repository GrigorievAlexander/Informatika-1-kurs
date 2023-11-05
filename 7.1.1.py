class vector():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

print('Сколько точек?')
n = int(input())
V = []
M = []
xm = 0
ym = 0
zm = 0
m = 0
for i in range(n):
    print('Введите массу (относительную массу)', i+1,'- ой точки.')
    M = M + [int(input())]
    print('Введите поочередно координаты', i+1,'- ой точки.')
    V = V + [vector(input(),input(),input())]

for i in range(n):
    xm = xm + V[i].x*M[i]
    ym = ym + V[i].y*M[i]
    zm = zm + V[i].z*M[i]
    m = m + M[i]

print('Координаты центра масс:', xm/m, ym/m, zm/m)

