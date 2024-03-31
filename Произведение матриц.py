print('Введите количество перемножаемых матриц.')
n = int(input())

A = []
B = []
C = []
s = 0

print('Введите размер 1-ой матрицы.')
[h1, l1] = list(map(int, input().split()))
print('Введите 1-ую матрицу.')
for i in range(h1):
    A = A + list(map(int, input().split()))


for i0 in range(2, n+1):

    if i0 % 10 != 3: print('Введите размер ', i0, '-ой матрицы.', sep='')
    else: print('Введите размер ', i0, '-ей матрицы.', sep='')
    [h2, l2] = list(map(int, input().split()))

    if l1 != h2:
        print('Произведение НЕ определено! Проверьте размеры введенных матриц.')
        s = 1
    else:

        if i0 % 10 != 3: print('Введите ', i0, '-ую матрицу.', sep='')
        else: print('Введите ', i0, '-тью матрицу.', sep='')
        B = []
        for i in range(h2):
            B = B + list(map(int, input().split()))

        C = []
        for i in range(1, h1+1):
            for j in range(1, l2+1):
                c = 0
                for k in range(1, l1+1):
                    c = c + A[(i-1)*l1 + k - 1] * B[(k-1)*l2 + j - 1]
                C.append(c)

        A = C
        l1 = l2

if s == 0:
    print('Произведение матриц:')
    s = str()
    for i in range(1, h1+1):
        for j in range(1, l1+1):
            s = s + str(A[j + (i-1)*l1 - 1]) + ' '
        print(s)
        s = str()