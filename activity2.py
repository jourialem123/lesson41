#Write a Python program that finds the factorial of a number using recursion and returns the result. (Example - If number = 5, factorial = 5*4*3*2*1 = 120

def factorial(num):
    if num==1:
        return num
    else:
      return num*factorial(num-1)
num=int(input("Enter a number"))
if num<0:
   print("Can not find factorial for negative numbers")
elif num==0:
 print("The factorial of 0 is 1")
else:
   print("The factorial of {} is {}".format(num,factorial(num)))
   
