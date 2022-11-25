"""task4"""
n = int(input('give me number '))
max_digit = 0
while n > 0:
    if max_digit < n % 10:
        max_digit = n % 10
    n = n // 10
print(f'max digit in number={max_digit}')
