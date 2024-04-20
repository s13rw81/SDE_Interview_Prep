fruits = ['apple', 'orange', 'banana', 'grape', 'strawberry', 'blueberry', 'mango']
prices = [1.25, 0.75, 0.50, 2.00, 3.50, 4.00, 1.75]

fruit_prices = [(fruit, price) for fruit, price in zip(fruits, prices)]

filtered_fruit_prices = [fp for fp in fruit_prices if 1 <= fp[1] <= 3]
sorted_fruit_prices = sorted(filtered_fruit_prices, key=lambda x: x[1], reverse=True)
print(sorted_fruit_prices)

filtered_fruit_prices = [(fruit, price) for fruit, price in zip(fruits, prices) if 1 <= price <= 3]
fruit_prices = sorted(filtered_fruit_prices, key=lambda x: x[1], reverse=True)
print(fruit_prices)

fruit_prices = [(fruit, price) for fruit, price in zip(fruits, prices) if 1 <= price <= 3]
filtered_fruit_prices = sorted(fruit_prices, key=lambda x: x[1], reverse = True)
print(filtered_fruit_prices)

fruit_prices = [(fruit, price) for fruit, price in zip(fruits, prices)]
filtered_fruit_prices = [fp for fp in fruit_prices if 1 <= fp[1] <= 3]
sorted_fruit_prices = sorted(filtered_fruit_prices, key=lambda x: x[1], reverse = False)
print(sorted_fruit_prices)