def main():
    height = float(input("Enter the initial height in meters: "))
    bounces = 0

    while height >= 0.001:
        height = height * 0.60
        bounces += 1

    print("The ball bounced", bounces, "times.")


if __name__ == "__main__":
    main()