cart_items = {'Laptop': 50000, 'charger': 10000, 'pendrive': 30000}

def totalPrice():
    if len(cart_items) == 0:
        print("The cart is empty!!")
        return 0 

    total = 0
    for  price in cart_items.values():
        if 20000 <= price <= 50000:
            price *= 0.9 
        else:
            price *= 0.85
        total += price 

    return total

print("The total price is:", totalPrice())
