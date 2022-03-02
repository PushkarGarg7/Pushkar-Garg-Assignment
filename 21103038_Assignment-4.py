# Question1

print('Question-1')
def Hanoi(n, source, destination, auxillary):
    if n==1:
        print("Move disc 1 from", source, "to", destination)
    else:
        Hanoi(n-1, source, auxillary, destination) 
        print("Move disc", n, "from", source, "to", destination) 
        Hanoi(n-1, auxillary, destination, source) 

n=int(input("Enter the number of discs: "))
Hanoi(n, 'A', 'B', 'C') 
#Considering A as source peg and B as destination peg and C as the auxilliary peg



# Question2

print('Question-2')
rows=int(input("Enter the number of rows: "))
def factorial(n): # Calculating factorial
    if(n==0 or n==1):
        return 1
    else:
        return n*factorial(n-1)

for i in range(0, rows): # Calculating nCr
    for j in range(0, rows-i):
        print(" ", end="")
    for j in range (0, i+1):
        print(int(factorial(i)/(factorial(j)*factorial(i-j))), end=" ") # Now will put formula of nCr in the pascal's triangle
    print()

def pascal(n, p):
    if(n<0):
        return
    else:
        pascal(n-1, p) # recursion gives previous lines of Pascal's triangle
        for i in range(0, p-n):
            print(" ", end="")
        for i in range(0, n):
            print(int(factorial(n-1)/(factorial(i)*factorial(n-1-i))), end=" ") # Now will give current line of Pascal's Triangle
        print()
pascal(rows, rows)


# Question-3

print('Question-3')
number1=int(input("Enter first number: "))
number2=int(input("Enter second number: "))
quotient=number1//number2
remainder=number1%number2
print("The quotient is", quotient, "and the remainder is", remainder)

# PART-(a)
print(callable(quotient))
print(callable(remainder))

# PART-(b)
print(quotient!=0)
print(remainder!=0)

# PART-(c)
list_=[quotient, remainder]+[4, 5, 6] # adding elements in list
print(list_)
list_=(list(filter(lambda i: i<=4, list_)))
print(list_)

# PART-(d)
set_=set(list_) 
print(set_)

# PART-(e)
set_=frozenset(set_)
print(set_)

# PART-(f)
maximum_num=max(set_) # finding max value
print(maximum_num)
print(hash(maximum_num)) # finding hash value



# Question3
 
print('Question-4')

class Student: # class named student
    def __init__(self, name, roll_no):
        self.name=name # assigning name
        self.roll_no=roll_no # assigning roll number

stud_1=Student("Pushkar",21103038) # object s1 is created
print("Student's name is", stud_1.name)
print("Student's SID is", stud_1.roll_no)
del stud_1 # object s1 is deleted



# Question5

print('Question-5')

class Employee:
    def __init__(self, name, salary):
        self.name=name
        self.salary=salary

Empl_1=Employee("Mehak", 40000)
Empl_2=Employee("Ashok", 50000)
Empl_3=Employee("Viren", 60000)

# PART-a
Empl_1.salary=70000 # updating salary of Mehak
print(Empl_1.salary)

# PART-b
del Empl_3 # deleting the record of Viren


# Question-6
print('Question-6')
G_word=input("Enter George's word: ")
B_word=input("Enter Barbie's word: ")

def anagrams(i): # function to find anagrams
    if i=="":
        return [i]
    else:
        ans=[] # list of anagrams
        for w in anagrams(i[1:]):
            for pos in range(len(w)+1): # putting first letter in different positions in the anagrams of the remaining letters
                ans.append(w[:pos]+i[0]+w[pos:])
        return ans

correct_word=anagrams(G_word)
if B_word in correct_word: # checking if Barbie's word is an anagram of George's word
    print("Friendship is True.")
else:
    print("Friendship is Fake.")
