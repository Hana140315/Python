
"""
Counter
"""
def count(z):
    counter=[]
    for i in range(z,0,-1):
      counter.append(i)
      print(counter)
count(5)

"""
Print return 
"""
def PR(list):
    print(list[0])
    return(list[1])
print(PR([2,3]))

"""
First Plus Length
"""
def FPL(list):
    print(list[0])
    return len(list)
print(FPL([4,6,7,2,3,4,10]))



"""
Values Greater than Second 
"""
def VGTS(list):
    if len(list)<2:
        #print("False")
        return False
    newlist=[]
    for i in list:
        if i> list [1]:
            newlist.append(i)
    print(len(newlist))
    return newlist

print(VGTS([3,5,7,9,8,2,5,1]))
print(VGTS([2,8]))


"""
This Length, That Value
"""
def LAV(x,y):
    lvalue=[]
    for i in range(x):
        lvalue.append(y)
    return lvalue
print(LAV(5,8)



