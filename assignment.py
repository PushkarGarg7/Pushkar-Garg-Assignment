# Question1
Num_1 = int(input("Enter the first number ",))
Num_2 = int(input("Enter the second number ",))
Num_3 = int(input("Enter the third number ",))
Sum = Num_1 + Num_2 + Num_3
average = Sum / 3
print("The average of these numbers is ",average)

# Question2
Gross_Income = int(input("Enter your income ",))
Dependent = int(input("Enter number of dependent ",))
Standard_deduction = 10000
Dependent_deduction_amount = Dependent * 3000
print("The value of deducted amount is ",Dependent_deduction_amount)
Taxable_Income = Gross_Income - Standard_deduction - Dependent_deduction_amount
Tax = (20/100) * (Taxable_Income)
print("The value of tax is",Tax)
print("The value of taxable income is ",Taxable_Income)


# Question3
List = []
SID = int(input("Enter your SID ",))
Name = str(input("Enter your name ",))
Gender = str(input("Enter your gender {Use 'M' for 'Male' , 'F' for 'Female' and use 'U' for 'Unknown'}",))
Course_Name = str(input("Enter your course name ",))
CGPA = float(input("Enter your CGPA ",))
List.append(SID)
List.append(Name)
List.append(Gender)
List.append(Course_Name)
List.append(CGPA)
print(List)


# Question4
li = list(map(int, input("Enter the marks of five students: ",).split()))
li.sort()
print(li)


# Question5
List = ['Red', 'Green', 'White', 'Black', 'Pink', 'Yellow']
List.remove('Black')
print(List)
List[3], List[4] = 'Purple', 'Purple'
print(List)
