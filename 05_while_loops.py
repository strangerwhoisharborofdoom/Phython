# Program 5: Factorial Calculation using While Loop

n = int(input("Enter a non-negative integer to find its factorial: "))

if n < 0:
    print("Factorial is not defined for negative numbers.")
else:
    factorial = 1
    i = 1
    while i <= n:
        factorial *= i
        i += 1
    print(f"Factorial of {n} = {factorial}")
