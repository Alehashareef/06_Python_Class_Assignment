class NegativeNumberError(Exception):
    pass

def calculate_square_root(x):
    if x < 0:
        raise NegativeNumberError("Cannot calculate square root of a negative number.")
    return x ** 0.5

try:
    num = float(input("Enter a number: "))
    result = calculate_square_root(num)
    print("Square root is:", result)

except NegativeNumberError as ne:
    print("Custom Error:", ne)
except ValueError:
    print("Invalid input! Please enter a numeric value.")
except Exception as e:
    print("Something went wrong:", e)
finally:
    print("Program Finished.")
