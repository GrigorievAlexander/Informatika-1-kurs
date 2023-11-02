import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

X = pd.read_csv('IRIS_data.csv')
S = []
N = []

for i in range(len(X)):
    for n in X.Species:
        if n not in N:
            N = N + [n]

K = [0]*len(N)

for i in range(len(N)):
    for n in X.Species:
        if n == N[i]:
            K[i] = K[i] + 1/len(X)

plt.pie(K, labels = N)
plt.title('Доли ирисов')
plt.show()

s1 = 0
s2 = 0
s3 = 0

for i in range(len(X)):
    if X.PetalLengthCm[i] > 1.5: s1 = s1 + 1
    if X.PetalLengthCm[i] < 1.2: s2 = s2 + 1
    else: s3 = s3 + 1

plt.pie([s1,s3,s2], labels = ['Больше 1,5 см', 'От 1,2 до 1,5 см', 'Меньше 1,2 см'])
plt.title('Длина ирисов')
plt.show()