def fact(n):
    if(n==1):
        return 1
    else:
        return n+fact(n-1)
no=int(input("enter a number"))
n=fact(no)
print("the SUM OF N NUMBER:",n)
