count = int(input("Number of products purchased: "))
price = float(input("Product price: "))

if count > 2:
    total = (2 * price) + ((count - 2) * price * 0.75)
else:
    total = count * price

print(f"Amount to pay: {total:.2f}")
