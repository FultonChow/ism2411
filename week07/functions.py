#  In exercise 5, the first thing I spotted was the missing colon on line 10, I feel like it was easy to spot because the coding ai already was showing me the error and it just looked abnormal. Then the error logs pointed out the other error in line 16 which did not come immediately but then also ai looked at the termial and game me a few ideas to what my error could of been.
# The apply discount function works by combining the given prices and then the given dicount which is followed by what teir you fall into. I think a college could use this without reading the body because the instructions are clear and simple enough to display.
#  I used claude/ google gemni to explain terminal errors and a further explination of error logs which gave me mulitple differnet possiblitys to what the error could have been and how each problem would most likey need to be handled.
# --- Exercise 1 ---

# Define calculate tax function

def calculate_tax(price, rate):
    return price * rate

# calling the function

tax1 = calculate_tax(100, 0.07)
tax2 = calculate_tax(250, 0.08)

print("Tax on $100 at 7%: ${:.2f}".format(tax1))
print("Tax on $250 at 8%: ${:.2f}".format(tax2))
print("Another Tax: ${:.2f}".format(calculate_tax(500, 0.05)))

# --- Exercise 2 ---

def apply_discount(price, tier):
    if tier == "gold":
        return price * 0.85
    elif tier == "silver":
        return price * 0.90
    elif tier == "bronze":
        return price * 0.95
    else:
        return price

price = 200
tiers = ["gold", "silver", "bronze"]

for tier in tiers:
    print(f"{tier}: ${apply_discount(price, tier):.2f}")

# --- Exercise 3 ---
discount = apply_discount(200, "gold") #use below
tax = calculate_tax(discount, 0.07)
after_tax = discount + tax
print(f"After gold discount: ${discount:.2f}")
print(f"After Tax: ${after_tax:.2f}")



def final_price(price, tier, tax_rate):
    discounted = apply_discount(price, tier)
    tax = calculate_tax(discounted, tax_rate)
    return discounted + tax

print(f"Final price: ${final_price(200, 'gold', 0.07):.2f}")

# --- Exercise 4 ---

orders = [(200, "gold"), (150, "silver"), (80, "bronze"), (500, "none")]

for price, tier in orders:
    total = final_price(price, tier, 0.07)
    print(f"Price: ${price:.2f}, Tier: {tier}, Final: ${total:.2f}")
print()

# --- Exercise 5 ---
# broken_sales.py - trace and diagnose before fixing anything.
sales = [120, 80, 250, 175, 90]

total = 0
for sale in sales:
    total += sale      # now it will not add them all up toghether, but will only do that last number instead
print(f"Total: ${total}")

count = 0
for sale in sales:   # I added : so it's a valid for loop
    count += 1
print(f"Count: {count}")

i = 0
while i < len(sales):   # I got rid of the equal sign beacuse it was causing an index out of range error and "i" could not be read properly.
    print(sales[i])
    i += 1

# --- Exercise 6 ---

x = 100

def double_it():
    x = 999
    return x * 2

print(x)
print(double_it())
print(x)