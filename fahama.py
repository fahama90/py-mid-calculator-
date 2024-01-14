def calculator():
    print("Simple Calculator")
    print("Operations:")
    print("1. Add")
    print("2. Subtract")
    print("3. Multiply")
    print("4. Divide")

    try:
        choice = int(input("Enter operation number (1/2/3/4): "))
        num1 = float(input("Enter first number: "))
        num2 = float(input("Enter second number: "))

        if choice == 1:
            result = num1 + num2
        elif choice == 2:
            result = num1 - num2
        elif choice == 3:
            result = num1 * num2
        elif choice == 4:
            if num2 != 0:
                result = num1 / num2
            else:
                print("Error: Division by zero")
                return
        else:
            print("Invalid input. Please enter a valid operation number.")
            return

        print(f"Result: {result}")

    except ValueError:
        print("Invalid input. Please enter valid numbers.")

if _name_ == "_main_":
    calculator()
