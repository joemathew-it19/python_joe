number = int(input("enter a number"))
res =0
n = number
while(n>0):
    r=n%10
    res+=r*r*r
    n//=10
if(res==number):
    print("the no is angstrong")
else:
    print("the no is not angstrong")
