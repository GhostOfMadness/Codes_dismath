# Поиск кратчайших путей из вершины 0 в любую другую вершину
# Граф является простым и связным
# v - количество вершин (нумеруются от 0)
# e - количество ребер (задаются парами смежных вершин)
import sys


sys.setrecursionlimit(100000000)
v, e = map(int, input().split())
adjlist = [list() for i in range(v)]
for i in range(e):
    v1, v2 = map(int, input().split())
    adjlist[v1].append(v2)
    adjlist[v2].append(v1)
s = 0
q = [s]
path = [0] * v
visited = [False] * v
def bfs(s):
    visited[s] = True
    for w in adjlist[s]:
        if visited[w] == False and w not in q:
            q.append(w)
            path[w] = path[s] + 1
    q.pop(0)
    if len(q) > 0:
        for i in q:
            bfs(i)
    return path
# Результат - список длин путей от вершины 0 в порядке неубывания
print(*bfs(s))
