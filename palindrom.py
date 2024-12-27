Num=int(input("Enter the  Number:"))
Rem=0
Reverse_Num=0
Temp=Num
while(Num!=0):
    Rem=Num%10
    Reverse_Num=Reverse_Num*10+Rem
    Num=Num//10
if(Temp==Reverse_Num):
    print(Temp,"is a palindrom....!")
else:
    print(Temp,"not a palindrom")        