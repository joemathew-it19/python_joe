number = int(input("enter a number"))
res =0
n = number
while(n>0):
    r=n%10
    res=res*10+r
    n//=10
if(res==number):
    print("the no is palindrome")
else:
    print("the no is not palindrome")
