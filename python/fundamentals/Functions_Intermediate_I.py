import random
def randInt(min= 0  , max= 100  ):

    num = random.random()*(max-min)+min

    return  round(num)

print(randInt())
print(randInt(min=50))
print(randInt(min=1, max=2))
print(randInt(max=80))