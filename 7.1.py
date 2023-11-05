class vector():
    def __init__(self, x, y, z):
        self.x = float(x)
        self.y = float(y)
        self.z = float(z)

print('Введите поочередно тройку координат 1-го вектора.')
first_vector = vector(input(),input(),input())
print('Введите поочередно тройку координат 2-го вектора.')
second_vector = vector(input(),input(),input())
print('Введите число:')
a = float(input())


def abs(self):
    return ((self.x**2+self.y**2+self.z**2)**0.5)

print('Длины векторов соответственно:', abs(first_vector), 'и', abs(second_vector))

def summ(first_vector, second_vector):
    return vector(first_vector.x + second_vector.x, first_vector.y + second_vector.y, first_vector.z + second_vector.z)

print('Вектор суммы имеет координаты:', summ(first_vector,second_vector).x, summ(first_vector,second_vector).y, summ(first_vector,second_vector).z)

def diff(first_vector, second_vector):
    return vector(first_vector.x - second_vector.x, first_vector.y - second_vector.y, first_vector.z - second_vector.z)

print('Вектор разности имеет координаты:', diff(first_vector,second_vector).x, diff(first_vector,second_vector).y, diff(first_vector,second_vector).z)

def mult(first_vector, second_vector):
    return (0.5*( abs(first_vector)**2 + abs(second_vector)**2 - abs(diff(first_vector, second_vector))**2 ))
print('Скалярное произведение составляет:', mult(first_vector, second_vector))

def const(self,a):
    return vector(self.x*a, self.y*a, self.z*a)
print('Произведения векторов на введенное число соответственно:', const(first_vector, a).x, const(first_vector, a).y, const(first_vector, a).z, 'и', const(second_vector, a).x, const(second_vector, a).y, const(second_vector, a).z)