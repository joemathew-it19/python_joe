def mini(a):
    c=a//60
    return c
def sec(a):
    d=a%60
    return d
a=int(input("enter your seconds"))
z=mini(a)
y=sec(a)
print("in minutes is :",z,"minutes ",y)
