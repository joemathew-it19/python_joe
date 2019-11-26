# program to append and display 
d=open("new.txt","r")
s=d.read()
print(s)

g=open("new.txt","a")
g.write("welcome ")
g.close()


d=open("new.txt","r")
s=d.read()
print(s)
