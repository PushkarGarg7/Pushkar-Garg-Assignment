#Question 1

string_1=input("Enter a string-")
string_2=string_1.upper()
list_1=[]
list_2=string_2.split()
y=len(list_2)
d=dict()
t=dict()
if len(list_2)==1:          
    for i in string_2:      
        list_1.append(i) 
    for j in list_1:        
        if j in d:         
            d[j]=d[j]+1 
        else:
            d[j]=1
    print(d)        

else:
    for i in list2:        #for multiple words
        if i in t:
            t[i]=t[i]+1
        else:
            t[i]=1
    print(t) 
    

#Question 2

month=int(input("Enter month-"))


if(month in[1,3,5,7,8,10,12]):
    day=int(input("Give day:"))
    if(1<=day<=31):
        year=int(input("Give year:"))
        if(1800<=year<=2025):
            print("Date:",day,"/",month,"/",year)
            if(month==12 and day==31):
                print("Next Date:","1/1/",year+1)
            elif(day==31):
                print("Next Date:","1/",month+1,"/",year)
            else:
                print("Next Date:",day+1,"/",month,"/",year)
        else:
            print("year not valid")
    else:
         print("date not valid")
elif(month in[4,6,9,11]):
    day=int(input("Enter day:"))
    if(1<=day<=30):
        year=int(input("Enter year:"))
        if(1800<=year<=2025):
            print("Date:",day,"/",month,"/",year)
            if(day==30):
                print("Next Date:","1/",month+1,"/",year)
            else:
                print("Next Date:",day+1,"/",month,"/",year)
        else:
            print("year not valid")
    else:
         print("date not valid")
elif(month==2):
    year=int(input("Give year:"))
    if(1800<=year<=2025):
        day=int(input("Give day:"))
        if(year%4==0):
            if(1<=day<=29):
                print("Date:",day,"/",month,"/",year)
                if(day==29):
                    print("Next Date:","1/",month+1,"/",year)
                else:
                    print("Next Date:",day+1,"/",month,"/",year)              
            else:
                print("day not valid")
        else:
            if(1<=day<=28):
                print("Date:",day,"/",month,"/",year)
                if(day==28):
                    print("Next Date:","1/",month+1,"/",year)
                else:
                    print("Next Date:",day+1,"/",month,"/",year)       
            else:
                print("day not valid")     
    else:
        print("year not valid")
else:
    print("month not valid")
    
#Question 3

given_list=[1,2,3,4,5,6,7,8,9,10]
modified_list_with_tupples=[]
for i in given_list:
    modified_list_with_tupples.append((i,i**2))
print(modified_list_with_tupples)

#Question 4

Grade_points=int(input("Enter a number from 4 to 10:"))
if(Grade_points==4):
    print("Performance=Poor")
    print("Letter Grade=D")
elif(Grade_points==5):
    print("Performance=Below Average")
    print("Letter Grade=C")
elif(Grade_points==6):
    print("Performance=Average")
    print("Letter Grade=C+")
elif(Grade_points==7):
    print("Performance=Good")
    print("Letter Grade=B")
elif(Grade_points==8):
    print("Performance=Very Good")
    print("Letter Grade=B+")
elif(Grade_points==9):
    print("Performance=Excellent")
    print("Letter Grade=A")
elif(Grade_points==10):
    print("Performance==Outstanding")
    print("Letter Grade=A+")
else:
    print("invalid input")

#Question 5

Given_Word="ABCDEFGHIJK"

variable=1


while(variable<7):
    print(" "*(variable-1),Given_Word[0:11-((variable-1)*2)])
    variable=variable+1


#Question 6

student_info=dict()
n="y"
alistsid=[]
listsid=[]
#(a)
print("(a):")
while(n=="y"):
    sid=int(input("enter sid:"))
    if sid in listsid:
        print("Error!run the code with a different sid!")
        break
    listsid.append(sid)
    name=input("Enter your name:")
    student_info[sid]=name
    n=input("give a letter Y or N:")
    alistsid.append((sid,name))
print("The required dictionary:",student_info)
print("The list will be used in further parts:")
print("The required list:",alistsid)

#(b)
print("(b):")
print("The dictionary we had before:")
print(student_info)
newdict=dict()
alistname=[]
for (m,n) in student_info.items():
    newdict[n]=m
    alistname.append((n,m))
print("exchanged the key value pair but its not sorted:")
print(newdict)
print("unsorted list:")
print(alistname)
alistname.sort()
print("sorted list:")
print(alistname)
print("sorted dictionary:")
sorted_dict=dict(alistname)
print(sorted_dict)
required_dict_name=dict()
for (m,n) in sorted_dict.items():
    required_dict_name[n]=m
print("This is the dictionary sorted on the basis of name-")
print(required_dict_name)

#(c) 
print("(c):")
print("The earlier list will be used now:")
print(alistsid)
alistsid.sort()
print("now the list is sorted-")
print(alistsid)
sorted_student_info_sid=dict(alistsid)
print("sorted dictionary based on sid:",sorted_student_info_sid)

#(d)    
print("(d):")    
entered_sid=int(input("enter one of the previous sid's entered:"))
print("The name of the student with the entered sid is:")    
print(student_info[entered_sid])

#Question7
first_number=int(input("enter a number:"))
second_number=int(input("enter another a number:"))
sum=first_number+second_number
series=[first_number,second_number]
n="y"
while(n=="y"):
    series.append(series[len(series)-1]+series[len(series)-2])
    print(series)
    n=input("Give y to contnue and n to stop:")
print("we have a list having a fibonacci series:")
print(series)

sum=0
for i in series:
    sum=sum+i
print("Average of the sequence:")
print(sum/len(series))

#Question 8
Set1={1,2,3,4,5}
Set2={2,4,6,8}
Set3={1,5,9,13,17}

#(a)
print("(a):")
new_set1=Set1^Set2
print(new_set1)

#(b)
print("(b):")
new_set2=Set1^(Set2^Set3)
print(new_set2)

#(c)
print("(c):")
new_set3=(Set1&Set2)|(Set2&Set3)|(Set1&Set3)
print(new_set3)

#(d)
print("(d)")
Set={1,2,3,4,5,6,7,8,9,10}
new_set4=Set-Set1
print(new_set4)

#(e)
print("-------------(e)------------")
new_set5=Set-(Set1|Set2|Set3)
print(new_set5)
print("Done!")
