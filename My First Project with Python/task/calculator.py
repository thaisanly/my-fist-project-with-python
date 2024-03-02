# Write your code here

# name = input("What's your name?")
# print(f"Hello, {name}!")

sales = {"Bubblegum": 202, "Toffee": 118, "Ice cream": 2250, "Milk chocolate": 1680, "Doughnut": 1075, "Pancake": 80}

print(f"Product:")
print("Bubblegum: $" + str(sales["Bubblegum"]))
print("Toffee: $" + str(sales["Toffee"]))
print("Ice cream: $" + str(sales["Ice cream"]))
print("Milk chocolate: $" + str(sales["Milk chocolate"]))
print("Doughnut: $" + str(sales["Doughnut"]))
print("Pancake: $" + str(sales["Pancake"]))

income = 7777.0
earn_amount = 0

for price in sales.values():
    earn_amount += price

print(f"Earned amount: ${earn_amount}")
print(f"Income: ${income}")

expense = float(input("Staff expenses:"))
other_expense = float(input("Other expenses:"))

net_income = earn_amount - expense - other_expense

print(f"Net income: ${net_income}")