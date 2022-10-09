import random
limit = int(input('n = '))
randomlist = []
for i in range(0,8):
        n = random.randint(1,limit)
        if not i in randomlist:
            randomlist.append(n)
print(randomlist,end = '')