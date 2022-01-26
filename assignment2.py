#Question1
string1="Python is a case sensitive language" #string1
print("The length of string is",len(string1)) #(part a)
print("The reversed string is ",string1[::-1])# (part b)
string2=string1[10:26]#(part c)
string3=string1.replace("a case sensitive","object oriented")
print(string3)#(part d)
print("The index of substring a is ",string1.find('a'))#(part e)
print("The origial string after removing white spaces is",string1.replace(" ",""))#(part f)
print("\n")


#Question2
NAME=input("Enter your name")
SID=int(input("Enter your SID"))
DEPARTMENT=input("Enter your department")
CGPA=float(input("Enter your CGPA"))
print("Hey %s,"%NAME,"Here!")
print("My SID is %d" %SID)
print("I am from %s"%DEPARTMENT,"and my CGPA is %f"%CGPA)
print("\n")

#Question3
a=56
b=10
print("a. ",a&b)
print("b. ",a|b)
print("c. ",a^b)
print("Left shift both a and b with 2 bits respectively :",a<<2 ,b<<2)
print("Right shift a with 2 bits and b with 4 bits respectively : ",a>>2,b>>4)
print("\n")


#Question4
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))
number3 = float(input("Enter third number: "))
 
if (number1 >=number2) and (number1 >=number3):
   largest = number1
elif (number2 >=number1) and (number2 >=number3):
   largest = number2
else:
   largest = number3
 
print("THE LARGEST NUMBER IS ",largest)
print("\n")



#Question5
_String=input("Enter a string")
if 'name' in _String:
    print ("Yes")
else:
    print ("No")
print("\n")


#Question6
a=float(input("Enter first side of the triangle"))
b=float(input("Enter second side of the triangle"))
c=float(input("Enter third side of the triangle"))
if(a>=(b+c)):      #Equality sign is used because if sum of two sides is equal to third then it is a straight line not a triangle
    print("No")
elif(b>=(a+c)):
    print("No")
elif(c>=(a+b)):
    print("No")
else:
    print("Yes")    
