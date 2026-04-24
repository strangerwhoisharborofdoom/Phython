num=float(input("Enter the number :"))
def factorial_recursive(num):
    if num == 0 or num == 1:
        return 1
    return num * factorial_recursive(num - 1)

print(factorial_recursive(num))
