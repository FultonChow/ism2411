""""""
# 1. Coming into Python, I thought scripts were very hard to understand even after typing and to realize that here in the terminal, the output results in just one or two work answers shows me how truly dominant coding is and that it can minimize work loads. Just hope my job doesnt get taken by AI doing this type of work.
# 2. When I used to work at Culvers, I would have to wake up really early on the weekends to help with inventory and we had to go into the freezer and directly count everything in there and I wasnt even a manager so I didnt even have a jacket. If I could use these lists to track imports and exports it wouldnt be such a hard tasks tracking inventory.
""""""
#Exercise 1
from ast import pattern


print("---Exercise 1: Build the list ---")
inventory = ["pen", "notebook", "stapler", "tape", "marker"]
print(inventory)
print(len(inventory))
print()

#Exercise 2
print("---Exercise 2: Index practice ---")
print(inventory[0])
print(inventory[-1])

middle_index = len(inventory) // 2
print(inventory[middle_index])
print()

#Exercise 3: Slicing
print("---Exercise 3: Slicing ---")
print(inventory[0:3])
print(inventory[-2:])
print(inventory[::2])
print()

#Exercise 4: Modifying 
print("---Exercise 4: Modifying ---")
inventory.append("envelope")
print(inventory)

inventory.remove("tape")
print(inventory)

inventory.sort()
print(inventory)
print()

#Exercise 5: tuple comparison
print("---Exercise 5: Tuple comparison ---")
coords = (40.7128, -74.0060)

try:
    coords[0] = 99
except TypeError:
    print("typeError caught successfully!")
    print("Explanation: Tuples are immutable, meaning their elements cannot be changed after creation.")
    print("This makes them reliable for fixed data like GPS cordinates.")

print(coords)
print()

#Exercise 6: Average of a list of sales
print("---Exercise 6: Average of a list of sales ---")
sales = [100, 250, 75, 480, 200]

total_sales = sum(sales)
count_sales = len(sales)
average_sales = total_sales / count_sales
best_day = max(sales)
worst_day = min(sales)

print(f"Total sales: {total_sales}")
print(f"Average sales: {average_sales}")
print(f"Best: {best_day}")
print(f"Worst: {worst_day}")
print()

#Exercise 7: Accumulator pattern
print("---Exercise 7: Accumulator pattern ---")
prices = [9.99, 14.99, 4.99, 24.99, 1.99]
discounted_prices = [] 

for price in prices:
    new_price = round(price * 0.90, 2)
    discounted_prices.append(new_price)

print(prices)
print(discounted_prices)
print()

#Exercise 8: Filter abouve the threshold
print("---Exercise 8: Filter above the threshold ---")
sales_data = [340, 127, 589, 204, 467, 88, 731, 315, 62, 490]
high_sales = []

for sale in sales_data:
    if sale > 300:
        high_sales.append(sale)

count_high = len(high_sales)
avg_high = round(sum(high_sales) / count_high, 2)

print(high_sales)
print(f"Count: {count_high}")
print(f"Average: {avg_high}")
