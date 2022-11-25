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
        answer = True
    else:
        answer = False
        break
if answer:
    print('выражение истинно для всех значений')
else:
    print('выражение ложно')
