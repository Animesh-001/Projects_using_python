operator=input("Enter any operator among (+,-,*,/,%):")
num1=int(input("enter a value:"))
num2=int(input("enter another value:"))
if '+' in operator:
    print("addition of two number is",num1+num2)
elif '-' in operator:
    print("substraction between two numbers",num1-num2)
elif '*' in operator:
    print("multiplication between two numbers",num1*num2)
elif '//' in operator:
    print("quotient between of two numbers",num1//num2)
elif '%' in operator:
    print("reminder between two number",num1%num2)
else:
    print("invalid operator")
