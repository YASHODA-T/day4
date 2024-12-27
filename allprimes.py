Num=int(input("enter the  integer:"))
print("prime numbers are:")
for i in range(1,Num+1):
    for j in range(2,i):
        if(i%j==0):
            break

    else:
        print(i)    