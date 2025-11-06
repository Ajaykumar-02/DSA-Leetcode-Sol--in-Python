nums=[5,6,7,7,1,9,1,1,5,1,1]

fre_map={} # method 1

for i in range(0,len(nums)):
    if nums[i] in fre_map:
        fre_map[nums[i]]+=1
    else:
        fre_map[nums[i]]=1
print(fre_map)   

hash_map={} # method 2
n=len(nums)
x=1

for i in range (0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
print(hash_map)    