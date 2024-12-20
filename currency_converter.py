print("Currency Converter")

def convert_currency(usd):
    inr_rate = 82.5  
    eur_rate = 0.92  
    gbp_rate = 0.77  
    inr = usd * inr_rate
    eur = usd * eur_rate
    gbp = usd * gbp_rate

    return inr, eur, gbp

usd_amount = float(input("Enter the amount in USD: $"))
inr, eur, gbp = convert_currency(usd_amount)

print(f"\n{usd_amount} USD is equal to:")
print(f"{inr:.2f} INR")
print(f"{eur:.2f} EUR")
print(f"{gbp:.2f} GBP")
