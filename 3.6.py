X = input().split()
Y = input().split()

k = len(X)
smX = 0
smY = 0
smXY = 0
smX2 = 0

if len(X) != len(Y): print("Некорректно введенные данные")
else:

    for i in range(k):
        smX = smX + float(X[i])
        smY = smY + float(Y[i])
        smXY = smXY + (float(X[i]) * float(Y[i]))
        smX2 = smX2 + (float(X[i])**2)

    srX = smX / k
    srY = smY / k
    srXY = smXY / k
    srX2 = smX2 / k

    b = (srXY - srX*srY) / (srX2 - (srX)**2)
    a =  srY - b*srX

    print("Угловой коэффициент прямой апроксимации: ",b)
    print("Свободный член прямой апроксимации: ",a)