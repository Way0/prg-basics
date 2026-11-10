decimal = int(input("Enter decimal number: "))
number = decimal
remainders = []

if number == 0:
    remainders.append("0")

while number > 0:
    remainders.append(str(number % 2))
    number //= 2

binary = "".join(reversed(remainders))
print(f"{decimal}(10) = {binary}(2)")
