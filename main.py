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

def subtract():
    first = int(input("Enter first number: "))
    second = int(input("Second #: "))
    print(f"{second-first}")

if __name__ == "__main__":
    multiply_two_numbers_from_input()
    divide_two_numbers_from_input()
    add_two_numbers_from_input()