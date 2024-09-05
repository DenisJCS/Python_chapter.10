print("Give me two numbers, and I'll divide them.")
print("Enter 'q' to quit.")

num1 = input("Enter first number")
num2 = input("Enter second number")

try:
    result = int(num1) + int(num2)
    print(f"Result is {result}")
except ValueError:
    print("Please enter number.")
    