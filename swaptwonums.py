#write apython program to swap two numbers bytaking the input from users
#1.using aurthematic operator
Num1=int(input("Enter the number:"))
Num2=int(input("Enter the number:"))
print("before swaping")
print("Num1",Num1)
print("Num2=",Num2)
Num1=Num1+Num2
Num2=Num1-Num2
Num1=Num1-Num2
print("After the swaping")
print("Num1=",Num1)
print("Num2=",Num2)
print("------------------------------------------------------")
#2.using third variable
Num1=int(input("Enter the number:"))
Num2=int(input("Enter the number:"))
print("before swaping")
print("Num1",Num1)
print("Num2=",Num2)
temp=Num1
Num1=Num2
Num2=temp
print("After the swaping")
print("Num1=",Num1)
print("Num2=",Num2)
print("------------------------------------------------------")
#3.without using third variable
Num1=int(input("enter the first number:"))
Num2=int(input("enter the second number"))
print("before swaping")
print("Num1=",Num1)
print("Num2=",Num2)
Num1,Num2=Num2,Num1 
print("After the swaping")
print("Num1=",Num1)
print("Num2=",Num2)
print("------------------------------------------------------")