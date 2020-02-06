#eval function example with set operations
set1=set(map(int,input("Enter elements for set seperated by  (space)").split()))

N=int(input("Enter number of operation to be performed"))    #number of operations to be performed
for i in range (N):
    temp=input("enter command with arguments").split()
    cmd=temp[0]       #comand/operation to be perform
    args=temp[1:]     #arguments
    if(cmd!="print"):
        eval('set1.{0}{1}'.format(cmd,tuple(map(int,args))))
    else:
        print(set1)
