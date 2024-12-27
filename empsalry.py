#write a python program to read the employee name and designation and salary special allowances,bonus as input from the user
#i).gross monthly salary (salary+special allowance)
#ii).gross anual salary (gross monthly salary*12+bonus)
#caliculate the taxable income 
#if salary>500000--------------15% tax
#if salary>400000---------------10% tax
#salary>100000 to 300000--------2% tax
#print employee details
Name=str(input("Name of the Employee:"))
Des=(input("Designation of the Employee:"))
Sal=int(input("Salary of Employee:"))
Spcl=int(input("Special Allowances:"))
bonus=int(input("Bonus of the EMployee:"))
print("EMPLOYEE DETAILS :")
print("-----------------------------------")
print("EMPLOYEE NAME=",Name)
print("EMPLOYEE DESIGNATION=",Des)
print("EMPLOYEE SALARY=",Sal)
print("EMPLOYEE SPECIAL ALLOWANCES=",Spcl)
print("EMPLOYEE BONUS",bonus)
grossmonthlysalary=Sal+Spcl
grossannualsalary=grossmonthlysalary*12+bonus
print("grossmonthlysalary:",grossmonthlysalary)
print("grossannualincome:",grossannualsalary)
Taxable_income=0
if(Sal>500000):
    Taxable_income=grossannualsalary*15/100
    print("Taxable_income",Taxable_income)
elif(Sal>400000):
    Taxable_income=grossannualsalary*10/100
    print("Taxable_income:",Taxable_income-grossannualsalary)
else:
    Taxable_income=grossannualsalary*2/100
    print("Taxable_incone:",Taxable_income-grossannualsalary)