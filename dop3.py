"""dop3"""
x = int(input('give me x '))
y = int(input('give me y '))
if x > 0 and y > 0:
    print(f'точка х={x},у={y} лежит в первой четверти')
elif x < 0 and y > 0:
    print(f'точка х={x},у={y} лежит во второй четверти')
elif x < 0 and y < 0:
    print(f'точка х={x},у={y} лежит в третьей четверти')
elif x > 0 and y < 0:
    print(f'точка х={x},у={y} лежит в четвертой четверти')
elif x == 0:
    print(f'точка х={x},у={y} лежит на оси У')
elif y == 0:
    print(f'точка х={x},у={y} лежит на оси Х')
