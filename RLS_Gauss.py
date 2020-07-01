nm = list(map(int, input().split()))
n = nm[0] # количество уравнений
m = nm[1] # количество неизвестных
# Исходная матрица
matx = []
for i in range(n):
    matx.append(list(map(int, input().split())))
# Преобразование исходной матрицы в расширенную матрицу СЛАУ размером m*(m+1)
# В векторной форме МНК сводится к поиску координат вектора правых частей
# в линейном m-мерном подпространстве (m - кол-во регрессоров)
linsys = []
for i in range(m):
    line = []
    for j in range(m + 1):
        s = 0
        for k in range(n):
            s += matx[k][i] * matx[k][j]
        line.append(s)
    linsys.append(line)
# Прямой ход метода Гаусса
i = 0
j = 0
while j < m - 1 and i < m - 1:
    linsys.sort(key=lambda x: list(map(abs, x)), reverse=True)
    if linsys[i][j] != 0:
        for k in range(i + 1, m):
            coef = -linsys[k][i] / linsys[i][j]
            for u in range(len(linsys[k])):
                linsys[k][u] = linsys[k][u] + coef * linsys[i][u]
        i += 1
        j += 1
    else:
        j += 1
# Ранг расширенной матрицы
rangbig = 0
for i in range(len(linsys)):
    c = 0
    c = sum(1 for e in linsys[i] if abs(e) > 0.0000001)
    if c != 0:
        rangbig += 1
# Ранг основной матрицы
rangsmall = 0
for i in range(len(linsys)):
    c = 0
    c = sum(1 for e in linsys[i][:m] if abs(e) > 0.0000001)
    if c != 0:
        rangsmall += 1
# Теорема Кронекера-Капелли
if rangbig != rangsmall:
    print('Система не имеет решений')
if rangbig == rangsmall:
    if rangbig < m:
        print('Система имеет бесконечное множество решений')
    if rangbig == m:
        # Обратный ход метода Гаусса
        for i in range(m - 1, 0, -1):
            for k in range(i - 1, -1, -1):
                coef = -linsys[k][i] / linsys[i][i]
                for u in range(len(linsys[k])):
                    linsys[k][u] = linsys[k][u] + coef * linsys[i][u]
        res = [linsys[i][m] / linsys[i][i] for i in range(m)]
        print('Система имеет единственное решение')
        print(*res)
