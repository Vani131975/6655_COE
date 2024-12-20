def calculate_bill(units):
    bill = 0

    if units <= 100:
        bill = units * 3
    elif 101 <= units <= 200:
        bill = 100 * 3 + (units - 100) * 5
    elif 201 <= units <= 300:
        bill = 100 * 3 + 100 * 5 + (units - 200) * 7
    else:
        bill = 100 * 3 + 100 * 5 + 100 * 7 + (units - 300) * 10

    return bill

units_consumed = int(input("Enter the number of units consumed: "))
bill_amount = calculate_bill(units_consumed)
print(f"The electricity bill for {units_consumed} units is: ₹{bill_amount}")
