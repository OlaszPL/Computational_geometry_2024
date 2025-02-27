# połączenie tego samego rodzaju danych

import pandas as pd

df = pd.read_csv('D.csv')

result = {}

for i in range(len(df.index)):
    Type,Eps,mat_det_func,Left,Mid,Right = df.iloc[i]
    key = (Left, Mid, Right)
    if Eps == 0.0:
        Eps = 0
    if not key in result:
        result[key] = (set([Type]), set([Eps]), set([mat_det_func])) # Type, Eps, mat_det_func
    else:
        result[key][0].add(Type)
        result[key][1].add(Eps)
        result[key][2].add(mat_det_func)

# generowanie kolumn do typsta

for key in result:
    Type, Eps, mat_det_func = result[key]
    Left, Mid, Right = key
    # [*Precyzja*],[$bold(epsilon)$],[*Funkcja liczenia wyznacznika*],
    # [*Punkty na lewo od prostej*],[*Punkty\ na prostej*],
    # [*Punkty na prawo od prostej*],
    print("[", end='')
    for t in Type:
        print(t, "\\ ", end='')
    print("],", end='')
    print("[", end='')
    for e in Eps:
        print(e, "\\ ", end='')
    print("],", end='')
    print("[", end='')
    for m in mat_det_func:
        print(m, "\\ ", end='')
    print("],", end='')
    print("[", Left, "], ", end='')
    print("[", Mid, "], ", end='')
    print("[", Right, "], ")