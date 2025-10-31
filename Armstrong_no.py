def Armstrongno(n):
    num=n
    total=0
    nod=len(str(n))

    while num>0:
        ld=num%10
        total=total+(ld**nod)
        num=num//10
    return total==n
# print(Armstrongno(1634))   

#tc=o(log10N)
#sc=o(1)
n=int(input("enter the no:"))
print(Armstrongno(n))


  