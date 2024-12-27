year=int(input("enter the year:"))
cout=20
leap_couunt=0
print("years are :")
while(leap_couunt!=cout):
    if(year%4==0 and year%100!=0) or (year%400==0):
        leap_couunt+=1
        print(year)
    year=year+1
