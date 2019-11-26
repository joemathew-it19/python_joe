def fun(m):
    print(m)
    m[0]=0
    print(m)   #  [1,2,3]
k=[1,2,3]      # [1,2,3]
print(k)       # [0,2,3]
fun(k)         #[0,2,3]
print(k) # 0 is replace instead of 1 
