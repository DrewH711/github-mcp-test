def multiply_two_numbers_from_input():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    product = first * second
    print(f"Product: {product}")


def divide_two_numbers_from_input():
    while True:
        try:
            numerator = float(input("Enter the numerator: "))
            denominator = float(input("Enter the denominator: "))
            if denominator == 0:
                print("Error: Cannot divide by zero. Please try again.\n")
                continue
            quotient = numerator / denominator
            print(f"Quotient: {quotient}")
            break
        except ValueError:
            print("Error: Invalid input. Please enter numeric values.\n")


def add_two_numbers_from_input():
    first = float(input("Enter the first number: "))
    second = float(input("Enter the second number: "))
    total = first + second
    print(f"Sum: {total}")


def exponentiate_two_numbers_from_input():
    base = float(input("Enter the base: "))
    exponent = float(input("Enter the exponent: "))
    result = base ** exponent
    print(f"Result: {result}")


if __name__ == "__main__":
    multiply_two_numbers_from_input()
    divide_two_numbers_from_input()
    add_two_numbers_from_input()
    exponentiate_two_numbers_from_input()