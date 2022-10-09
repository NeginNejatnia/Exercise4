def Factorial(n) :
    i = 1
    while(True) :
         
        if (n % i == 0) : #baghi mande
            n //= i;  #khareje ghesmate sahih
             
        else :
            break
             
        i += 1
 
    if (n == 1) :
        return True
     
    else :
        return False
 
n = int(input('---> '))
ans = Factorial(n)
     
if (ans == 1) :
    print("Yes")
 
else :
    print("No")