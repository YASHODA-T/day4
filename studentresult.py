#write a program to read the student name &scores of 3 subjects&print the student report card..
#i)print total,average
#ii)print 1st class >if average >90
#         2nd class >if average >75
#         3rd class > if average >60
#          fail      >  average <60
print("Student reort card:")
Name=str(input("Student Name:"))
sub1=int(input("Subject1 score:"))
sub2=int(input("Subject2 score:"))
sub3=int(input("Subject3 score:"))
total=sub1+sub2+sub3
average=total%3
print("Student Report card")
print("---------------------------------")
print("Student Name",Name)
print("Subject1:",sub1)
print("Subject2:",sub2)
print("Subject3:",sub3)
if(sub1>=35 and sub2>=35 and sub3>=35):
    print("Total",total)
    print("Average:",average)
    if(average>90):
       print("First Class")
    print("congratulations you have qualified with 1st class")
    elif(average>75):
         print("Second Class:")
    elif(average>60):
        print("Third Class") 
else:
    print("fail") 