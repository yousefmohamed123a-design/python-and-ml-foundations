# Python compound interest calculator
# A = p ( 1 + (r / n) )^ t
# p : initial balance    r : interest rate  t : time

p = float(input("Enter your initial balance : "))
while p < 0:
    print("The value can not be negative or a zero")
    p = float(input("Enter your initial balance : "))


r = float(input("Enter the interest rate : "))
while r < 0:
    print("The value can not be negative or a zero")
    r = float(input("Enter the interest rate : "))

t = int(input("Enter the time period in years : "))
while t < 0:
    print("The value can not be negative or a zero")
    t = int(input("Enter the time period in years : "))


A = p * ((1 + (r / 100)) ** t)
print(f"Your balance after {t} years ${A:.3f}")
