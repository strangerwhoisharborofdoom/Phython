# Program 4: Multiplication Tables and Sequence Sums using For Loops

# --- Multiplication Table ---
print("=== Multiplication Table ===")
table_num = int(input("Enter a number to print its multiplication table: "))
print(f"\nMultiplication table of {table_num}:")
for i in range(1, 11):
    print(f"  {table_num} x {i:2} = {table_num * i}")

# --- Sum of first N natural numbers ---
print("\n=== Sum of First N Natural Numbers ===")
count = int(input("Enter a positive integer N: "))
total = 0
for i in range(1, count + 1):
    total += i
print(f"Sum of first {count} natural numbers = {total}")

# --- Sum of squares of first N natural numbers ---
print("\n=== Sum of Squares of First N Natural Numbers ===")
squares_count = int(input("Enter a positive integer N: "))
sum_of_squares = 0
for i in range(1, squares_count + 1):
    sum_of_squares += i * i
print(f"Sum of squares of first {squares_count} natural numbers = {sum_of_squares}")
