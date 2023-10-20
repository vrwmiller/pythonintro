#! env python

name = input("Your name? ")
color = input("Color? ")
age = int(input("Age? "))

# NAME is AGE years old and loves the color COLOR.
#print(name, end=" ")
#print("is" + str(age) + "years old and loves the color" + color + ".", sep=" ")

print(name, 'is', age, 'years old and loves the color', color + '.')