print(" Topic : Factors or Divisors of the n Numbers. ")
# Brute force Solution :
n = int(input("Enter the number:"))
num = n
result = []               #[]= empty list

for i in range(1, num + 1):
    if num % i == 0:
        result.append(i)

print(result)  # TC= o(n) & SC = o(k)

# Better Solution :
n = int(input("Enter the number: "))
num = n
result = []

for i in range(1, num // 2+1):
    if num % i == 0:
        result.append(i)
result.append(n)
print(result)

  # TC= o(n/2)=o(n) because we not consisder constrain & SC = o(k)

# Optimal Solution :
from math import sqrt
n = int(input("Enter the number:"))
num = n
result = []               #[]= empty list

for i in range(1, int(sqrt(num))+1):
    if num % i == 0:
        result.append(i)
        if num//i !=i:
            result.append(num//i)
            
result.sort()    # if need it 
print(result) # TC= o(Square root of n) + o(nlogn) & Tc= o(k) amount of fact




