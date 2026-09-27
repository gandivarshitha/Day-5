'''

---Operators---

-->Operator is used to perform a specific task in between two oprands
eg:a+b

+--> specific task that is addition
a,b--> are the oprands/variables

---------Types of Operators----------
1.Arithematic operators
2.Assignment Operators
3.Logical Operators
4.Comparsion Operators
5.Membership Operators
6.Identity Operators

'''

#Arithematic Operators: 

first_number=int(input("Enter the first number"))
second_number=int(input("enter the second number"))

#addition of first number and second number is 30

print(f"Addition of {first_number} and {second_number} is {first_number+second_number}")
print(f"Subtraction of {first_number} and {second_number} is {first_number-second_number}")
print(f"Multiplication of {first_number} and {second_number} is {first_number*second_number}")
print(f"Division of {first_number} and {second_number} is {first_number/second_number}")
#20/5
print(f"Floor division of {first_number} and {second_number} is {first_number//second_number}")
print(f"Modulus of {first_number} and {second_number} is {first_number%second_number}")
print(f"power of {first_number} and {second_number} is {first_number**second_number}")

#area of circle


radius=float(input("enter the radius of the circle"))
area=3.14*radius*radius
print(f"area of the circle is: {area}")




# simple interest

p=int(input("enter the amount"))
t=float(input("enter the time period"))
r=float(input("enter the rate of interest"))

simple_interest=p*t*r/100
print(f"simple interest is :{simple_interest}")