balance = 1000.0
pin = "1234"

def check_pin():
    user_pin = input("Enter 4-digit PIN: ")
    if user_pin == pin:
        return True
    print("Incorrect PIN!")
    return False

def change_pin():
    global pin
    if check_pin():
        new_pin = input("Enter new 4-digit PIN: ")
        if len(new_pin) == 4 and new_pin.isdigit():
            pin = new_pin
            print("PIN successfully changed.")
        else:
            print("Invalid PIN! Must be 4 digits.")

if check_pin():
    while True:
        print("\n1. Check balance\n2. Deposit\n3. Withdraw\n4. Change PIN\n5. Exit")
        choice = input("Select option: ")
        if choice == '1':
            print(f"Balance: {balance} PLN")
        elif choice == '2':
            amount = float(input("Amount to deposit: "))
            balance += amount
            print(f"Balance: {balance} PLN")
        elif choice == '3':
            amount = float(input("Amount to withdraw: "))
            if amount <= balance:
                balance -= amount
                print(f"Balance: {balance} PLN")
            else:
                print("Insufficient funds!")
        elif choice == '4':
            change_pin()
        elif choice == '5':
            break
