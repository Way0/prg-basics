###
# Sums numbers entered by user
#
total_sum = 0
count = 0

while True:
    number = int(input("Enter a number (0 to stop): "))
    
    if number == 0:
        break  # Exit the loop when 0 is entered
    total_sum += number
    count += 1

print(f"The total sum of the numbers is: {total_sum}")
if count > 0:
    print(f"Arithmetic mean: {total_sum / count}")
