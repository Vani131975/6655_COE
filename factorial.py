print("Factorial")
def fact(n):
    if n==1 or n==0:
        return 1
    return n*fact(n-1)

n=int(input("Enter any number: "))
print(f"The factorial of {n} is: ",fact(n))