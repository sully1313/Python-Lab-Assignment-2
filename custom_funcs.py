def greater_two(num):
    print("\n\tThe length of your entry is " + str(num))
    modulus = num % 3
    multiplied = num * 10
    divide = num / 2

    print(str(format('\n\t' + str(num) + ' MOD 3 = ' + str(modulus), '2')))
    print(str(format('\n\t' + str(num) + ' X 10 = ' + str(multiplied), '2')))
    print(str(format('\n\t' + str(num) + ' DIVIDED by 10 = ' + str(divide), '2')))


def less_equal_two(num):
    print("\n\tThe length of your entry is " + str(num))
    addition = num + 56
    subtraction = num - 45
    power = num**2

    print(str(format('\n\t' + str(num) + ' + 56 = ' + str(addition), '2')))
    print(str(format('\n\t' + str(num) + ' - 45 = ' + str(subtraction), '2')))
    print(str(format('\n\t' + str(num) + ' SQUARED = ' + str(power), '2')))
