"""task5"""
revenue = int(input('give me revenue '))
costs = int(input('give me costs '))
profit = revenue - costs
if profit > 0:
    print(f'you have profit={profit}')
    print(f'your profitability(profit/revenue)= {profit / revenue}')
    people = int(input('give me numbers of employees '))
    print(f'your profit per one employee= {profit / people}')
else:
    print(f'you have loss, your profit={profit}')
