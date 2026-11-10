def sum_digits(number):
    str_number = str(abs(number))
    total = 0
    for digit in str_number:
        total += int(digit)
    return total

any_number = int(input('Enter integer number: '))
result = sum_digits(any_number)
print('The sum of the digits in the number {} is {}'.format(any_number, result))