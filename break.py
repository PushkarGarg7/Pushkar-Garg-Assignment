n=int(input("how many values you want:"))
a=range(1,n+1)
sum=0
for i in a:
    b=int(input("enter value:"))
    if b<0:
        break
    else:    
        sum=sum+b
print(sum)
    
    
    
    
    
