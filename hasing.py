n = [ 1,2,5,10,2,12,3,1,1,5]
m = [10,1,111,2,3,4,12,23]

 # Brute force Solution   tc=o(n*m) & sc=0(1)
for num in m:
    count=0
    for x in n:
        if x==num:
            count +=1
    print(count)        

# optimal Solution   tc=o(n*m) & sc=0(1)
n = [5, 3, 2, 2, 1, 5, 5, 7, 5, 10]
m = [10, 111, 1, 9, 5, 67, 2]

# # Given constraint: numbers are between 1 and 10
L = 11                     # because max number = 10
hash_list = [0] * L        # initialize list of size 11 with all zeros

# # Step 1: Store frequency of each number in n
for num in n:
    hash_list[num] += 1

# # Step 2: For each number in m, print its frequency (or 0 if out of range)
for num in m:
    if num < 1 or num > 10:
        print(0)
    else:
        print(hash_list[num])
n = [1, 2, 5, 10, 2, 12, 3, 1, 1, 5]
m = [10, 1, 111, 2, 3, 4, 12, 23]



#Dict: 
# # Step 1: Build frequency map from n
fre_map = {}
for i in range(len(n)):
    if n[i] in fre_map:
        fre_map[n[i]] += 1
    else:
        fre_map[n[i]] = 1

print("Frequency map:", fre_map)

# # Step 2: Check each m element's count in n
for num in m:
    if num in fre_map:
        print(f"{num} → {fre_map[num]}")
    else:
        print(f"{num} → 0")



# Character hasing:
s = "azyxyyzaaaa"
q = ["d", "a", "y", "x"]

# Step 1: Create hash list for 26 lowercase letters
hash_list = [0] * 26

# Step 2: Count frequency of each character in s
for ch in s:
    ascii_val = ord(ch)
    index = ascii_val - 97   # 'a' -> 0, 'b' -> 1, ...
    hash_list[index] += 1

# Step 3: Print frequency for each character in q
for ch in q:
    ascii_val = ord(ch)
    index = ascii_val - 97
    print(f"{ch} → {hash_list[index]}")



