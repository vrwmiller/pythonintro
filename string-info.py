#! env python

m = input("Enter a message: ")

print("First character:", m[0])
print("Middle character:", m[int(len(m) / 2)])
print("Last character:", m[-1])

print("Even index characters:", m[0::2])
print("Odd index characters:", m[1::2])

print("Reverse order:", m[::-1])