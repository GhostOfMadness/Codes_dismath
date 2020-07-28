import sys


sys.setrecursionlimit(1000000000)
v, e = map(int, input().split())
adjlist = [list() for i in range(v)]
for i in range(e):
    v1, v2 = map(int, input().split())
    adjlist[v1 - 1].append(v2)
    adjlist[v2 - 1].append(v1)
visited = [False] * v
# Все вершины красятся в 2 цвета: 1 и 2
color = [0] * v
def dfs(s):
    visited[s - 1] = True
    # concom содержит все вершины, входящие в одну компненту связности
    concom.append(s)
    for w in adjlist[s - 1]:
        if not visited[w - 1]:
            if color[s - 1] == 1:
                color[w - 1] = 2
            else:
                color[w - 1] = 1
            dfs(w)
# c - счетчик "ошибок"
c = 0
for i in range(1, v + 1):
    if not visited[i - 1]:
        concom = []
        # Первая вершина каждой компоненты связности окрашена в цвет 1
        color[i - 1] = 1
        # Проверка, что смежные вершины покрашены в разные цвета
        # И это верно для каждой вершины из найденной компоненты связности
        for ver in concom:
            for adjv in adjlist[ver - 1]:
                if color[ver - 1] == color[adjv - 1]:
                    c += 1
if c != 0:
    # Есть смежные вершины, окрашенные в один цвет
    print('NO')
else:
    print('YES')
