# 4. Median of Two Sorted Arrays
# Given two sorted arrays nums1 and nums2 of size m and n respectively, return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
# Example :-
#   Input: nums1 = [1,2], nums2 = [3,4]
#   Output: 2.50000
#   Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.

nums1=[1,3]
nums2=[2]
# nums3=sorted(nums1+nums2)   # Shortcut

# We have another way to do this with looping which is this
nums3=[]
for ele in range(len(nums1)):
    nums3.append(nums1[ele])
for ele in range(len(nums2)):
    nums3.append(nums2[ele])
nums3=sorted(nums3)
if len(nums3)%2==0:
    mid_1=int(len(nums3)/2)
    mid_2=mid_1-1
    print("Median is: ",(nums3[mid_1]+nums3[mid_2])/2)
else:
    temp_mid=int(len(nums3)/2)
    print("Median is: ",nums3[temp_mid])