def Palindroneno(n):
    num=n
    result=0
    

    while num>0:
        ld=num%10
        result=(result*10)+ld
        num=num//10
    return n==result

n=int(input("enter the no:"))
print(Palindroneno(n))    

#tc=o(log10N)
#sc=o(1)


