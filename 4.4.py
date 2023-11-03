import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

T = pd.read_csv('IRIS_data.csv')

f = plt.figure(figsize=(16,9))
f1 = f.add_subplot(611)
f2 = f.add_subplot(612)
f3 = f.add_subplot(613)
f4 = f.add_subplot(614)
f5 = f.add_subplot(615)
f6 = f.add_subplot(616)

x1 = np.array(T.SepalLengthCm)
y1 = np.array(T.SepalWidthCm)

x2 = np.array(T.SepalLengthCm)
y2 = np.array(T.PetalLengthCm)

x3 = np.array(T.SepalLengthCm)
y3 = np.array(T.PetalWidthCm)

x4 = np.array(T.SepalWidthCm)
y4 = np.array(T.PetalLengthCm)

x5 = np.array(T.SepalWidthCm)
y5 = np.array(T.PetalWidthCm)

x6 = np.array(T.PetalLengthCm)
y6 = np.array(T.PetalWidthCm)

z1 = np.polyfit(x1, y1, 1)
Y1 = np.polyval(z1, x1)
p1 = np.poly1d(z1)
print(p1)
f1.plot(x1, Y1, 'black',label = 'Зависимость ширины ириса от длины ириса')

z2 = np.polyfit(x2, y2, 1)
Y2 = np.polyval(z2, x2)
p2 = np.poly1d(z2)
print(p2)
f2.plot(x2, Y2, 'b',label = 'Зависимость длины лепестка от длины ириса')

z3 = np.polyfit(x3, y3, 1)
Y3 = np.polyval(z3, x3)
p3 = np.poly1d(z3)
print(p3)
f3.plot(x3, Y3, 'r',label = 'Зависимость ширины лепестка от длины ириса')

z4 = np.polyfit(x4, y4, 1)
Y4 = np.polyval(z4, x4)
p4 = np.poly1d(z4)
print(p4)
f4.plot(x4, Y4, 'b--',label = 'Зависимость длины лепестка от ширины ириса')

z5 = np.polyfit(x5, y5, 1)
Y5 = np.polyval(z5, x5)
p5 = np.poly1d(z5)
print(p5)
f5.plot(x5, Y5, 'r--',label = 'Зависимость ширина лепестка от ширины ириса')

z6 = np.polyfit(x6, y6, 1)
Y6 = np.polyval(z6, x6)
p6 = np.poly1d(z6)
print(p6)
f6.plot(x6, Y6, 'g--',label = 'Зависимость ширины лепестка от длины лепестка')

f1.scatter(x1,y1, marker='x')
f1.grid()
f2.scatter(x2,y2, marker='x')
f2.grid()
f3.scatter(x3,y3, marker='x')
f3.grid()
f4.scatter(x4,y4, marker='x')
f4.grid()
f5.scatter(x5,y5, marker='x')
f5.grid()
f6.scatter(x6,y6, marker='x')
f6.grid()
plt.show()