#WAP to check that 'ilovepython' is present in a string or not

s=input("Enter a string")          # taking input from user
t=0                                 #initial index value 
for i in 'ilovepython':        
    if i in s[t:]:                  #checking if i present in s from index t
        t=s.index(i,t)+1            # if yes increase index t by 1
    else:           
        print("NO")                 #if i is not in s then print no
print("YES")
