nums = [5,3,2,2,1,5,5,7,5,10]
m = [10,111,1,9,5,67,2]
hash_map = {}
n = len(nums)
for i in range(0,n):
    hash_map[nums[i]]=hash_map.get(nums[i],0)+1
for x in m:
    print(hash_map.get(x,0))