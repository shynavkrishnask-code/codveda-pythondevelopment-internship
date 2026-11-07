"""
Level 1 - Task 1: Simple Calculator
Performs addition, subtraction, multiplication and division.
"""


def add(a, b):
    return a + b


def subtract(a, b):
    return a - b


def multiply(a, b):
    return a * b


def divide(a, b):
    if b == 0:
        return "Error: Division by zero is not allowed."
    return a / b


OPERATIONS = {
    "1": ("Addition", "+", add),
    "2": ("Subtraction", "-", subtract),
    "3": ("Multiplication", "*", multiply),
    "4": ("Division", "/", divide),
}


def get_number(prompt):
    """Keep asking until the user enters a valid number."""
    while True:
        try:
            return float(input(prompt))
        except ValueError:
            print("Invalid input. Please enter a number.")


def show_menu():
    print("\n=== Simple Calculator ===")
    for key, (name, symbol, _) in OPERATIONS.items():
        print(f"{key}. {name} ({symbol})")
    print("5. Quit")


def format_result(value):
    """Show whole numbers without a trailing .0"""
    if isinstance(value, float) and value.is_integer():
        return int(value)
    return value


def main():
    while True:
        show_menu()
        choice = input("Select an operation (1-5): ").strip()

        if choice == "5":
            print("Goodbye!")
            break

        if choice not in OPERATIONS:
            print("Invalid choice. Please select 1-5.")
            continue

        num1 = get_number("Enter first number: ")
        num2 = get_number("Enter second number: ")

        name, symbol, func = OPERATIONS[choice]
        result = func(num1, num2)

        if isinstance(result, str):  # error message from divide()
            print(result)
        else:
            print(f"{format_result(num1)} {symbol} {format_result(num2)} = {format_result(result)}")


if __name__ == "__main__":
    main()
