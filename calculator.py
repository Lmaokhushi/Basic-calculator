num1 = float(input("Enter a number:"))
oper = input("Enter an operator:")
num2 = float(input("Enter another number:"))

if oper =="+":
    print(num1 + num2)
elif oper =="-":
    print(num1 - num2)
elif oper =="*":
    print(num1 * num2)
elif oper =="/":
    print(num1 / num2)
else:
    print("Invalid operator")