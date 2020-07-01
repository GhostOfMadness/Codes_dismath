mn = list(map(int, input().split()))
m = mn[0] # количество уравнений
n = mn[1] # количество переменных
# Ввод расширенной матрицы СЛАУ
matx = []
for i in range(m):
    matx.append(list(map(int, input().split())))
i = 0
j = 0
# Прямой ход метода Гаусса
while j < n  and i < m - 1:
    matx.sort(key=lambda x: list(map(abs, x)), reverse=True)
    if abs(matx[i][j]) > 0.0000001:
        for k in range(i + 1, m):
            coef = -matx[k][j] / matx[i][j]
            for u in range(j, n + 1):
                matx[k][u] = matx[k][u] + coef * matx[i][u]
        i += 1
        j += 1
    else:
        j += 1
# matx - ступенчатая расширенная матрица
# Считаем ранг расширенной матрицы
rangbig = 0
for i in range(len(matx)):
    c = 0
    for j in range(len(matx[i])):
        if abs(matx[i][j]) > 0.0000001:
            c += 1
    if c > 0:
        rangbig += 1
# Считаем ранг основной матрицы
rangsmall = 0
for i in range(len(matx)):
    c = 0
    for j in range(len(matx[i]) - 1):
        if abs(matx[i][j]) > 0.0000001:
            c += 1
    if c > 0:
        rangsmall += 1
# Теорема Кронекера-Капелли
if rangbig != rangsmall:
    print('NO')
else:
    if rangbig < n:
        print('INF')
    else:
        # обратный ход метода Гаусса
        for i in range(n - 1, 0, -1):
            for k in range(i - 1, -1, -1):
                coef = -1 * matx[k][i] / matx[i][i]
                for u in range(len(matx[k])):
                    matx[k][u] = matx[k][u] + coef * matx[i][u]
        print('YES')
        # Теперь matx - диагональная матрица (относительно исходной матрицы А)
        res = [matx[i][-1] / matx[i][i] for i in range(n)]
        print(*res)
