total_cost = 0
num_of_items = int(input("Number of Items: "))

while num_of_items < 0:
    print("Invalid number of Items")
    num_of_items = int(input("Number of Items: "))
for i in range(num_of_items):
    item_price = float(input("Price of Item: "))
    total_cost += item_price
if total_cost > 100:
    total_cost = total_cost * 0.1
print("Total price for", num_of_items, "items is $", total_cost)
