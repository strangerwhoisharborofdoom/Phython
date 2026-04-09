# Program 4: Multiplication Tables and Sequence Sums using For Loops

# --- Multiplication Table ---
print("=== Multiplication Table ===")
n = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication table of {n}:")
for i in range(1, 11):
    print(f"  {n} x {i:2} = {n * i}")

# --- Sum of first N natural numbers ---
print("\n=== Sum of First N Natural Numbers ===")
n = int(input("Enter a positive integer N: "))
total = 0
for i in range(1, n + 1):
    total += i
print(f"Sum of first {n} natural numbers = {total}")

# --- Sum of squares of first N natural numbers ---
print("\n=== Sum of Squares of First N Natural Numbers ===")
n = int(input("Enter a positive integer N: "))
sum_of_squares = 0
for i in range(1, n + 1):
    sum_of_squares += i * i
print(f"Sum of squares of first {n} natural numbers = {sum_of_squares}")
