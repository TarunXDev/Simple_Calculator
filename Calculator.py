def calculator():
    print("Simple Calculator")
    print("Select an operation:")
    print("1. Addition")
    print("2. Subtraction")
    print("3. Multiplication")
    print("4. Division")

    try:
        choice = int(input("Enter your choice (1-4): "))

        if choice not in [1, 2, 3, 4]:
            print("Invalid choice. Please select a valid operation.")
            return

        numbers = input("Enter numbers separated by space: ").split()
        numbers = [float(num) for num in numbers]

        if not numbers:
            print("No numbers entered.")
            return

        if choice == 1:
            result = sum(numbers)
            operation = "Addition"
        elif choice == 2:
            result = numbers[0]
            for num in numbers[1:]:
                result -= num
            operation = "Subtraction"
        elif choice == 3:
            result = 1
            for num in numbers:
                result *= num
            operation = "Multiplication"
        elif choice == 4:
            result = numbers[0]
            try:
                for num in numbers[1:]:
                    if num == 0:
                        print("Error: Division by zero is not allowed.")
                        return
                    result /= num
            except ZeroDivisionError:
                print("Error: Division by zero is not allowed.")
                return
            operation = "Division"

        print(f"Result of {operation}: {result}")

    except ValueError:
        print("Invalid input. Please enter numeric values.")

if __name__ == "__main__":
    calculator()
