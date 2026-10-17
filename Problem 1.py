def simpleDiv(dividend, divisor):
    count = 0

    while dividend >= divisor:
        dividend -= divisor
        count += 1

    return count


def main():
    dividend = int(input("Enter the dividend: "))
    divisor = int(input("Enter the divisor: "))

    if divisor <= 0:
        print("The divisor must be a positive integer.")
    else:
        result = simpleDiv(dividend, divisor)
        print("The result is:", result)


main()