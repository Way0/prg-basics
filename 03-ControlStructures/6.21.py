amount = int(input("Enter the amount in PLN: "))
print(f"The amount of PLN {amount} in coins:")

c5 = amount // 5
amount %= 5

c2 = amount // 2
amount %= 2

c1 = amount // 1

print(f"5 PLN coins: {c5}")
print(f"2 PLN coins: {c2}")
print(f"1 PLN coins: {c1}")
