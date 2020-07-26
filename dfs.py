# Подсчет компонент связности в неориентированном графе
# v - количество вершин (нумеруются от 1)
# e - количество ребер, задаются парами смежных вершин
import sys


sys.setrecursionlimit(100000000)
v, e = map(int, input().split())
adjlist = [list() for i in range(v)]
for i in range(e):
    v1, v2 = map(int, input().split())
    if v1 != v2:
        if v2 not in adjlist[v1 - 1]:
            adjlist[v1 - 1].append(v2)
        if v1 not in adjlist[v2 - 1]:
            adjlist[v2 - 1].append(v1)
visited = [False] * v

def dfs(s):
    visited[s - 1] = True
    for j in adjlist[s - 1]:
        if not visited[j - 1]:
            dfs(j)

c = 0
for i in range(1, v + 1):
    if not visited[i - 1]:
        dfs(i)
        c += 1
print('Число компонент связности = %d' % d)
