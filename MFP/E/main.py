dists = {}

def dist(x1, y1, x2, y2):
    return ((x1-x2)**2 + (y1-y2)**2)**0.5


def bfs(inicio, final, grafo):
    if inicio == final: return True
    visitados = [inicio]
    next = [i for i in grafo[inicio]]
    
    while next:
       atual = next.pop(0)
       if atual in visitados: continue
       visitados.append(atual)

       if atual == final: return True

       for i in grafo[atual]:
           next.append(i)
    return False


def solve():
    s1, s2 = map(int, input().split())

    print("S" if bfs(s1-1,s2-1,grafo) else "N")
        
        

n, q, d = map(int, input().split())
q+=1

sedes = []
for _ in range(n):
    x, y = map(int, input().split())
    sedes.append((x, y))

grafo = {}
for i in range(n):
    for j in range(3):
        if i == j: continue
        if i not in grafo: grafo[i] = []
        if dist(sedes[i][0], sedes[i][1], sedes[j][0], sedes[j][1]) <= d:
            grafo[i].append(j)

print(grafo)

while (q:=q-1): solve()

