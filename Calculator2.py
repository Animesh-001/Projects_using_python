#operator input selected by computer
import random
def Calc(num1,num2,op):
    if op=="+":
        return num1+num2
    elif op=="-":
        return num1-num2
    elif op=="*":
        return num1*num2
    elif op=="//":
        return num1//num2
    elif op=="%":
        return num1%num2
    elif op=="**":
        return num1**num2

n=random.randint(1,6)
if n==1:
    op="+"
elif n==2:
    op="-"
elif n==3:
    op="*"
elif n==4:
    op="/"
elif n==5:
    op="%"
elif n==6:
    op="**"

print("Computer Selected operator is:",op)
a=int(input("Enter first number:"))
b=int(input("Enter second number:"))
c=Calc(a,b,op)
print(c)
