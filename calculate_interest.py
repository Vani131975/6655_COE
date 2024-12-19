k0 = float(input("Enter initial balance k0: "))
interest = float(input("Enter interest rate in percentage: "))
interest /= 100
k1 = k0 * (1 + interest)
print(f"The capital after one year is: {k1:.2f}")

n = int(input("Enter number of years: "))
k = k0
year = 1

while year <= n:
  k = k * (1 + interest)
  print(f"The capital after {year} year is: {k:.2f}")
  year += 1
