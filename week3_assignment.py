print("=== Food Truck Order System ===")
print("Enter food type: appetizer ($5.00), entree ($11.00), or dessert ($6.50)")
print("Type 'done' when finished ordering\n")

prices = {
    "appetizer": 5.00,
    "entree": 11.00,
    "dessert": 6.50
}

total = 0.0

while True:
    food = input("Enter food type: ").lower()

    if food == "done":
        break
    elif food in prices:
        price = prices[food]
        total += price
        print(f"Price: ${price:.2f}")
        print(f"Current total: ${total:.2f}\n")
    else:
        print("Sorry, that’s not on the menu. Try again.\n")

print("\n=== Order Summary ===")
print(f"Subtotal: ${total:.2f}")

discount = 0.0
if total >= 35.00:
    discount = 4.50
    print(f"Combo Deal Discount: -${discount:.2f}")

final_total = total - discount
print(f"Final Total: ${final_total:.2f}")
print("Thank you for your order!")
print("done")