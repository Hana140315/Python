"""
Biggle Size
"""
def changebig(list):
    newlist=[]
    x="big"
    for i in list:
        if i<0:
            newlist.append(x)
        else:
            newlist.append(i)
    return newlist

print(changebig([-1,5,7,-3,-8,10]))

"""
Count Positives
"""
def countpos(list):
    newlist=[]
    count=0
    for i in list:
        if i> 0:
            count+=1
        list[len(list)-1]=count
    return list
print(countpos([1,-7,-3,5,9,-49]))


"""
Sum Total
"""
def Total(list):
    total=0
    for i in list:
        total+=i
        print(total)
    return total
print(Total([1,-7,-3,5,9,-49]))


"""
Avarage
"""
def avrg(list):
    ava=0
    for i in list:
        ava+=i
    return ava/len(list)
print(avrg([1,-7,-3,5,9,-49]))
print(avrg([5,8,1,5,9,20]))


"""
length
"""
def leng(list):
    return len(list)
print(leng([1,-7,-3,5,9,-49]))
print(leng([5,8,1,5]))


"""
Minimum
"""
def mini(list):
    if len(list)<0:
        print("False")
        #return False
    min=0
    for i in list:
       if min>i:
           min= i
    return min 
    print(min)
print(mini([1,-7,-3,5,9,-49]))
print(mini([]))


"""
maximum
"""
def maxi(list):
    if len(list)<0:
        print("False")
        #return False
    max=0
    for i in list:
       if max<i:
           max= i
    return max
    print(max)
print(maxi([1,-7,-3,5,9,-49]))
print(maxi([]))

"""
Ultimate Analysis
"""
def UANA(list):
    Hdict = {'sumTotal': Total(list), 'average':avrg(list), 'minimum':mini(list), 'maximun': maxi(list), 'length': leng(list)}
    return Hdict
print(UANA([37,2,1,-9]))

"""
Reverse List
"""
def RL(list):
    for i in range (0, int(len(list)/2)):
        x=list[len(list)-1-i]
        list[len(list)-1-i]= list[i]
        list[i]=x
    return list
print (RL([1,2,3,4]))
print(RL([6,7,8,4,9,2,0,8,10,3]))