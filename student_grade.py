maths = float(input("enter your maths mark:"))
physics =  float(input("enter your physics mark:"))
chemistry =  float(input("enter your chemistry mark:"))  #print student details 
python =  float(input("enter your pyhton mark:"))
total = physics+maths+chemistry+python
avg = total/4
print("your average is:",avg)
if(avg>95) and (avg<=100):
    print("your grade is A")
elif(avg>90) and (avg<=94):
    print("your grade is B")
elif(avg>80) and (avg<=89):
    print("your grade is c")
elif(avg>70) and (avg<=79):
    print("your grade is d")
elif(avg>60) and (avg<=69):
    print("your grade is e")
elif(avg>50) and (avg<=59):
    print("your grade is f")
else:
    print("better luck next time")
