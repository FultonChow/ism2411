# Reflection questions:
# 1. You should use the brackets when a key must exist and you want it to fail fast if missing. Use the get() method when a key may not exist and you want to provide a default value instead of raising an error.
# 2. This pattern is just like an Excel pivot table. The python version is better for large data sets and that goes without saying cause dats sets could get up to the millions. This will not cause any freezing like excel would do.
print("---Exercise 11")
customer = {
    "name": "Alice",
    "email": "alice@example.com",
    "tier": "Gold",
    "ytd_spend": 12400,
}

print("---Exercise 2---")
customer['phone'] = "813-555-0142"

print(customer)
customer['tier'] = "Platinum"

print(customer)
del customer["email"]

print(customer)

print(customer.get("email", "Email not found"))

print("---Exercise 3---")

print(customer.get("email", "no email on file"))

#try:
    #print(customer["email"])
#except KeyError as error:
    #print(f"KeyError Caught: {error}")
print("---Exercise 4---")
for key, value in customer.items():
    print(f"{key}: {value}")

for item in customer: 
    print(item)
print("---Exercise 5---")
tier_discounts = {"bronze": 0,
                    "silver": 0.05,
                    "gold": 0.10,
                    "platinum": 0.15}
purchase_amount = 200
discount_rate =tier_discounts.get(customer["tier"], 0)
final_price = purchase_amount * (1 - discount_rate)

print(f"Tier: {customer['tier']}")
print(f"Discount: {discount_rate * 100:.0f}%")
print(f"Final Price: ${final_price:.2f}")
print("---Exercise 6---")
customer2 = [
    {"name": "Bob", "tier": "Silver", "ytd_spend": 3200},
    {"name": "Carol", "tier": "Gold", "ytd_spend": 8750},
    {"name": "David", "tier": "Bronze", "ytd_spend": 450},
]

for record in customer2:
    rate = tier_discounts.get(record["tier"].lower(), 0)
    discount = 300 * rate
    print(f"{record['name']} ({record['tier']}): ${discount:.2f} discount on 300 purchase")

print("---Exercise 7---")
customer = {
    "Widget A": {"price": 9.99, "stock": 150},
    "Gadget C": {"price": 49.99, "stock": 8},
}

for product, details in customer.items():
    if details["stock"] < 20:
        print(f"LOW STOCK: {product} - Only {details['stock']} left in stock!")

print("---Exercise 8---")
transactions = [
    {"region": "South", "amount": 300},
    {"region": "North", "amount": 150},
    {"region": "South", "amount": 200}
]
sales_by_region = {}

for tx in transactions:
    region = tx["region"]
    amount = tx["amount"]
    sales_by_region[region] = sales_by_region.get(region, 0) + amount

for region in sorted(sales_by_region):
    print(f"{region}: ${sales_by_region[region]:.2f}")
