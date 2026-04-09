# Program 2: Area, Simple Interest, and Basic Arithmetic Expressions
import math

# --- Area calculations ---
print("=== Area Calculations ===")

length = float(input("Enter length of rectangle: "))
width = float(input("Enter width of rectangle: "))
rectangle_area = length * width
print(f"Area of rectangle = {rectangle_area:.2f}")

radius = float(input("Enter radius of circle: "))
circle_area = math.pi * radius * radius
print(f"Area of circle = {circle_area:.2f}")

base = float(input("Enter base of triangle: "))
height = float(input("Enter height of triangle: "))
triangle_area = 0.5 * base * height
print(f"Area of triangle = {triangle_area:.2f}")

# --- Simple Interest ---
print("\n=== Simple Interest ===")
principal = float(input("Enter principal amount: "))
rate = float(input("Enter annual interest rate (in %): "))
time = float(input("Enter time period (in years): "))
simple_interest = (principal * rate * time) / 100
total_amount = principal + simple_interest
print(f"Simple Interest = {simple_interest:.2f}")
print(f"Total Amount    = {total_amount:.2f}")

# --- Basic Arithmetic Expressions ---
print("\n=== Basic Arithmetic ===")
a = float(input("Enter first number: "))
b = float(input("Enter second number: "))
print(f"Addition       : {a} + {b} = {a + b}")
print(f"Subtraction    : {a} - {b} = {a - b}")
print(f"Multiplication : {a} * {b} = {a * b}")
if b != 0:
    print(f"Division       : {a} / {b} = {a / b:.2f}")
    print(f"Floor Division : {a} // {b} = {a // b}")
    print(f"Modulus        : {a} % {b} = {a % b}")
else:
    print("Division       : Cannot divide by zero")
print(f"Exponentiation : {a} ** {b} = {a ** b}")
