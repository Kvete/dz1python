"""dop1"""
day = int(input('give me day '))
if 0 < day < 6:
    print(f'day {day} is a workday')
elif 5 < day < 8:
    print(f'day {day} is a holiday')
else:
    print(f'{day} is not day of a week')
