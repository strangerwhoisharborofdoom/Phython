# Program 3: Number Comparison, Grading System, and Decision Making

# --- Number Comparison ---
print("=== Number Comparison ===")
x = float(input("Enter first number: "))
y = float(input("Enter second number: "))

if x > y:
    print(f"{x} is greater than {y}")
elif x < y:
    print(f"{x} is less than {y}")
else:
    print(f"{x} and {y} are equal")

# --- Grading System ---
print("\n=== Grading System ===")
marks = float(input("Enter your marks (0 - 100): "))

if marks < 0 or marks > 100:
    print("Invalid marks entered.")
elif marks >= 90:
    grade = "A+"
    result = "Pass"
elif marks >= 80:
    grade = "A"
    result = "Pass"
elif marks >= 70:
    grade = "B"
    result = "Pass"
elif marks >= 60:
    grade = "C"
    result = "Pass"
elif marks >= 50:
    grade = "D"
    result = "Pass"
else:
    grade = "F"
    result = "Fail"

if 0 <= marks <= 100:
    print(f"Marks : {marks}")
    print(f"Grade : {grade}")
    print(f"Result: {result}")

# --- Decision Making: Largest of three numbers ---
print("\n=== Find the Largest of Three Numbers ===")
p = float(input("Enter first number: "))
q = float(input("Enter second number: "))
r = float(input("Enter third number: "))

if p >= q and p >= r:
    print(f"The largest number is {p}")
elif q >= p and q >= r:
    print(f"The largest number is {q}")
else:
    print(f"The largest number is {r}")
