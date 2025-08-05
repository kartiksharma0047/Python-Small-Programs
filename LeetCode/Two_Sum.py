# LeetCode Problem :-  1. Two Sum
nums=[2,7,11,15]
target=9
for i in range(0,len(nums)):
    for j in range(i+1,len(nums)):
        if target==nums[i]+nums[j]:
            print(list([i,j]))