def dist(a, b):
    return ((b[0] - a[0])**2 + (b[1] - a[1])**2)**0.5

N = int(input())
P = []
for _ in range(N):
    P.append(list(map(float, input().split())))

def f(G):
    S = []
    if len(G) == 2: return dist(G[0], G[1])
    else:

        for i in G:
            for j in G:
                if i != j:
                    G1 = G + []
                    if i > j:
                        G1.remove(i)
                        G1.remove(j)
                    if i < j:
                        G1.remove(j)
                        G1.remove(i)
                    S.append(dist(i, j) + f(G1))
        return min(S)

print(f(P))