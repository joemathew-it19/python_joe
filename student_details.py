name = input("enter your name:")
roll_no = input("enter your roll_no:")
maths = float(input("enter your maths mark:"))
physics =  float(input("enter your physics mark:"))
chemistry =  float(input("enter your chemistry mark:"))
python =  float(input("enter your pyhton mark:"))
total = physics+maths+chemistry+python
avg = total/4
print(' ****  student mark sheet ****')
print("NAME:",name)
print("ROLL_NO:",roll_no)
print("TOTAL MARKS :",total)
print("AVERAGE:",avg)
