def count_digit(n):
    num=n
    count=0

    while num>0:
        count+=1
        num=num//10

    return count

n=int(input("enter the no:"))
print(count_digit(n)) 

        