Num=int(input("enter the Number:"))
count=0
'''for i in range(1,Num+1):
    if(Num%i==0):
        count+=1
if(count==2):
    print("Prime number:")
else:
    print("not a prime number:")'''
#=-----------------------------
for i in range(2,Num):
    if(Num%i==0):
        print("not a prime number") 
        break
else:
        print("Prime number")
           