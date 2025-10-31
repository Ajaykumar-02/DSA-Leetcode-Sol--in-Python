def reverse_no(n):
    num=n

    while num>0:
        last_digit=num%10
        print(last_digit)
        num=num//10
        

n=int(input("enter the no:"))
reverse_no(n) 

#tc=(log10N)
#sc=o(1)