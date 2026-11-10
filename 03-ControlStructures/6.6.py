hours = int(input("Enter number of hours: "))

if 1 <= hours <= 2:
    fee = 5
elif 3 <= hours <= 6:
    fee = 15
elif hours > 6:
    fee = 20
else:
    fee = 0

print(f"Fee: {fee} PLN")
