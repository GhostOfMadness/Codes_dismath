v, e = map(inr, input().split())
adjlist = [list() for i in range(v)]
for i in range(e):
    # Ребра задаются парой вершин
    v1, v2 = map(int, input().split())
    # Формируем список смежности
    if v1 == v2:
        adjlist[v1 - 1].append(v1)
        adjlist[v1 - 1].append(v1)
    else:
        adjlist[v1 - 1].append(v2)
        adjlist[v2 - 1].append(v1)
# Если у всех вершин четная степень, то счетчик равен числу вершин v
c = sum(1 for e in adjlist if len(e) % 2 == 0 and len(e) != 0)
visited = [False] * v
def dfs(s):
    visited[s - 1] = True
    for w in adjlist[s - 1]:
        if not visited[w - 1]:
            dfs(w)
# k - счетчик компонент связности
k = 0
for i in range(1, v + 1):
    if not visited[i - 1]:
        dfs(i)
        k += 1
# Для существования эйлерова цикла:
# 1. k = 1 (граф связный)
# 2. c = v (все вершины имеют четную степень)
if c != v or k != 1:
    print('NONE')
else:
    # Ищется произвольный цикл из веришны 1, удаляются пройденные ребра
    # Затем из вершин, которые не стали изолированными, ищутся другие циклы
    stack = [1]
    path = []
    while len(stack) > 0:
        top = stack[-1]
        if len(adjlist[top - 1]) > 0:
            newtop = adjlist[top - 1][0]
            stack.append(newtop)
            adjlist[top - 1].remove(newtop)
            adglist[newtop - 1].remove(top)
        else:
            path.append(top)
            stack.pop(-1)
        last = len(path) - 1
        print(*path[: last])
