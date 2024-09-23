coffee_price = 1.99
doughnut_price = 2.49
discount = 0.87
friends_number = 3

cost = coffee_price + doughnut_price 

print('стоимость кофе:', coffee_price)
print('стоимость пончика:', doughnut_price)
print('общая стоимость:', cost)

cost -= discount
cost = round(cost, 2)
print('общая стоимость со скидкой:', cost)

cost *= friends_number
print('общая стоимость на всех:', cost)

# ваш код

