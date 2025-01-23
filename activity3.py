#Write a Python program to create a calculator. Create individual functions for different operators - addition, subtraction, division, multiplication and return the output value.

num1=int(input("Enter number"))
num2=int(input("Enter another number"))

def sum(a,b):
     return a+b

def diff(a,b):
     return b-a

def div(a,b):
     return b/a

def mul(a,b):
     return a*b

print("The sum of {} and {} is {}".format(num1,num2,sum(num1,num2)))
print("The difference between {} and {} is {}".format(num1,num2,diff(num1,num2)))
print("The product of {} and {} is {}".format(num1,num2,mul(num1,num2)))
print("The Quotient of {} and {} is {}".format(num1,num2,div(num1,num2)))

