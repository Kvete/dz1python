"""dop2"""
mas = [[0, 0, 0],
       [0, 0, 1],
       [0, 1, 0],
       [0, 1, 1],
       [1, 0, 0],
       [1, 0, 1],
       [1, 1, 0],
       [1, 1, 1]]
for i in range(len(mas)):
    if not (mas[i][0] or mas[i][1] or mas[i][2]) == (
            not (mas[i][0]) and not (mas[i][1]) and not (mas[i][2])):
        print(
            f'выражение истинно для значений X={mas[i][0]}, Y={mas[i][1]}, Z ='
            f'{mas[i][2]}')
    else:
        print(
            f'выражение  ложно  для значений X={mas[i][0]}, Y={mas[i][1]}, Z ='
            f'{mas[i][2]}')
