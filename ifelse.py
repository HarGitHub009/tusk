print('enter first value')
num1 = int(input())
print('enter second value')
num2 = int(input())
print('enter operators (+,-,*,/)', end="")
val = input()
if val == '+':
 print("\n" + str(num1) + " + " + str(num2) + " = " + str(num1 + num2))
elif val == '-':
 print("\n" + str(num1) + " - " + str(num2) + " = " + str(num1 - num2))
elif val == '/':
 print("\n" + str(num1) + " / " + str(num2) + " = " + str(num1 / num2))
elif val == '*':
 print("\n" + str(num1) + " * " + str(num2) + " = " + str(num1 * num2))
else:
 print("\ninvalid operator")
