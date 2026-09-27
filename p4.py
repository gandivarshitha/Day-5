'''
----------Logical Operators-------------

Types:
1.Logical AND
2.Logical OR
3.Logical NOT


---------AND Operators--------------

  C1 C2  RESULT
  T  T     T
  T  F     F
  F  T     F
  F  F     F

----------OR Operators----------------

   C1 C2  RESULT
   T  T    T
   T  F    T
   F  T    T
   F  F    F

   
------------NOT Operator-----------
opposite to the original output

'''

a=int(input("enter the first number"))
b=int(input("enter the second number"))
c=int(input("enter the third number"))

'''

a=10
b=20
c=30

'''

print(a>b and a<c)
print(a<b and a>c)
print(a<b and a>c)

print(a>b or a<c)
print(a<b or a>c)

print(a>b)