

import string

password = input("Enter your password: ")

length = len(password) >= 8
upper = any(char.isupper() for char in password)
lower = any(char.islower() for char in password)
digit = any(char.isdigit() for char in password)
symbol = any(char in string.punctuation for char in password)

score = sum([length, upper, lower, digit, symbol])

print("\nPassword Analysis")
print("------------------")

if length:
    print("✔ Good Length")
else:
    print("✘ Password too short")

if upper:
    print("✔ Contains Uppercase")
else:
    print("✘ No Uppercase")

if lower:
    print("✔ Contains Lowercase")
else:
    print("✘ No Lowercase")

if digit:
    print("✔ Contains Digit")
else:
    print("✘ No Digit")

if symbol:
    print("✔ Contains Symbol")
else:
    print("✘ No Symbol")

print("\nFinal Result")

if score <= 2:
    print("Weak Password")
elif score <= 4:
    print("Medium Password")
else:
    print("Strong Password")
