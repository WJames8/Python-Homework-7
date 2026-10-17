def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a


def phi(n):
    relatively_prime = []

    for k in range(1, n):
        if gcd(n, k) == 1:
            relatively_prime.append(k)

    return relatively_prime


def main():
    n = int(input("Enter a positive integer n: "))

    if n < 1:
        print("Please enter a positive integer.")
        return

    result = phi(n)

    print("Numbers relatively prime to", n, ":", result)
    print("Euler's totient value:", len(result))


if __name__ == "__main__":
    main()