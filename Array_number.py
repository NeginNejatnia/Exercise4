list = []
n = int(input('enter number of list : '))
for i in range(0,n):
    listnumber = int(input())
    list.append(listnumber)
print(list)

flag = 0
i = 1
while i < len(list):
    if(list[i] < list[i - 1]):
        flag = 1
    i += 1

if (not flag) :
    print ("Yes, List is sorted.")
else :
    print ("No, List is not sorted.")




