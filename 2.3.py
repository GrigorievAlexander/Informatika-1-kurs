x = input()
n = 0

S = ['A', 'H', 'I', 'M', 'O', 'T', 'U', 'V', 'W', 'X', 'Y', '1', '8']

for i in range(len(x)):
    if x[i] in S:
        n = n + 1

if n == len(x) and x == x[::-1]:
    print(x, "is a mirrored palindrome")
else:

    for i in range(len(x)):
        if (x[i] == 'E' and x[len(x)-i-1] == '3') or (x[i] == 'J' and x[len(x)-i-1] == 'L') or (x[i] == 'S' and x[len(x)-i-1] == '2') or (x[i] == 'Z' and x[len(x)-i-1] == '5'):
            n = n + 1
        if x[i] == x[len(x)-i-1] and x[i] != S:
            n = n + 1

    if n == len(x):
        print(x, "is a mirrored string")
    else:

        if x == x[::-1]: print(x, "is a regular palindrome")
        else:
            print(x, "is not a palindrome")
