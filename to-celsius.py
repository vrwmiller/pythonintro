#! env python

f = float(input("Enter temp in Fahrenheit: "))
c = ((f - 32) * 5 / 9)

print("Fahrenheit:", f)
print("Celsius:", round(c, 2))