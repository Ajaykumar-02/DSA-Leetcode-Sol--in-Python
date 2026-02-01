# print 1 to 50

count = 0
c = count
while (c<=50):
    print("HI",c)
    c +=1

# 50 to 1 

count = 50
c = count
while (c>=1):
    print("HI",c)
    c -=1

# multiplication table using loop
n = 3
i = 1
while (i<=10):
    print(n*i)
    i +=1

#for loop
n = int(input("enter the no:"))
for i in range(1,11):
    print(i*n)    

# print list using loops

l =[1,4,9,16,25,36,49,64,81,100]
idx =0
while idx < len(l):
    print(l[idx])
    idx +=1 

# search for a number X in this tuple using loop
x = 36
i =0
t = (1,4,9,16,25,36,49,64,81,100)
# print(len(t))
while (i < len(t)):
    if(t[i]==x):
        print(f"found at index {i} = {x}") # milne ke bad bhi find karta rehga 
        break # iss aage find nhi karega
    else:
        print("finding")  

#search for a number X in this tuple using loop
nums = (1,4,9,16,25,36,49,64,81,100,36)
x = int(input("enter the no: "))
idx=0
for i in nums:
    if(i == x):
        print("found at index",idx)
    
    idx +=1  

 # print list using for loops 
nums = [1,4,9,16,25,36,49,64,81,100]
for l in nums:
    print(l)                   

# Sum of first n numbers 
n = 5
sum=0
for i in range(1,n+1):
    sum = sum + i
print("Total Sum of n= ",sum)
# while 
sum=0
i=1
while(i<=5):
    # print(i)
    sum += i
    i += 1
    
print("Total Sum of n=",sum)  

# Factorial

n = 5
fact=1
for i in range(1,n+1):
    fact *= i
print("fact=",fact)

# while 
n = 5
fact=1
i=1
while(i<=n):
    # print(i)
    fact *= i
    i += 1
    
print("fact of n=",fact)