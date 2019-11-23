#slicing or indexing or poistive indexing 
s="hello!!! we are =learn python programming!!"
print(s)
print(len(s))
print(s[16:23])  # this slicing print in given range
print(s[16:31:2]) # increment of no
print(s[16]) # print the word in 16
print(s[16:]) # from index to last
print(s[:16]) # from start to index
print(s[:]) # prints all
new=s[::-1]#reverse 
print(new)

# negative indexing
s="kathir"
print(s[-1]) #prints the last word
print(s[-1:-7:-1]) # must inc by -1 rev word
print(s[-7:-4:-1]) # prints the correct word 
