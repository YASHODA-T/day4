Num=int(input("Enter the Year:"))
if(Num%4==0 and Num%100!=0) or (Num%400==0):
    print(Num," is a leap year")
else:
    print(Num,"is not a leap year")