def main():
    try:
        num1 = int(input("Enter the first number: "))
        num2 = int(input("Enter the second number: "))
        operation = input("Enter the operation (+, -, *, /): ")

        if operation not in ["+", "-", "*", "/"]:
            raise ValueError("Invalid operation!")

        # Compute result safely
        if operation == "+":
            result = num1 + num2
        elif operation == "-":
            result = num1 - num2
        elif operation == "*":
            result = num1 * num2
        elif operation == "/":
            if num2 == 0:
                raise ZeroDivisionError("Cannot divide by zero!")
            result = num1 / num2

        # Only write if everything succeeded
        with open("./ds-course/equations.txt", "a+") as file:
            file.write(f"{num1} {operation} {num2} = {result}\n")

        print("Equation saved successfully.")

    except ValueError:
        print("Invalid input! Please enter valid numbers and operation.")
    except ZeroDivisionError as e:
        print(e)


if __name__ == "__main__":
    main()