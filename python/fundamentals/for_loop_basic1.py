"""
Print numbers
"""
def printINT(x):
    for i in range(0,x):
        print(i)
printINT(151)

"""
Print the multipliers of 5
"""
def printML(y):
    for i in range(5,y):
        if (i % 5==0):
            print(i)
printML(1001)

"""
Print the Coding Dojo
"""
def dojo(z):
    for i in range(1,z):
        if(i%5!=0 and i%10!=0):
            print(i)
        elif(i%5==0 and i%10==0):
            print("Coding Dojo")
        elif(i%5==0):
            print("Coding")
        
dojo(101)

"""
Print the sum of the off
"""
def odd(x):
    y=0
    for i in range(0,100):
        if(i%2!=0):
            y=y+i
    print(y)
odd(500001)

"""
Print the count down by 4
"""
def downcount(z):
        for i in range(z,2, -4):
            i=i-4
            print(i)

downcount(2018)

"""
Print Multi
"""
def MULT(x,y,z):
    mult=0
    for i in range(x,y,z):
        mult=x*y
        print(x, mult, z)

MULT(2,3,9)
