def calculate(num1, num2, operator):
    if operator == "+":
        return num1 + num2
    elif operator == "-":
        return num1 - num2
    elif operator == "*":
        return num1 * num2
    elif operator == "/":
        if num2 == 0:
            return "Error: Can't divide by zero!"
        return num1 / num2
    else:
        return "Error: Unknown operator."


def main():
    print("=== Simple Calculator ===")
    print("Operators available: +  -  *  /")
    print("Type 'q' at any time to quit.\n")

    while True:
        first = input("Enter first number: ")
        if first.lower() == "q":
            break

        operator = input("Enter operator (+, -, *, /): ")
        if operator.lower() == "q":
            break

        second = input("Enter second number: ")
        if second.lower() == "q":
            break

        try:
            first = float(first)
            second = float(second)
        except ValueError:
            print("Please enter valid numbers.\n")
            continue

        result = calculate(first, second, operator)
        print(f"Result: {result}\n")

    print("Thanks for using the calculator. Goodbye!")


if __name__ == "__main__":
    main()
