num1=float(input("Enter number 1 :"))
num2=float(input("Enter number 2 :"))
if(num1>num2):
    print(f"num1 is greater than num2")
elif(num2>num1):
    print(f"num2 is greater than num1")
else:
    print(f"num1 == num2")

print(f"Enter the marks(0f 100)")
marks = float(input("Enter the marks  :"))
if(marks>100):
    print(f"error//")
elif(marks>79):
    print(f"A Grade")
elif(marks>39):
    print(f"B Grade")
else:
    print(f"C Grade")
    
    
